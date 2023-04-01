import json
import sys
data = json.load(open(sys.argv[1]))
class Game(object) :
    def __init__(self) -> None:
        self.mapp = data
        self.id = 0

       
        
        
    def prompt(self):
        self.promptname = str(self.mapp[self.id]['name'])
        self.promptdesc = str(self.mapp[self.id]['desc'])
        try:
            if len(self.mapp[self.id]['items']) != 0 :
                self.promptitems = ' '.join(self.mapp[self.id]['items'])
                self.promptitems ="Items: " + self.promptitems + "\n" + "\n"
            else :
                self.promptitems = ''
            
        except:
            self.promptitems = ''
        self.promptexits = ' '.join(self.mapp[self.id]['exits'].keys())
        self.promptline = "> " + self.promptname + "\n" + "\n" + self.promptdesc + "\n" + "\n"  + self.promptitems +"Exits: " + self.promptexits + "\n" + "\n" + "What would you like to do?"
     
        


class Verbs(Game) :

    def go(self) :
        self.verb = input(self.promptline).lower()
        if self.verb == "go" : 
            print("Sorry, you need to 'go' somewhere.")
            

        self.verblist = self.verb.split(" ")
        if len(self.verblist) == 2: 
            if  self.verblist[0] == "go": 
                if self.verblist[1] in self.mapp[self.id]['exits'].keys() : 
                    self.id = self.mapp[self.id]['exits'][self.verblist[1]]
                    print("You " + self.verb + "\n")
                    Verbs.go(self)
                    Game.prompt(self)
                    
                else: 
                    print("There's no way to go "+ self.verblist[1]+ ".")
                    




c = Game()
v = Verbs()
v.prompt()
v.go()


