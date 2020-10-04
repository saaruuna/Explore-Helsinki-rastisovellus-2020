# Explore-Helsinki-rastisovellus-2020
Harjoitustyö kurssille Tietokantasovellus.

VÄLIPALALUTUS 3:
Sovellukseen voi tutustua osoitteessa http://explore-helsinki.herokuapp.com/. Sovellus toimii nyt käyttäjän puolella tarkoituksenmukaisesti. Käyttäjä pystyy suorittamaan rastin sekä
tarkastelemaan suoritettuja rasteja.

TODO:
- admin-toiminnallisuus: admin näkee, kuinka monta suoritettua rastia on käyttäjää kohti kategorioittain
- navigointi: käyttäjä pystyy navigoimaan kategorioiden perusteella
- timestampin lisääminen suorituksiin tarkastelua varten
- sovelluksen ulkoasun muokkaaminen paremmaksi
- bugin korjaaminen: session ei pääty jos käyttäjä sulkee selaimen


VÄLIPALAUTUS 2:
Sovellukseen voi tutustua osoitteessa http://explore-helsinki.herokuapp.com/. Siellä tulisi olla kirjautumistoiminnalisuus ja näennäinen mahdollisuus "suorittaa" rasti. Etusivulta voi lähteä tarkastelemaan listaa rasteista, kirjautumaan sisään tai luomaan käyttäjätunnus. Kun käyttäjä on kirjautunut sisään, tulisi näkyä rastin suoritustoiminnallisuus. Tämän varsinainen toteutus on vielä vaiheessa. Tähän palautukseen tähtäsin siihen, että sovellus ei kaadu, kun rasti "suoritetaan".

EDIT 22.9.2020: Kirjautuminen toimii nyt herokussa, toisin kuin kirjoitin palautukseen. Korjaus ei vaatinut muutoksia koodiin.



VÄLIPALAUTUS 1:
Projektin nimi on Explore Helsinki - rastisovellus. Sovelluksella on tarkoitus pystyä etsimään rastikiertelyyn kuuluvia rasteja sekä merkitä niitä suoritetuksi. Sovelluksen inspiraationa on rastikiertely, jota toteutan opiskelijajärjestölleni. Rastikiertely on suunnattu Helsinkiin muuttaneille opiskelijoille, jotka haluavat tutustua kaupunkiin. Aikaa rasteissa käymiseen on rajattomasti.

Kuvaus sovelluksen keskeisistä toiminnoista:

- Sovelluksen avulla voi suorittaa rasteja ja lisätä uusia rasteja.
- Käyttäjä voi olla peruskäyttäjä tai ylläpitäjä.
- Käyttäjä voi merkitä rastin suoritetuksi lataamalla kuvan kohteesta.
- Ylläpitäjä voi lisätä ja poistaa rasteja.
- Rastilla on jokin seuraavista kategorioista: Sports & Nature, Art & Architecture, Food & Drink, Culture & History.
- Ylläpitäjä voi tallentaa kuvauksen rastista.
- Rastit näkyvät kartalla.
- Käyttäjä näkee profiilissaan gallerian suoritetuista kohteista.
- Ylläpitäjä näkee, mitä rasteja käyttäjä on suorittanut.
