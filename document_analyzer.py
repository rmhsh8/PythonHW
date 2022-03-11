import string
d = dict()
text = open("document.txt", encoding = "utf8")
for line in text:
    line = line.translate(line.maketrans("", "", string.punctuation))
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
x = {}   
for key in list(d.keys()):
    x[key] = d[key]
sort = sorted(x.items(), key = lambda x:(-x[1],x[0]))
top5 = list(sort)[:5]
print(" ")
for i in top5:
    print(f"{i[0]}: {i[1]}")