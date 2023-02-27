import instances
from hacktoolchat import HacktoolChatbot
from chatui import UI

def run():
    ip = input("Enter IP address: ")
    if ip not in instances:
        return

    time = instances[ip].time
    msgs = instances[ip].msgs
    sols = instances[ip].sols
    final_lines = instances[ip].final_lines

    chatbot = HacktoolChatbot(msgs, sols, final_lines)
    ui = ChatUI(chatbot.start, chatbot.respond, countdown_timer=time)
    chatbot.link_say(ui.say)

    ui.start()

run()
