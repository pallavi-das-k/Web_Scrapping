#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup


# In[ ]:


import re


# In[ ]:


from urllib.request import urlopen


# In[ ]:


f = urlopen('https://www.')


# In[ ]:


s = BeautifulSoup(f, 'html.parser')
s = s.get_text()


# In[ ]:


p2 = re.findall(r"\+\d{2}\s?0?\d{10}",s)
p3 = re.findall(r"(\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4})",s)
p4 = re.findall(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",s)
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",s)


# In[ ]:


print(set(p2))
print(set(p3))
print(set(p4))
print(set(emails))


# In[ ]:




