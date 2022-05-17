f=open("test.txt")
filelines=f.readlines()
linecount=0
charactercount=0
wordcount=0
for line in filelines:
    linecount=linecount+1
    words=line.split()
    wordcount=wordcount+len(words)
    for character in line:
        charactercount+=1
print(linecount,wordcount,charactercount)

