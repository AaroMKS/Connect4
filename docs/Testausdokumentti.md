# Testausdokumentti


## Yleisesti
Tekoälyä vastaan on pelattu hyvin monia otteluja. Testattu erilaisia pelistrategioita ja testattu estääkö tekoäly voittoyritykset. Katsottu pelaako tekoäly ideaalisti ottaen varmat voitot ja luoden hyviä voittopiakkoja. Tekoälyn voittaminen on tällä hetkellä hyvin hankalaa, sillä tekoäly estää kaikki voittoyritykset hyvin tehokkaasti. Kokeiltu myös pelata omituisilla ja epäloogisilla strategioilla. 

## Peurstoimintojen testaus
Ohjelman perustoimintoja ollaan testattu tiedostossa test_game.py.

Testattu, että asetettu nappulaa menee oikealle sarakkeelle pohjalle. 
-testattu kaikilla seitsemällä sarakkeella

Testattu, että neljä päällekkäistä nappulaa antaa voiton.
-testattu kaikkilla seitsemällä sarakkeella, pelaajana 1

Testattu että neljän nappulan diagonaalinen suora antaa voiton. 
-testattu useilla napuloilla niin että 1 pelaajan nappulat muodostavat nousevan suoran 0-3 sarakkeilla.

Testattu että ohjelma ei anna laittaa täydelle kolumnille lisää nappuloita.
-testattu sarakkeella 0

Testattu että full_board-funktio palauttaa True, jos lauta on täynnä.
-testattu täyttämällä laudan jokainen kohta

Testattu että print_board toimii.
-asetettu nappulaa sarakkeeseen 0 ja katsottu onnistuuko funktion suoritus

## Tekoälyn testaus
Tekoälyä testattu tiedostossa test_ai.py

Testattu varman häviön välttämistä
-testattu tilanteessa jossa pelaajalla on 3 nappulaa päällekkäin sarakkeessa 1
-testattu tilanteessa jossa pelaajalla on 3 nappulaa diagonaalisesti peräkkäin alhaalta ylös sarakkeissa 0-3. Heuristiikan testaamiseki, pelilautaan lisättiin ylimääräisiä nappuloita

Testattu varman voiton ottamista
-testattu jos tekoälyllä on kolme päällekkäistä nappulaa sarakkeessa 1, se lisää yhden sen päälle
-varmaa voittoa on myös testattu monimutkaisella pelilaudalla, jossa tekoälyllä on mahdollisuus saada 4 diagonaalisesti nousevassa järjestyksessä. Sekä 0 että 4 täyttävät sen, mutta käyntijärjestyksen takia se asetetaan sarakkeeseen 4

Testattu heuristiikkafunktion palauttamia arvoja
-luotu pelitilanne jossa kahden ja kolmen rivejä ja laskettu käsin jokaisen sarakkeen heuristiikka-arvo ja katsottu palauttaako heuristiikkafunktio saman arvon eli -5000
-laskettu saman tilanteen jossa tarkasteliin varmaa diagonaalista voittoa heuristiikka-arvoa. Tulostettu jokaisen sarakkeen heuristiikka-arvo ja katsottu näyttävätkö ne oikeilta
-sama tehty myös tilanteelle jossa tarkastettu varmaa horisontaalista voittoa

Testattu että tekoäly ei valitse kolumnia joka on täynnä
-täytetty rivi 0 ja katsottu palauttaako minimax saman rivin




#### Testikattavuusraportti
<img width="814" height="222" alt="image" src="https://github.com/user-attachments/assets/a424ce38-b21c-4d69-ac2c-7da9a1ddd0ae" />


