import random

class Location(object):

    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):

    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc): # loc is a location object
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

    def reportLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk].getX(), self.drunks[drunk].getY()

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(start.distFrom(f.getLoc(d)))

def simWalks(numSteps, numTrials):
    homer = UsualDrunk('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f,homer,numSteps))
    return distances
    


def walkRecord(f, d, numSteps):
    start = f.getLoc(d)
    coordinates = []
    for s in range(numSteps):
        f.moveDrunk(d)
        coordinates.append(f.reportLoc(d))
    return coordinates

def simWalkRecord(numSteps):
    homer = UsualDrunk('Homer')
    origin = Location(50, 50)
    f = Field()
    f.addDrunk(homer, origin)
    return walkRecord(f, homer, numSteps)

import pylab

def drunkRoute(steps):
    coordinates = simWalkRecord(steps)
    xCoords = []
    yCoords = []
    for i in coordinates:
        xCoords.append(i[0])
        yCoords.append(i[1])
    gridLimit = max(max(xCoords), abs(min(xCoords)),\
    max(yCoords), abs(min(yCoords)))
    pylab.plot(xCoords, yCoords)
    pylab.xlim(-gridLimit, gridLimit)
    pylab.ylim(-gridLimit, gridLimit)
    pylab.show()
    
def drunkTest(numTrials = 20):
 for numSteps in [10,100,1000,10000]:
     distances = simWalks(numSteps, numTrials)
     print 'Random Walk of  ' + str(numSteps) + 'steps'
     print 'Mean =', sum(distances)/len(distances)
     print 'Max =', max(distances), 'Min =', min(distances)
     
     