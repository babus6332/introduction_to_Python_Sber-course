
# coding: utf-8

# In[ ]:


def lcm(a,b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)
 
with open("input.txt",'r') as file_in:
    for line in file_in:
        a = line.split(' ')
    ans = lcm(int(a[0]),int(a[1]))
with open('output.txt','w') as file_out:
    file_out.write(str(ans))
    

