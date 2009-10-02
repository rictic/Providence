# statesave.py - Test single VR checkpointing
from river.core.vr import VR

class Hello(VR):
    
    def counter(self):
        j = 0
        for i in range(10):
            j += i
    
    def main(self):
        """Call counter, but also include some computation outside of counter()"""
        k = 0
        for i in range(10): k += 1
        self.counter()
        for i in range(10): k += 1
