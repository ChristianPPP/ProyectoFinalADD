#!/usr/bin/env python
# coding: utf-8

#In[0]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
from turtle import ht
from bs4 import BeautifulSoup
import requests
import pymongo

#In[1]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
client= pymongo.MongoClient("mongodb+srv://admin:agujeronegro@cluster0.21fzo.mongodb.net/test")
nombredb=client['weapons']
db=nombredb['damages']

#In[0]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
urlBase = "https://warframe.fandom.com/wiki/Weapon_Comparison"
maxPages = 5
counter = 0
for i in range(1,maxPages):
    # Construyo la URL
    if i > 1:
        url = "%spage/%d/" %(urlBase,i)
    else:
        url = urlBase
    # Realizamos la petición a la web
    req = requests.get(url)
    # Comprobamos que la petición nos devuelve un Status Code = 200
    statusCode = req.status_code
    if statusCode == 200:
        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text, 'html.parser')
        # Recorremos todas las entradas para extraer la fecha y tema 
        for row in html.find_all('tr')[:970]: 
            # Find all data for each column
            columns = row.find_all('td')
            try:
                if (columns[0].text=='Name'):
                    print('vacio')
                else:
                    doc = {
                        'Name': columns[0].text,
                        'Weapon Type': columns[1].text,
                        'Trigger': columns[2].text,
                        'Attack': columns[3].text,
                        'Main Element': columns[4].text,
                        'Base Dmg': columns[5].text,
                        'Multishot': columns[6].text,
                        'Fire rate': columns[7].text,
                        'Crit': columns[8].text,
                        'Crit Dmg': columns[9].text,
                        'Status': columns[10].text,
                        'Reload': columns[11].text,
                        'Mag Size': columns[12].text,
                        'Avg Shot': columns[13].text,
                        'Burst DPS': columns[14].text,
                        'Sust DPS': columns[15].text,
                        'Avg Procs per sec': columns[16].text,
                        'Reserve Ammo': columns[17].text,
                        'PT': columns[18].text,
                        'Dispo': columns[19].text,
                        'MR': columns[20].text
                    }
                    #db.insert_one(doc)
            except IndexError:
                pass
    else:
        # Si ya no existe la página y me da un 400
        break
# %%
