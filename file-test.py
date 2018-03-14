f = open('/home/harsh/Entertainment/python_training/files/ajay.txt','r')
s = f.read()
letter_counts={}
for word in f.read().split():
	if word in s:
    	word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)