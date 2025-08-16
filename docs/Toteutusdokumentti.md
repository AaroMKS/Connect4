# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelmassa on main-funktio, joka ylläpitää pelin kulkua ja vaihtaa pelaajan vuoroa. Ohjelmassa on funktiot, jotka tarvistavat voittotilanteet ja mahdollisen tasapelin. 
Ohjelmassa on tekoäly, joka pelaa käyttäjää vastaan connect4-peliä.

Ohjelman käynnistettyä, käyttäjältä pyydetään numeroa väliltä 0-6, joka kirjoittamalla asetetaan sille sarakkeelle pelilaudalla.
Pelinappula menee alimpaan vapaaseen riviin sillä sarakkeella. Sen jälkeen ohjelma kutsuu minimax-algoritmia, joka laskee parhaan mahdollisen pelivuoron, jonka se ohjelma toteuttaa.
Minimax-algoritmi käy läpi kaikki sarakkeet ja laskee heuristiikkafunktion avulla, mikä sarakkeista on optimaalisin.
Se etsii mahdollisia neljän rivejä sekä kolmen ja kahden rivejä, joissa on tyhjää jomalla kummalla puolella. Jos pelinappula saa aikaan neljän rivin, ohjelma ilmoittaa voitosta. Jos pelilauta on täynnä ohjelma tarkistaa mahdollisen voiton ja muuten ilmoittaa tasapelistä.



## Laajojen kielimallien käyttö

Käytetty ChatGPT-tekoälyä selittämään ohjeita yksinkertaisemmin, auttamaan komentorivin käytössä, githubin käytössä, selittämään käsitteitä,
kuten poetry ja auttamaan pääsemään ohjelman kehityksessä alkuun.

## Lähteet
https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html
