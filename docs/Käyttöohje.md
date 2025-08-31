Kloona ensin repositorio koneellesi.

Lataa riippuvuudet
```
poetry install
```
Suorita ohjelma komennolla 
```
poetry run python main.py
```
Ohjelma käyttää game.py-tiedoston board-luokka ylläpitämään pelilautaa ja tarkastamaan voittotilanteita.
Main.py funktiossa määritetääm kumman pelivuoro ja se kysyy pelaajan pelivuorolla peliliikettä, jonka jälkeen se kutsuu iterative-funktiota joka kutsuu minimax-funktiota iteratiivisesti, joka palauttaa optimaalisen pelivuoron.
Minimax-funktio kutsuu heuristiikkafunktiota, joka palauttaa kaikille sarakkeille tietyn heuristiikka-arvon.

Ohjelma hyväksyy käyttäjän syötteinä ainoastaan luvut 0-6. 


