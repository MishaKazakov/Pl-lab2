import re

file = open("nign_exmpl.txt", "r")
text = file.read()
ips = re.findall('\d+\.\d+\.\d+\.\d+', text)
ips.sort()
word = []
word.append(ips[0])
for i in range(1,len(ips) + 1):
    if i == len(ips):
        print(word)
        break
    ip1 = re.search('\d+\.\d+\.\d+', word[len(word)-1] ).group(0)
    ip2 = re.search('\d+\.\d+\.\d+', ips[i]).group(0)
    if ip1 <> ip2:
        print(word)
        word = []
        word.append(ips[i])
        continue
    else:
        word.append(ips[i])
    
