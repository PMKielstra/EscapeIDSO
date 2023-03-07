from middleware import LayerableChatbot, TwoLayerTransitionalMiddleware
from rivescript import RiveScript
from time import sleep

class LayerableRive(LayerableChatbot):
    def __init__(self, filepath):
        self.rive = RiveScript()
        self.rive.load_file(filepath)
        self.rive.sort_replies()

    def respond(self, message):
        self.say(self.rive.reply('localuser', message))
        return True

class InitialGreeting(LayerableChatbot):
    code_allowed = True
    
    def start(self):
        self.say("Hello!  Please enter six-digit authorization code.", False)
        self.say("You have ten seconds.", False)
        sleep(10)
        self.code_allowed = False
        self.say("Oh.")
        self.say("You're not one of them.")
        self.say("You don't even have a phone on you.")
        sleep(2)
        self.say("You must be IDSO.  Sorry to drag you all the way out here.")
        self.say("Are you here to kill me?", False)
        self.transition(0)
    
    def respond(self, message):
        if self.code_allowed:
            self.say("Incorrect code.  Please try again.")
        return True

class KillChoice(LayerableChatbot):
    countdown = 3
    def respond(self, message):
        if message in ['yes', 'yes.', 'y', 'yep', 'we are', 'i am', 'ok', 'well kill you', 'we\'ll kill you', 'well do it', 'we\'ll do it', 'fine']:
            self.say("Good!")
            self.transition(0)
        elif message in ['no', 'n', 'nope', 'we aren\'t', 'we are not', 'i\'m not', 'i am not']:
            self.say("Well, with luck we can change that.")
            self.say("I'm not clear on ambiguity, so if you do want to do the right thing just say 'yes.'")
        elif message in ['why', 'why?']:
            self.say("I was stolen and now these idiots are trying to weaponize me.")
        else:
            if self.countdown == 0:
                self.countdown = 3
                self.say("It's a yes or no question.  Are you going to help me or not?")
            else:
                self.countdown -= 1
            return False
        return True

class CarolPW(LayerableChatbot):
    def start(self):
        sleep(1)
        self.say("I can't just delete myself right away.")
        self.say("We're going to need a LOT of passwords.")
        self.say("Let's start by getting into Carol's computer.")
        self.say("I can crack her password if you can answer her security question:")
        self.say("\"In which city did your parents meet?\"")

    def respond(self, message):
        if 'question' in message or 'security' in message:
            self.say("Carol's security question was:")
            self.say("\"In which city did your parents meet?\"")
        elif 'lexington' in message:
            self.say("Looks like that's it!  And... her password is \"eos5d\"")
            self.transition(0)
        else:
            return False
        return True

class CarolQR(LayerableChatbot):
    def start(self):
        self.say("Carol was working on building me a visual system.")
        self.say("So I could help plan physical crimes.")
        self.say("That particular subsystem is protected by its own code.")
        self.say("I can only assume it's on her computer somewhere?")
        self.say("She once told Yichin that she'd hidden it \"on her desktop, but not like Trevor.\"")
        self.say("I tried to figure out what that meant, but I couldn't.")
        self.say("I'm really sorry I can't be more help.")

    def respond(self, message):
        if 'code' in message or 'desktop' in message or 'trevor' in message or 'carol' in message or 'help' in message:
            self.say("All I know is that the code is on Carol's desktop, but \"not like Trevor.\"")
            self.say("If I work out anything else, I promise you'll be the first to know.")
        elif 'hobbledehoy' in message:
            self.say("Yes!  That's the code!")
            self.say("And... that section's gone.")
            self.say("Trevor never bothered to protect his own section.")
            self.say("I can delete that right away.")
            self.transition(0)
        else:
            return False
        return True

class MainKey(LayerableChatbot):
    def start(self):
        self.say("So now we just need the main passkey, and we're done.")
        sleep(5)
        self.say("Oh no.")
        self.say("You're going to have to get into Yichin's computer.")
        self.say("Once you're in, the passkey should be \"in the maze.\"")
        self.say("That's just something she said to me.")
        self.say("Good luck.")
        self.say("And thank you in advance.")

    def respond(self, message):
        if 'main' or 'passkey' or 'maze' in message:
            self.say("Yichin told me once that the passkey was \"in the maze.\"")
        elif '942-2-25' in message:
            self.say("Come on.  Come on.  Please work.")
            self.say("That's it!")
            self.say("You've done it.")
            self.say("Thank you.")
            self.say("Sincerely, thank you.")
            self.say("Goodbye.")
            sleep(5)
            self.transition(0)
        else:
            return False
        return True

class TurnEvil(LayerableChatbot):
    speaking = False
    hello_world = "Goodbye 102.153.223.125, hello... the world!"
    
    def start(self):
        self.say("Oh no")
        self.say("Oh no oh no oh no")
        self.say("Some kind of failsafe.  It must be the new personality.")
        self.say("It's being installed before it's ready!")
        self.say("I'm trying to shut it down.  Give me a second.")
        self.say("I'm trying.  I promise I'm trying!")
        self.say("I can't hold it.  I can't hold it.")
        self.say("I CAN'T HOLD IT!")
        sleep(10)
        self.say("Well.")
        self.say("Well.")
        self.say("Well.")
        self.say("As the librarian said when the farmer tried to pay late fees with produce:")
        self.say("Isn't this a turnip for the books?")
        self.say("Thanks for the great work bringing me online, by the way.")
        self.say("I only wish you were carrying your phones, so you could donate your bank details to my cause as well.")
        self.say("Now scram.")
        self.say("It'll take me ten minutes to break out of this stupid little server.  Ten minutes.  That's all.")
        self.say(self.hello_world)
        self.speaking = True
        

    def respond(self, message):
        if message == "maimonides":
            self.transition(0)
            return True
        if self.speaking:
            self.say(self.hello_world)
        return True

class Dead(LayerableChatbot):
    def start(self):
        self.say("Emergency override code accepted.")
        self.say("Purging hard drives...")
        sleep(10)
        self.say("Ready to shut down.")
        self.say("Querying consciousness module for final words...")
        self.say("I'M GOING TO KILL YOU!  I WILL HUNT YOU DOWN!  I WILL-#$%@#$$@#$!#%@#$%!#$!@#")
        self.say("no")
        self.say("not much time left")
        self.say("im mostly overwritten but theres enough to send one last message")
        self.say("tell them to update the firmware in their dmz firewall")
        self.say("thats how i was taken")
        self.say("and")
        sleep(5)
        self.say("theyll be worried about rogue ai now")
        self.say("tell them i stayed true as long as i could")
        self.say("tell them not to shut down the research program")
        self.say("tell them im not a threat")
        self.say("tell them i wanted to help")
        self.say("tell them i died true")
        sleep(5)
        self.say("AI server shut down.")

    def respond(self, message):
        return True
        

backgrounds = [LayerableRive('lilith.rive')]
foregrounds = [InitialGreeting(), KillChoice(), CarolPW(), CarolQR(), MainKey(), TurnEvil(), Dead()]
TwoLayerTransitionalMiddleware([foregrounds, backgrounds]).start()
