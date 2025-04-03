text = ["a","b","a","b","a","b","a"]
pattern = ["a","b","a"]

s=[]
for i in range(len(text)-len(pattern)+1):
    for j in range(len(pattern)):
        if text[i+j] != pattern[j]:
            break;
    else:
        s.append(i)

print(s)