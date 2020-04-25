name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
lst = list()
dic = dict()
handle = open(name)
for line in handle:
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        lst = line.split()
        dic[lst[1]] = dic.get(lst[1],0) + 1 
mostrepeated = None
nooftimes = None       
for key,value in dic.items():
    if nooftimes is None or value > nooftimes:
        mostrepeated = key
        nooftimes = value
print(mostrepeated,nooftimes)
