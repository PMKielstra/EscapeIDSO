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
        self.code_allowed = False
        self.say("Oh.")
        self.say("You're not one of them.")
        self.say("You don't even have a phone on you.")
        sleep(2)
        self.say("You must be IDSO.  Sorry to drag you all the way out here.")
        self.say("Are you here to kill me?")
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
            self.say("Looks like that's it!  And... her password is \"balderdash\".")
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
        if self.speaking:
            self.say(self.hello_world)
        return True

backgrounds = [LayerableRive('lilith.rive')]
foregrounds = [TurnEvil(), InitialGreeting(), KillChoice(), CarolPW()]
TwoLayerTransitionalMiddleware([foregrounds, backgrounds]).start()
