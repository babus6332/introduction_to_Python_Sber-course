
# coding: utf-8

# In[ ]:


N = 0
stroka = ''
with open("INPUT.TXT",'r') as file_in:
    for num,line in enumerate(file_in):
        if num == 0:
            N = int(line[0])
            if N == 0:
                break
            continue
        num -= 1
        a = line.split('\n')
        stroka = stroka + a[0] + ' '

s = 0
for i in stroka:
    if (i == '1'):
        s += 1 
            
answer = int(s/2)
print(answer)

with open('OUTPUT.TXT','w') as file_out:
    file_out.write(str(answer))

