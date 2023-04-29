### Test code to see how Github works
import math as math
import random as random
from random import choices

class coin():
    def __init__(self,hBias=0.5):
        self.hBias=hBias
        pass
    def toss(self):
        r=choices(('heads','tails'),[self.hBias,1-self.hBias])
        return(r)
    
c=coin(0.1)
print(c.toss())
