print("Starting app")
minsup = 1
flie = "catSample.txt"
file = open(flie)
file2 = open(flie)
full = file2.read()
full = full.replace("\n"," ")
lines = file.readlines()
file.close()
file2.close()
lines = [line.replace("\n"," ") for line in lines]
print("Got basic data")
print(4)
words = {}
wrds = []
lined = {key: [] for key in full.replace("\n", " ").split(" ")}
lined[''] = []
print("Creating one word patterns")
for h in range(0, len(lines)):
    hs = lines[h].replace("\n", "").split(" ")
    for word in hs:
        wrds.append(word)
        lined[word].append(h)
wrds = list(filter(None,wrds))
print("Counting one word patterns")
wrds = list(set(wrds))
for w in range(0, len(wrds)):
    count = len(lined[wrds[w]])
    words[wrds[w]] = count
print("Filtering one words")
wordF = list(filter(lambda x: words[x] > minsup, words))
wordDct = {}
for i in wordF:
    print("%s : %d" %(i,words[i]))
print("Program done")
