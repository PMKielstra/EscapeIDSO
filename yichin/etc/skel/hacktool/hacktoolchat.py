class HacktoolChatbot:
    def __init__(self, msgs, sols, final_lines):
        assert len(msgs) == len(sols)
        self.msgs = msgs
        self.sols = sols
        self.final = final
        self.solved = False

    def link_say(self, say):
        self.say = say

    def print_security(self):
        self.say("Encountered security measure:")
        self.say(msgs[0])

    def start(self):
        self.print_security()

    def respond(self, attempt):
        if self.solved:
            for f in final_lines:
                self.say(f)
            return
        
        if attempt == self.sols[0]:
            self.say("Security measure bypassed.")
            self.sols.pop(0)
            self.msgs.pop(0)
            if len(self.sols) == 0:
                self.solved = True
            return

        self.say("Attempt failed.  Security measure still operational.")
        self.print_security()
        
            
