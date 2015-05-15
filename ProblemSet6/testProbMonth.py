import random
def testJune(trials):
    a = 0
# run trials 
# randomly see birth in 0 11
# increment any month

    june48 = 0.0
    for trial in range(trials):
        june = 0
        for i in range(446):
            if random.randint(1,12) == 6:
                june += 1
        
        if june >= 48:
            june48+=1


    print 'chance of born in june ' + str(june48/trials)

def testMonth(trials):
    a = 0
# run trials 
# randomly see birth in 0 11
# increment any month

    any48 = 0.0
    
    for trial in range(trials):
        monthBorn = [0.0]*13
        for i in range(446):
            monthBorn[random.randint(1,12)] += 1

        if max(monthBorn) >= 48:
            any48+=1


    print 'chance of born in any month ' + str(any48/trials)

    