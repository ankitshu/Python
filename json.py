#import json
#letter_counts[letter] = letter_counts.get(letter, 0) + 1
f=open('/home/harsh/Test-Abhishek/abhi')
print(f.name)

counter = 1;
dict1 = {};
for line in f:
    #print (line)
    sLine = line.split()
    #print(sLine) 
    for sWord in sLine:
        #print(sWord)
        dict1[sWord]= dict1.get(sWord, 0) + 1
        #print(dict1)
f1=open('/home/harsh/Test-Abhishek/dict1_file.txt','w')
import json
json.dump(dict1,f1)
f1.close()
f1=open('/home/harsh/Test-Abhishek/dict1_file.txt','r+')
contentInF1=json.load(f1)
print(contentInF1)
    