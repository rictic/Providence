from river.core.vr import VR

k = 1000

def func(): 
    a = 100
    def nested():
        n = 1
        for i in range(k): n += n * a
        return n
    return nested()

class NestedScoper(VR):
    def main(self):
        print func()
        