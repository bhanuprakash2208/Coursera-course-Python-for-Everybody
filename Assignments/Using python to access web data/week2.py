import re 
handle = open('forsubmission.txt')
num_list=[]
for line in handle:
    l = re.findall('[0-9]+',line)
    if len(l)!=0:
        for i in l:
            num_list.append(int(i))
print(sum(num_list))
