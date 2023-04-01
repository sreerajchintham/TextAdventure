import json
import sys
data = json.load(open(sys.argv[1]))
map = [{'name': 'A white room', 'desc': 'You are in a simple room with white walls.', 'exits': {'north': 1, 'east': 3}}, {'name': 'A blue room', 'desc': 'This room is simple, too, but with blue walls.', 'exits': {'east': 2, 'south': 0}}, {'name': 'A green room', 'desc': 'You are in a simple room, with bright green walls.', 'exits': {'west': 1, 'south': 3}, 'items': []}, {'name': 'A red room', 'desc': "This room is fancy. It's red!", 'exits': {'north': 2, 'west': 0}, 'items': ['rose']}]

class Game(object) :
    def __init__(self) -> None:
        self.mapp = data
        self.id = 0

       
        
        
    def action(self):
        self.promptname = str(self.mapp[self.id]['name'])
        self.promptdesc = str(self.mapp[self.id]['desc'])
        try:
            if len(self.mapp[self.id]['items']) != 0 :
                self.promptitems = ' '.join(self.mapp[self.id]['items'])
                self.promptitems ="Items: " + self.promptitems + "\n" + "\n"
            
        except:
            self.promptitems = ''
        self.promptexits = ' '.join(self.mapp[self.id]['exits'].keys())
        self.promptline = self.promptname + "\n" + "\n" + self.promptdesc + "\n" + "\n"  + self.promptitems +"Exits: " + self.promptexits + "\n" + "\n" + "What would you like to do?"
     
        self.verb = input(self.promptline)
        self.verblist = self.verb.split(" ")
        if  self.verblist[0] == "go": 
            if self.verblist[1] in self.mapp[self.id]['exits'].keys() : 
                self.id = self.mapp[self.id]['exits'][self.verblist[1]]
                print("You" + self.verb + "\n\n")
                Game.action(self)

    def go(self) :

            






    def __repr__(self) -> str:
        return f'{self.mapp[self.id]["name"]}\n{self.mapp[self.id]["desc"]}\n'
c = Game()
c.__init__()
c.action()
