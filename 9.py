
# coding: utf-8

# In[ ]:


s, m = 0,1
num = []
with open("input.txt",'r') as file_in:
    for line in file_in:
        a = line.split(' ')
    for i in range(len(a)):
        num.append(int(a[i]))
        if (((int(a[i])) > 0)):
            s = s + int(a[i])
    mn = min(num)
    mx = max(num)
    for i in range(len(num)):
        if (num[i] == mn):
            index1 = i
        if (num[i] == mx):
            index2 = i
    if (index1 <= index2):
        for i in range(index1+1,index2):
            m = m * num[i]
    else:
        for i in range(index2+1,index1):
            m = m * num[i]
with open('output.txt','w') as file_out:
    file_out.write(str(s))
    file_out.write(' ')
    file_out.write(str(m))

