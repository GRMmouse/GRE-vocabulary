import os, random
from Tkinter import *
from vocab_helper import *

class Game(object):
    def __init__(self,width=800,height=600):
        self.width=width
        self.height=height

###########
## Model ##
###########                          
    def initAnimation(self):
        self.timerDelay=100
        content = read("vocab.txt").splitlines()
        random.shuffle(content)
        self.vocabs = map(lambda s: s.split('@'), content)
        self.length = len(self.vocabs)
        self.curIndex = 0

##########
## View ##
########## 
    def redrawAll(self):
        self.canvas.delete(ALL)
        if (self.curIndex < self.length):
            t = self.vocabs[self.curIndex][0]
        else:
            t = "End of List"
        cx = self.width/2
        cy = self.height/2
        self.canvas.create_text(cx, cy, text = t, font="Arial 40 bold")
        
#############
## Control ##
#############
            
    def sizeChange(self,event):
        self.width=event.width
        self.height=event.height
        self.redrawAll()

    def onLeftMousePressed(self,event):
        # The user knows the word
        if (self.curIndex < self.length):
            self.vocabs[self.curIndex][2] = str(max(0, int(self.vocabs[self.curIndex][2])-1))
            self.curIndex +=1
        self.redrawAll()
        
    def onRightMousePressed(self,event):
        # The user does not know the word
        if (self.curIndex < self.length):
            self.vocabs[self.curIndex][2] = str(int(self.vocabs[self.curIndex][2])+1)
            print("The meaning of %s is:"%self.vocabs[self.curIndex][0])
            meaning = (self.vocabs[self.curIndex][1]).split('#')
            for i in xrange(len(meaning)):
                print ("%d. %s"%(i+1, meaning[i]))
            print
            self.curIndex +=1
        self.redrawAll()

    def onTimerFired(self):
        if (self.curIndex >= self.length):
            return
        self.redrawAll()
        self.canvas.after(self.timerDelay,self.onTimerFired)

    def run(self):
        self.root=Tk()
        self.canvas=Canvas(self.root,width=self.width,height=self.height)
        self.canvas.pack(fill=BOTH,expand=YES)
        #os.system(self.cmd)
        #winsound.PlaySound("song.mp2",winsound.SND_FILENAME)
        self.root.bind("<Configure>", self.sizeChange)
        self.root.bind("<Button-1>",self.onLeftMousePressed)
        self.root.bind("<Button-3>", self.onRightMousePressed)
        self.initAnimation()
        self.onTimerFired()
        self.root.mainloop()
        content = map(lambda l:  "@".join(l), self.vocabs)
        write("vocab.txt", "\n".join(sorted(content)))
        print("Done")

def main():
    game=Game()
    game.run()

main()
