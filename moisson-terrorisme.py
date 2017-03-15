#coding: utf-8 

#Le moissonnage est très incomplet. Le script qui fonctionne se termine à la ligne 40.
#J'ai laissé des traces de certains de mes essais suivant cette ligne.
#Je suis au courant que la page que j'ai choisi «moissonne» déjà des données
#Même si il peut être pertinent de transcoder ces données en .csv ou .xls
#J'ai choisi cet url en connaissance de cause: python n'est pas une facilité pour moi et je souhaitais choisir
#une option relativement facile pour moi
#Visiblement ça n'a pas nécessairement aidé


import csv
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/United_States_State_Department_list_of_Foreign_Terrorist_Organizations"

fichier = "terroriste.csv"

entetes = {
	"User-Agent":"Louis Pelchat-LAbelle - Requête envoyée dans le cadre d'un cours de journalisme informatique à l'UQAM (EDM5240)",
	"From":"louis.atmosphere@hotmail.com"
}

contenu = requests.get(url, headers=entetes)
page = BeautifulSoup(contenu.text,"html.parser")


i=0


for ligne in page.find_all("tr"):
     if ligne.td is not None:
         #date = ligne.a.get("table")
         page= ligne.text
         print(page)
         
         f = open(fichier,"a")
         pouet = csv.writer(f)
         pouet.writerow(page)
         
#Lorsque j'essayais des formules comme les suivantes pour isoler mes valeurs:

#for ligne in page.find_all("tr"):
     #if ligne.td is not None:
         #page= ligne.text
         #print(page[td])
         
#Ou celle-là
         
#for ligne in page.find_all("tbody"): #(ou n'importe quelle autre variable exepté td et tr)
     #if ligne.td is not None:
       
         #page= ligne.text
         #print(page)
         
#Sois le script ne roulais même pas, et ne faisais qu'ajouter une ligne vide au bash
#Où alors j'avais le message d'erreur suivant: 
#TypeError: string indices must be integers
#Problème pour lequel j'ai tenté tant bien que mal de trouver des solutions dans stackoverflow,
#l'aide du syllabus de github, ou le bit.ly sur le moissonnage que tu nous avais fourni.
#Voici quelques-uns de ces essais
         
         
         #for i in page.find_all("tbody"):
            #if i.text.strip()=="td":
                #print(i.find_next("tr")).text.strip()

        #for ligne in page.find("td"):
        
        #print(ligne.content)
        
        #print(ligne.find_all("td"))
        
        #if ligne.text.strip("td") == "tbody":
        
        #print(ligne.find_next("td").text.strip)
        
#Rendu au moment où j'aurais pu isoler mes valeurs à l'aide de crochet [] à un endroit où un autre de mon script
#Il aurait été facile de les organiser pour ensuite les exporter en .csv.
# Il aurait fallu que je les identifie à des variable que j'aurais mise ensemble dans un print
#Voici un exemple avec du script fictif et non fonctionnelle, à l'aide de balise imaginaires

#for ligne in page.find_all("tr"):
     #if ligne.td is not None:
         #datecreation = ligne.a.get("a")[tr]
         #nom = ligne.a.get("td")[tr]
         #pays= ligne.a.get(tbody)[tr]
         #region= ligne.a.gt("p")[tr]
         
        #terreur= (datecreation,nom,pays,region)
        
        #print(terreur)
        
#J'ai tout de même créer un .csv avec mon script fonctionnel même si mes données ne sont pas du tout isolées
#Et que tout es très illisible.
#Cependant, les informations que je voulais isolées se retrouvent parmi celle contenue dans le .csv

#Merci et bonne semaine :) 
         
         
         
