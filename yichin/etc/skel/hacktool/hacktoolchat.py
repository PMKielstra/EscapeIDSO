class HacktoolChatbot:
    def __init__(self, msgs, sols, final_lines):
        assert len(msgs) == len(sols)
        self.msgs = msgs
        self.sols = sols
        self.final_lines = final_lines
        self.solved = False

    def link(self, say, stop_clock):
        self.say = say
        self.stop_clock = stop_clock

    def print_security(self, first_time=True):
        if first_time: self.say("Encountered security measure:")
        self.say(self.msgs[0])

    def start(self):
        self.print_security()

    def respond(self, attempt):
        if self.solved:
            self.stop_clock()
            self.say("Run successful.")
            for f in self.final_lines:
                self.say(f)
            return
        
        if attempt == self.sols[0]:
            self.say("Security measure bypassed.")
            self.sols.pop(0)
            self.msgs.pop(0)
            if len(self.sols) == 0:
                self.solved = True
                self.respond("")
            else:
                self.print_security()
            return

        self.say("Attempt failed.  Security measure still operational.")
        self.print_security(False)
        
            
