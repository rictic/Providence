import cPickle as pickle
from river.core.vr import VR
from river.core.objdump import objdump
from sys import stderr

STATE_VR_IGNORE_ATTRS = ['atomic', 'keys', 'parent', 'state_enabled',
    'sysvr', 't', 'vm', 'vri']

class InvalidResult(object):
    def __init__(self, exception=None):
        pass
        
class InvalidState(object):
    def __init__(self, exception=None):
        pass

class dumpstate(VR):
    def main(self):
        argv = self.argv[1:]
        filename = None
        index = None
        if len(argv) > 0:
            filename = argv[0]
            argv = argv[1:]
        else:
            print 'usage: dumpstate <filename> [<index>]'
            return False
        
        state_file = open(filename, 'r')
        self.index = pickle.load(state_file)
        state_file.close()
        
        results = self.get_watch_results(argv)
        csv_file = open(filename+".csv",'w')
        print >> csv_file, ",".join(argv)
        for result in results:
            if (type(result) is InvalidState):
                print >> stderr, repr(result)
                continue
            print result
            print >> csv_file, ",".join(str(x) for x in result)
        csv_file.close()

    def get_watch_results(self, watches):
        for i in range(len(self.index['states'])):
            state_str = self.index['states'][i]
            try:
                state = pickle.loads(state_str)
            except Exception, e:
                yield InvalidState(e)
                continue
            yield self.get_watches(watches, state)
            
    def get_watches(self, watches, state):
        if (not (state and state.t and state.t.frame)):
            return InvalidState()
        objdump(state.t.frame.f_code)
        results = []
        for watch in watches:
            try:
                results.append(eval(watch, state.t.frame.f_globals, state.t.frame.f_locals))
            except Exception, e:
                results.append(InvalidResult(e))
        return results
