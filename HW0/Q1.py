f = open('words.txt')
words = f.read()
words = words.split()
words[-1] = words[-1].split('\n')[0]
d = {}
l = []
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
        l.append(word)
        
Q = open('Q1.txt', 'w')
for k in d:
    print(k, str(l.index(k)), str(d[k]))
    if k != l[-1]:
        Q.write((k+' '+str(l.index(k))+' '+str(d[k])+'\n'))
    else:
        Q.write((k+' '+str(l.index(k))+' '+str(d[k])))
        
Q.close