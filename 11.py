
# coding: utf-8

# In[ ]:


k, n = map(int, input().split())
a = [1, 1]
for i in range(2, n + 1):
    a.append(sum(a[len(a) - min(k, len(a)):]))
print(a[n])

