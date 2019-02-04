import patch

# -----------------------

def getFunctionName(frame):
    'Returns the name of the function containing the given frame.'
    return frame.f_code.co_name

level = 0
def trace_call(frame):
    'Do something before a call.'
    global level
    level +=1
    print "%s> %s" % ("-"*level, getFunctionName(frame)) 

def trace_exit(frame):
    'Do something after return of a call.'
    global level
    print "<%s %s" % ("-"*level, getFunctionName(frame)) 
    level -=1

# -----------------------

def testSort():
    import sort
    patch.apply_patch(sort.go, trace_call, trace_exit)
    sort.go('test.txt')

def testExample():
    import example
    patch.apply_patch(example.start, trace_call, trace_exit)
    example.start()

def testShort():
    class A(object):
        def y(self):
            print self.x
        def x(self):
            return 3
    
    def start():
        print "asdf"
        a = A()
        a.y = 2
        a.x()
        print a
        a.x()
    
    patch.apply_patch(start, trace_call, trace_exit)
    start()

# -----------------------

if __name__=='__main__':
    #testSort()
    testExample()
    #testShort()

