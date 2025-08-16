# Määrittelydokumentti
Suoritan kurssin Tietojenkäsittelytieteen kandiohjelmassa (TKT).
## Ohjelmointikielet
Toteutan harjoitystyön Pythonilla. Hallitsen vain Pythonin siinä määrin, että voin toteuttaa vertaisarvioinnin.  
## Aihe
Toteutan pelin Connect4, jossa pelaaja kilpailee tekoälyä vastaan saadakseen neljä pelimerkkiä peräkkäin 6x7-kokoiselle pelilaudalle.
Tavoitteena on luoda tehokas tekoäly Minimax-algoritmia ja sen optimointeja käyttäen, joka pystyy löytämään parhaan mahdollisen siirron.  
Tekoälyn ohjelmoinnissa käytän Minimax-algoritmia siirtojen läpi käymiseen. Algoritmia tehostetaan alfa-beeta-karsinnalla, joka estää turhien siirtojen analysoinnin. Algoritmia nopeutetaan myös iteratiivisella syventämisellä. 
Pelitilanteen hyvyyttä arvioidaan yksinkertaisella heuristiikkafunktiolla.
Tietorakenteina käytän hajautustaulua, johon talletetaan edellisellä kierroksella arvioitu mahdollisimman paras siirto. Pelilautana on kaksiulotteinen lista, johon talletetaan pelinappuloiden sijainnit.

Ohjelmalle annetaan syötteenä aina numero väliltä 0-6, joka kuvaa saraketta, johon nappula pudotetaan. Tekoäly saa syötteenä pelitilanteen ja vuorossa olevan pelaajan, joiden avulla se laskee parhaan mahdollisen siirron. Molempien siirrot talletetaan pelilautaan.
Voiton tarkistuksen aikavaatimus on O(1), koska se käy läpi vain rivit, jotka sisältävät edellisen siirron.
Minimax-algoritmi voi viedä aikaa O(siirtojen määrä*syvyys), mutta tätä voidaan nopeuttaa Alfa-beeta-karsinnalla. Nämä voivat vielä muuttua täysin.
## Lähteet
https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html

