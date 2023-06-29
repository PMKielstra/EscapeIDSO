from instances import get_instance
from hacktoolchat import HacktoolChatbot
from chatui import ChatUI

def run():
    ip = input("Enter IP address: ")
    instance = get_instance(ip)
    if not instance:
        print("No target found at this IP address.")
        input("Press enter to quit.")
        return

    time = instance.time
    msgs = instance.msgs
    sols = instance.sols
    final_lines = instance.final_lines

    chatbot = HacktoolChatbot(msgs, sols, final_lines)
    ui = ChatUI(chatbot.start, chatbot.respond, countdown_timer=time)
    chatbot.link(ui.add_line, ui.stop_clock)

    ui.start()

run()
