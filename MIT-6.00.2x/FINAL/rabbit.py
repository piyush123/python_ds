import random
import pylab 



CURRENTRABBITPOP = 500
CURRENTFOXPOP= 30
MAXRABBITPOP = 1000

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    
    reprod = int(100*(1.0 - float(CURRENTRABBITPOP)/float(MAXRABBITPOP)))
    
    current = CURRENTRABBITPOP
    for r in range(current):
        if CURRENTRABBITPOP < MAXRABBITPOP:
            prob = random.randint(0,99)
            print "++++"
            print  reprod, prob
            if reprod > prob:
                print "===="
                print reprod,prob
                CURRENTRABBITPOP += 1
    
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    
    probeat = int(float(CURRENTRABBITPOP)/float(MAXRABBITPOP)*100.0)
    currentpop = CURRENTFOXPOP
    
    print 'current pop ' + str(currentpop)
    print 'eat '+str(probeat)
    for f in range(currentpop):
        print 'current pop f' + str(f)
        if CURRENTRABBITPOP > 10:
            eat = random.randint(0,99)
            print probeat, eat
            if probeat > eat:
                newfox = random.randint(0,2)
                print 'fox ' +str(newfox)
                CURRENTRABBITPOP -= 1
                if newfox == 0:
                    CURRENTFOXPOP += 1
                    print CURRENTFOXPOP
            else:
                deadfox = random.randint(1,10)
                if deadfox > 1 and CURRENTFOXPOP > 10:
                    CURRENTFOXPOP -= 1
                

    #print "----"
    #print CURRENTRABBITPOP, CURRENTFOXPOP

        
    


def runSimulation(numSteps):

        rabbit_populations = []
        fox_populations = []
        # TO DO
        for i in range(numSteps):
            rabbitGrowth()
            rabbit_populations.append(CURRENTRABBITPOP)
            foxGrowth()
            fox_populations.append(CURRENTFOXPOP)
        #print 'rabbits ' + str(CURRENTRABBITPOP)
        #print 'fox ' + str(CURRENTFOXPOP)
        steps = []
        steps.extend(range(numSteps))
        pylab.plot(steps,fox_populations, label = 'fox')
        pylab.plot(steps,rabbit_populations, label ='rabbit')
        pylab.legend(loc='upper right')
        #pylab.plot.xlim(500)
        #pylab.plot.ylim(4000)
        pylab.xlabel(' steps ')
        pylab.ylabel(' pop ')
        pylab.ylim(-50,800)
        pylab.xlim(-50,200)
        #pylab.plot.show()
        print "---"
        print max(rabbit_populations)
        print max(fox_populations)
        
        coeff = pylab.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
        
        pylab.plot(pylab.polyval(coeff, range(len(rabbit_populations))))
        
        coeff2 = pylab.polyfit(range(len(fox_populations)), fox_populations, 2)
        
        pylab.plot(pylab.polyval(coeff2, range(len(fox_populations))))
        
        print 'coeff ' + str(coeff)
        return((rabbit_populations,fox_populations))