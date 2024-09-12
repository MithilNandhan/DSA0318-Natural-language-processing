text="The ab bought a cab at lab station"
words=text.split()
found=[]
for word in words:
    state=0
    for char in word:
        if state==0:
            if char=='a':
                state=1
            else:
                state=0
        elif state==1:
            if char=='b':
                state=2
            elif char=='a':
                state=1
            else:
                state=0
        elif state==2:
            if char=='a':
                state=1
            else:
                state=0
        if state==2:
            found.append(word)
print(found)
