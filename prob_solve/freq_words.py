text = ""
with open("notes.txt", 'r', encoding="utf-8") as f:
    text = f.read()
    
words = text.split(" ")
dic = {}

for word in words:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
        
        
print(dic)
