from river.core.vr import VR

n = 1000

def counter():
    """Count up to n and keep a running sum of values so far"""
    j = 0
    for i in range(n):
        j += i

class CounterRunner(VR):
    def main(self):
        """Call counter, but also include some computation outside of counter()"""
        k = 0
        for i in range(n): k += 1
        counter()
        for i in range(n): k += 1
