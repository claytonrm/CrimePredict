
# coding: utf-8

# In[5]:


import requests
import json
from lxml import html
from IPython.display import display, HTML


# In[6]:


url = 'http://dados.gov.br/dataset/sistema-nacional-de-estatisticas-de-seguranca-publica'


# In[7]:


session = requests.Session()
response = session.get(url=url)

root = html.fromstring(response.conten)


# In[15]:


list = root.xpath('//*[@class="resource-url-analytics"]')


# In[16]:


for i, row in enumerate(list[1:]):
    url_data_resource = row.attrib['href']
    data = session.get(url=url_data_resource)
    
    with open('crimes_by_city.txt' , 'a') as out:
        decode_content = data.content.decode('ISO-8859-1')
        out.write(decode_content)
        

