# Määrittelydokumentti
Suoritan kurssin Tietojenkäsittelytieteen kandiohjelmassa (TKT).
## Ohjelmointikielet
Toteutan harjoitystyön Pythonilla. Hallitsen vain Pythonin siinä määrin, että voin toteuttaa vertaisarvioinnin.  
## Aihe
Toteutan työssäni minimax-algoritmin. Työssä on myös alfa-beeta-karsinta, heuristiikka-funktio, iteratiivinen syvennys ja saman pelaajan viereisiä nappuloita laskeva algoritmi.
Käytän työssäni tietorakenteina listoja esim. pelilaudan esittämiseen, käytät sanakirjaa tallentamaan jo laskettuja tiloja sekä tupleja ja kokonaislukuja apuna.
Ohjelma saa syötteenä kokonaisluvun väliltä 0-6, jotka vastaavat saraketta johon nappula halutaan pudottaa. Tekoälyalgoritmi saa syötteekseen pelilaudan, jonka pohjalta se päättelee parhaan siirron. Iteratiivinen syveneminen saa syötteekseen aikarajan ja syvyyden.  
Minimaxin aikavaativuus on O(b^d). Alfa-beeta-karsinnan avulla se voi päästä O(b^(d/2)). b on haaratumisluku ja d on syvyys. Algoritmi tarvitsee sen verran aikaa, koska se katsoo kaikki mahdolliset siirrot ja jokaiselle siirrolle niitä seuraavat siirrot syvyyteen d asti. Minimaxin tilavaativuus on O(b·d), koska pelilauta aina kopioidaan. 

## Ydin
Toteutan pelin Connect4, jossa pelaaja kilpailee tekoälyä vastaan saadakseen neljä pelimerkkiä peräkkäin 6x7-kokoiselle pelilaudalle.
Tavoitteena on luoda tehokas tekoäly Minimax-algoritmia ja sen optimointeja käyttäen, joka pystyy löytämään parhaan mahdollisen siirron.  
Tekoälyn ohjelmoinnissa käytän Minimax-algoritmia siirtojen läpi käymiseen. Algoritmia tehostetaan alfa-beeta-karsinnalla, joka estää turhien siirtojen analysoinnin. Algoritmia nopeutetaan myös iteratiivisella syventämisellä. 
Pelitilanteen hyvyyttä arvioidaan yksinkertaisella heuristiikkafunktiolla.
Tietorakenteina käytän hajautustaulua, johon talletetaan edellisellä kierroksella arvioitu mahdollisimman paras siirto. Pelilautana on kaksiulotteinen lista, johon talletetaan pelinappuloiden sijainnit.

## Lähteet
https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html



