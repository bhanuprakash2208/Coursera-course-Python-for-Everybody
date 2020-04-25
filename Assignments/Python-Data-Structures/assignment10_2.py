name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
lst = []
dic = dict()
handle = open(name)
for line in handle:
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        lst = line.split()
        dic[lst[5][:2]] = dic.get(lst[5][:2],0) + 1 
#print(dic)
x = sorted([(key,value) for key,value in dic.items()])
for key, value in x:
    print(key,value)
