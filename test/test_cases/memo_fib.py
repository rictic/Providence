from river.core.vr import VR

cache = {1:1, 2:1}
def fib(n):
    gl = globals()
    if (n not in cache):
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

k = 20

class MemoFib(VR):
    
    def main(self):
        print fib(k)
        
