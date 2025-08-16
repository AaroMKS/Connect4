# Testausdokumentti
## Yksikkötestit
Yksittötesteissä ollaan käytetty unittest-kirjastoa. Yksikkötesteillä ollaan testattu pelin perusominaisuuksia, kuten nappulan asettamista, voittamista ja tekoälyn perustomintoja.
Ollaan testattu myös yksikkötesteillä, ottaako tekoäly varman voiton, kun on kolmen pystyrivi muodostettuna.
On myös testattu estääkö tekoäly vastustajan varman voiton, jos vastustajalla on kolmen pystyrivi.
Ollaan testattu palauttaako heuristiikkafunktio arvon 5000 tietyssä pelitilanteessa. 

## Muut testit
Ollaan pelattu huomattava määrä tekoälyä vastaan. Kokeiltu erilaisia strategioita. Tarkistettu ottaako tekoäly varman voiton ja estääkö se varman voiton. 

Testattu aikakatkaisun toimivuutta ja syvyyksien toimivuutta. Luotu funktio joka laskee minimaxin palauttaman heuristiikkaarvon ja kolumnin tietyissä eri syvyyksissä ja tarkasteltu näiden aikavaativuutta. Luotu myös funktio joka testaa meneekä funktion suoritusaika ikinä yli määritetyn max_depth muuttujan. 

#### Testikattavuusraportti
<img width="1534" height="536" alt="image" src="https://github.com/user-attachments/assets/cffa57bb-666b-410e-a212-d4d17ba2265e" />

