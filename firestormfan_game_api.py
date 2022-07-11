
import random
class App:
    class Block:
        def __init__(self,x,y):
            self.x = x
            self.y = y
    def __init__(self,width=128,height=128):
        self.width = width
        self.height = height
        self.reset()
        self.bestscore=0
        self.blocks = []
        
        for i in range(-(-(self.width+16)//48)):
            x = i*(48)
            if i <3:
                y = self.height-64
            else:
                y = (self.height-80) + random.randint(0,60)
            self.blocks.append(self.Block(x,y))

    def reset(self):
        self.px = 0
        self.py = self.height-128
        self.pv = 0
        self.pvx = 0
        self.maxpvx = 3
        self.jump = -5
        self.vy = 0.2
        self.walkspeed = 2
        self.blockspeed =0.8
        self.score=0

    def update(self,jump:bool=False,left:bool=False,right:bool=False):
        self.btn_jump = jump
        self.btn_left = left
        self.btn_right = right

        self.pltx=0
        self.blockspeed = self.blockspeed+1/(60*60)
        self.py = self.py+self.pv
        self.ground = False
        if self.py>self.height:
            if self.score > self.bestscore:
                self.bestscore = self.score
            self.reset()
        
        if self.btn_left:
            self.pvx = self.pvx*self.walkspeed+1
        if self.btn_right:
            self.pvx = self.pvx*self.walkspeed-1

        if self.pvx>self.maxpvx:
            self.pvx = self.maxpvx
        elif self.pvx<-self.maxpvx:
            self.pvx = -self.maxpvx

        self.px = self.px-self.pvx/2
    
        self.pvx = self.pvx*0.5
        for block in self.blocks:
            block.x = block.x-self.blockspeed
            dx = self.px-block.x
            dy = self.py-block.y

            if abs(dx)<16 and abs(dy)<16:
                if abs(dx)<abs(dy):
                    if dy<4:
                        self.py = self.py-dy-16
                        self.pv = 0
                        self.ground = True
                        self.px = self.px-self.blockspeed
                    else:
                        self.py = self.py-dy+16
                        if self.pv<0:
                            self.pv=0
                else:
                    self.pvx = 0
                    if dx<0:
                        self.px = self.px-dx-16
                    else:
                        self.px = self.px-dx+16
            
            if block.x < -16:
                block.x = block.x+(-(-(self.width+16)//48))*48
                block.y = (self.height-80) + random.randint(0,60)
                self.score = self.score+10
        self.sound = False
        if self.btn_jump:
            if self.ground:
                self.sound = True
                self.pv = self.pv+self.jump
        
        self.pv = self.pv+self.vy

        ret = {
            'px':self.px,
            'py':self.py,
            'pv':self.pv,
            'pvx':self.pvx,
            'score':self.score,
            'bestscore':self.bestscore,
            'blocks':[{'x':block.x,'y':block.y} for block in self.blocks],
            'sound':self.sound,
            'ground':self.ground
        }
        return ret
