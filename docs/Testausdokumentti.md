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

# Aikojen testaus
Iterativiisen syvenemisen testaus on tiedostossa test_time.py.

Testattu minimaxia eri syvyksiillä ja katsottu paljon aikaa siihen menee.
-Käyty läpi syvyydet 1-9, kutsuttu iterative funktiota tällä syvyydellä ja laskettu siihen kulunut aika. Samalla myös testattiin heuristiikka-arvon muuttumista syvyyden kasvaessa.

Tämä palauttaa arvot:

1 3 5000 0.0

2 1 -100 0.0

3 2 5000 0.006177425384521484

4 3 -100 0.009221792221069336

5 3 5000 0.031735897064208984

6 3 -100 0.07682180404663086

7 3 5000 0.4119851589202881

8 3 -100 1.0381157398223877

9 3 5000 10.007506132125854

Testattu toimivatko eri aikarajat ja kestääkö iterative funktion suorituksessa todella enintään aikarajan verran
-testattu aikarajoilla 0.5, 1.0, 2.0, 3.0. Luotu pelitilanne ja kutsuttu iterative funktiota ja mitattu tähän kuluva aika.

Tämä palauttaa arvot:

Time limit 0.5s: best column=3, took=0.514s

Time limit 1.0s: best column=3, took=1.002s

Time limit 2.0s: best column=3, took=2.006s

Time limit 3.0s: best column=3, took=3.011s





#### Testikattavuusraportti
<img width="814" height="222" alt="image" src="https://github.com/user-attachments/assets/a424ce38-b21c-4d69-ac2c-7da9a1ddd0ae" />


