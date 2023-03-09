import curses
from threading import Thread
import time

class ChatUI:
    def __init__(self, bot_start, bot_respond, update_interval=60, countdown_timer=None):
        self.update_interval = update_interval
        self.bot_start = bot_start
        self.bot_respond = bot_respond
        self.lines = []
        self.temp_input = ""
        self.time_left = countdown_timer
        self.countdown_finished = False

    def draw(self):
        """Erase and redraw the screen based on the current state, but don't update curses."""
        self.stdscr.erase()
        lines = self.lines[-curses.LINES + 3:]
        for i, (line, bold) in enumerate(lines):
            if bold:
                self.stdscr.addstr(i, 0, line, curses.A_BOLD)
            else:
                self.stdscr.addstr(i, 0, line)
        if self.time_left is not None:
            time_str = time.strftime("%M:%S", time.gmtime(self.time_left))
            self.stdscr.addstr(0, curses.COLS - len(time_str), time_str, curses.A_STANDOUT)            
        self.stdscr.addstr(curses.LINES - 1, 0, '> ' + self.temp_input)
        self.stdscr.noutrefresh()

    def stop_clock(self):
        self.time_left = None

    def add_line(self, line, bold=True):
        """Add a line of text to the chat UI history."""
        self.lines += [(line, bold)]

    def update_loop(self):
        """Every 1/self.update_interval seconds, clear and redraw the screen.  This shouldn't cause any flicker."""
        while True:
            time.sleep(1/self.update_interval)
            self.draw()
            curses.doupdate()
            if self.time_left is not None:
                self.time_left -= 1/self.update_interval
                if self.time_left <= 0:
                    self.countdown_finished = True
                    print("Out of time.  Press any key to end run.")
                    del self.stdscr
                    return

    def input_loop(self):
        """Take user input at the bottom of the screen, and spawn a thread for the bot to process it."""
        while True:
            if self.countdown_finished: return
            user_input = self.stdscr.getkey()
            if user_input in ['\n', '\r', '\r\n']:
                if len(self.temp_input) > 0:
                    full_input = self.temp_input
                    self.temp_input = ""
                    self.add_line('> ' + full_input, False)
                    Thread(target=self.bot_respond, args=(full_input.lower(),)).start()
            elif user_input == 'KEY_BACKSPACE':
                self.temp_input = self.temp_input[:-1]
            elif len(user_input) == 1:
                self.temp_input += user_input

    def init_curses(self, stdscr):
        """Store a reference to the main screen window and start all the relevant threads."""
        self.stdscr = stdscr
        Thread(target=self.bot_start).start()
        Thread(target=self.update_loop).start()
        self.input_loop()

    def start(self):
        """Display and run the chatbot."""
        curses.wrapper(self.init_curses)
