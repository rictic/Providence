import cPickle as pickle
from river.core.vr import VR
from river.core.objdump import objdump

STATE_VR_IGNORE_ATTRS = ['atomic', 'keys', 'parent', 'state_enabled',
    'sysvr', 't', 'vm', 'vri']

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
        
        if len(argv) > 0:
            index = int(argv[0])
        
        state_file = open(filename, 'r')
        si= pickle.load(state_file)
        state_file.close()

        print 'State Info:'
        print 'UUID   :', str(si['uuid'])
        print 'APPID  :', str(si['appid'])
        print 'MODULE :', si['module']
        #print 'MODULE :', si['filename']
        print 'START  :', si['start']
        print 'END    :', si['end']
        print 'COUNT  :', si['count']
        
        if index is not None:
            states = si['states']
            print 'State Index %d:' % index
            vr = pickle.loads(states[index])
            vr.vri = None
            vr.vm = None
            objdump(vr)
            objdump(vr.t)
            objdump(vr.t.frame)
            #@self.dump_state(vr)
            del vr.t

    def dump_state(self, vr):
        self.objhash = {}
        self.dump_vr_state(vr)
        self.dump_tasklet_state(vr.t)
        
    def dump_vr_state(self):
        pass
        
    def dump_frame(self):
        pass
        
    def dump_tasklet_state(self):
        pass
    
