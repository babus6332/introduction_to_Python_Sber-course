
# coding: utf-8

# In[ ]:


even = ''
odd = ''
with open("INPUT.TXT",'r') as file_in:
    for line in file_in:
        a = line.split(' ')
    for i in range(len(a)):
        if (((int(a[i])) % 2) == 0):
            even = even + str(int(a[i])) + ' ' 
        else:
            odd = odd + str(int(a[i])) + ' ' 

with open('OUTPUT.TXT','w') as file_out:
    file_out.write(odd[:-1])
    if (odd != ''):
        file_out.write('\n')
    else:
        file_out.write('\n')
    file_out.write(even[:-1])
    if (even != ''):
        file_out.write('\n')
    else:
        file_out.write('\n')
    if (len(even) < len(odd)):
        file_out.write('NO')
    else:
        file_out.write('YES')

