#%%

import pandas as pd
import requests
from bs4 import BeautifulSoup
  
URL = "https://m.dk/stationer/"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

list_url = []
for link in soup.find_all('a'):
    list_url.append(link.get('href'))

list = []
for url in list_url:
    if url[:4] == '/sta':
        url = 'https://m.dk' + url
        list.append(url)


#%%
name_list = []
description_list = []
linjer_list = []
ind_list = []
type_list = []
elevator_list = []

#%%

for url in list:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')


    for name in soup.find_all("h1", class_="page-header__title"):
        name_list.append(name.text)

    for url in list:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        description = soup.find_all("div", class_="content-block__text")[0]
        description_text = description.find_all("p")[1]
        description_list.append(description_text.text)






#%%
    for Linjer in soup.find_all("li")[7]:
        linjer_list.append(Linjer.text)

    for ind in soup.find_all("li")[8]:
        ind_list.append(ind.text)

    for type in soup.find_all("li")[10]:
        type_list.append(type.text)

    for elevator in soup.find_all("li")[11]:
        elevator_list.append(elevator.text)



# %%
df = pd.DataFrame({'Name': name_list, 'Description': description_list, 'Linjer': linjer_list, 'Ind': ind_list, 'Type': type_list, 'Elevator': elevator_list})
df.to_csv('scrap.csv', index=False)
# %%
len(linjer_list)

# %%
print(ind_list)
# %%
print(name_list)
len(name_list)

#%%
print(description_list)
len(description_list)

#%%

    #funcionando a parte da descrição



# %%
df = pd.DataFrame({'nome': description_list})

#%%
df
# %%
