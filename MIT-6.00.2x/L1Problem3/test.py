
def suffixmatch(word,w):
    count = 0
   
    for i in range(len(w)):
        if (word[1:i] == w[1:i]):
            print word[0:i], w[0:i]
            count +=1 
        else:
            return count
    print count
    return count

def getsuffixes(word):
    suffixes = []
    for i in range(len(word)):
        suffixes.append((word[i:]))
    return suffixes
    
lines = int(raw_input())
a = 0
b = 0
word =[]
for i in range(lines):
        word.append(raw_input())
 
for h in range(len(word)):               
        suffixes = getsuffixes(word[h])
        for w in suffixes:
            a += suffixmatch(word, w)
           

        print a    
                

        