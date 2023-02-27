from chatui import ChatUI
from abc import ABC, abstractmethod
from time import sleep

class LayerableChatbot(ABC):
    def link(self, say_method, transition_method):
        self.say = say_method
        self.transition = transition_method
    
    @abstractmethod
    def respond(self, message):
        pass

    def start(self):
        pass

CHARS_PER_SEC = 8

class TwoLayerTransitionalMiddleware:
    def respond_level(self, level, message):
        return self.chatbot_lists[level][self.position[level]].respond(message)
    
    def respond(self, message):
        responded = False
        i = 0
        while not responded:
            responded = self.respond_level(i, message)
            i += 1

    def transition(self, level, direction=1):
        self.position[level] += direction

    def say(self, text, wait=True):
        self.UI.add_line(text)
        if wait:
            sleep(len(text) / CHARS_PER_SEC)
    
    def __init__(self, chatbot_lists, update_interval=60):
        self.chatbot_lists = chatbot_lists
        self.UI = ChatUI(self.chatbot_lists[0][0].start, self.respond, update_interval=update_interval)
        self.position = [0, 0]
        for chatbots in chatbot_lists:
            for chatbot in chatbots:
                chatbot.link(self.say, self.transition)

    def start(self):
        self.UI.start()
