import pylab

# You may have to change this path
WORDLIST_FILENAME = "C:\Users\Piyush\OneDrive\Documents\Python\Chapter3\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    props = []
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    proportion = 0
    for line in wordList:
        temp = 0
        total = len(line)
        for e in line:
            if e in vowel:
                temp = (temp + 1)
        print temp/float(len(line))
        props.append(temp/float(len(line)))
        
    pylab.hist(props,15)
    
    pylab.show()
    
                            
    
                
        
    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
