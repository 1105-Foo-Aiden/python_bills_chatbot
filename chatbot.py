import re
import random

class BillBot:
    negative_res = ("nothing", "don't", "stop", "sorry")
    exit_cmd = ("quit", "pause", "exit", "goodbye", "bye", "later", "no")
    
    def __init__(self):
        self.matching_phrases = {"how_to_pay_bill": [r'.*how.*pay bills.*', r'.*how.*pay my bill.*'], "pay_bill":[r'.*want.*pay my bill.*', r'.*need.*pay my bill.*']}
    
    def welcome(self):
        name = input("Hi welcome, what is your name so we can get started:\n")
        will_help = input(f'Okay, {name}, what can I help you with?\n')
        
        if will_help in self.negative_res:
            print("Okay, I will stop helping you.")
            
            return
        self.handleConvo(will_help)
    
    def handleConvo(self, reply):
        while not self.make_exit(reply):
            reply = self.match_reply(reply)
    pass
    
    def make_exit(self, reply):
        for cmd in self.exit_cmd:
            if cmd in reply:
                print("Okay, I will stop helping you.")
                return True
            
        return False
    
    def match_reply(self, reply):
        for key, values in self.matching_phrases.items():
            for pattern in values:
                found_match = re.match(pattern, reply)
                if found_match and key == "how_to_pay_bill":
                    return self.how_pay_bill_intent()
                if found_match and key == "pay_bill":
                    self.pay_bill_intent()
                
        return input("I can't understnad you, can you ask that in a different way? ")
    
    def pay_bill_intent(self):
        return input("inside self.pay_bill_intent()")
    
    def how_pay_bill_intent(self):
        return input("You can pay your bill a couple of ways.\n 1) online at bill.codecademybank.com or\n 2) you can pay your bill right now with me. \nCan I help you with anything else?\n")
    
    
cutstomer_sup = BillBot()
cutstomer_sup.welcome()