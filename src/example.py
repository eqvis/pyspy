import os
from pprint import pprint

class Banana(object):
    def eat(self, x=""):
        #print "eat", x
        pass

class Person(object):
    def __init__(self):
        self.no_bananas()
        self.something = ""

    def setSomething(self, value):
        self.something = value

    def no_bananas(self):
        self.bananas = []

    def add_banana(self, banana):
        self.bananas.append(banana)

    def eat_bananas(self):
        for i in range(len(self.bananas)):
            banana = self.bananas.pop()
            if calculate(i, len(self.bananas)):
                banana.eat('_if_')
                os.path.isfile("path")
                self.setSomething('foo')
                #print "eating!"
            elif i == 2: banana.eat('_elif_')
            else:
                banana.eat('x')
                
        self.no_bananas()

def calculate(x,y):
    result = x + y + x^2
    return (result/2)%2

def start():
    #print "INFO: running start()..."
    person = Person()
    #pprint(dir(person))
    calculate(2, 3)
    for a in xrange(2):
        person.add_banana(Banana())
    if False:
        pass
    person.eat_bananas()
    person.setSomething('bar')
    #s = person.setSomething
    #print dir(s)
    #print s.__func__, dir(s.__func__)


if __name__ == '__main__':
    start()

