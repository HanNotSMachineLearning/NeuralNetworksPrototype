# Testresultaten - Neural networks

In dit document staan de verschillende resultaten van het testen van het prototype uitgewerkt.

Developer: Robin

Reviewer 1:  Sander

Reviewer 2: 	



## Accuraatheid

Onder het onderdeel accuraatheid zijn een aantal verschillende zaken van het prototype getest beteft de accuraatheid van de gemaakte voorspelling.

#### Dataset grootte

Het eerste onderdeel dat getest is, is de toename van de accuraatheid van het algoritme naarmate de hoeveelheid beschikbare trainingsdata groter wordt. Dit is getest door het prototype te trainen kleinere hoeveelheden data van de volledige dataset. 

De onderstaande tabel bevat de waardes van de gemiddelde accuraatheids percentage van de applicatie die zijn gevonden door de applicatie te testen met de testdataset. 

| Percentage data          | Developer | Reviewer 1 | Reviewer 2 |
| ------------------------ | --------- | ---------- | ---------- |
| **25% van de dataset**   | 63⅓ %     | 53,33%     |            |
| **50% van de dataset**   | 73⅓ %     | 63,33%     |            |
| **75% van de dataset**   | 80 %      | 83,33%     |            |
| **100%  van de dataset** | 83⅓ %     | 83,33%     |            |

#### Aantal ingevoerde symptomen

Naast de afhankelijkheid van de accuraatheid ten opzichte van de grootte van de dataset is ook de accuraatheid van het prototype getest ten opzichte van het aantal ingevoerde symptomen waarmee de voorspelling moet worden gedaan. 

In de onderstaande tabellen staan de resultaten van de tests die zijn uitgevoerd om de accuraatheid te bepalen.

| 1 symptoom ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom   | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| -------------------- | --------------------- | ------------------ | ------------------- | ---------------------- | ------------------------------- |
| developer            | man                   | 21                 | hoesten             | astma                  | j                               |
| developer            | man                   | 53                 | pijn bij borst      | longontsteking         | n (astma)                       |
| developer            | vrouw                 | 18                 | niezen              | griep                  | n (verkoudheid)                 |
| developer            | vrouw                 | 25                 | kortademig          | astma                  | j                               |
| reviewer 1           | man                   | 17                 | Hoesten             | verkoudheid            | N (Astma)                       |
| reviewer 1           | man                   | 70                 | Niezen              | verkoudheid            | N (Longontsteking)              |
| reviewer 1           | vrouw                 | 44                 | Hoge slijmproductie | Bronchitis             | J                               |
| reviewer 1           | man                   | 38                 | Kortademig          | Astma                  | J                               |
| reviewer 2           |                       |                    |                     |                        |                                 |
| reviewer 2           |                       |                    |                     |                        |                                 |
| reviewer 2           |                       |                    |                     |                        |                                 |
| reviewer 2           |                       |                    |                     |                        |                                 |

| 2 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ----------------- | ---------------------- | ------------------------------- |
| developer             | vrouw                 | 36                 | hoesten, keelpijn | griep                  | j                               |
| developer             | man                   | 44                 | piepende ademhaling, kortademig | longontsteking | n (astma)                 |
| developer             | vrouw                 | 77                 | verstopte neus, niezen | verkoudheid       | j                               |
| developer             | man                   | 69                 | hoge slijmproductie, verstopte neus | bronchitis | n (astma)                 |
| reviewer 1            | man | 12 | Hoesten, Piepende ademhaling | Bronchitis | J |
| reviewer 1            | vrouw | 53 | Hoesten,  Kortademig | Astma | J |
| reviewer 1            | vrouw | 23 | Hoofdpijn, Vermoeidheid | Griep | N (Verkoudheid) |
| reviewer 1            | man | 25 | Verstopte neus, Niezen | Verkoudheid | J |
| reviewer 2            |                       |                    |                   |                        |                                 |
| reviewer 2            |                       |                    |                   |                        |                                 |
| reviewer 2            |                       |                    |                   |                        |                                 |
| reviewer 2            |                       |                    |                   |                        |                                 |

| 3 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ----------------- | ---------------------- | ------------------------------- |
| developer             | man                   | 22                 | hoesten, benauwdheid, verstopte neus | griep | j                             |
| developer             | vrouw                 | 55                 | spierpijn, vermoeidheid, neusvleugelen | longontsteking | j                  |
| developer             | vrouw                 | 88                 | hoesten, niezen, keelpijn | verkoudheid | n (astma)                          |
| developer             | man                   | 19                 | hoesten, piepende ademhaling, kortademig | bronchitis | n (astma)            |
| reviewer 1            | vrouw | 11 | Hoofdpijn,  Keelpijn, Hoesten | Verkoudheid | N (Griep) |
| reviewer 1            | vrouw | 19 | Verstopte Neus, Hoesten, Keelpijn | Verkoudheid | J |
| reviewer 1            | vrouw | 56 | Keelpijn, Hoge slijmproductie,  Pijn bij borst | Longontsteking | N (Griep) |
| reviewer 1            | man | 73 | Hoesten, Koorts, Keelpijn | Griep | J |
| reviewer 2            |                       |                    |                   |                        |                                 |
| reviewer 2            |                       |                    |                   |                        |                                 |
| reviewer 2            |                       |                    |                   |                        |                                 |
| reviewer 2            |                       |                    |                   |                        |                                 |

| 4 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ----------------- | ---------------------- | ------------------------------- |
| developer             | vrouw                 | 24                 | hoesten, hoofdpijn, neusvleugelen, vermoeidheid | longontsteking | j         |
| developer             | vrouw                 | 43                 | kortademig, benauwdheid, hoesten, piepende ademhaling | astma | j            |
| developer             | man                   | 20                 | hoesten, keelpijn, spierpijn, hoofdpijn | griep | n (verkoudheid)            |
| developer             | man                   | 99                 | hoge slijmproductie, koorts, spierpijn, piepende ademhaling | bronchitis | j |
| reviewer 1            | man | 37 | Benauwdheid,  Kortademig,  Hoesten,  Piepende ademhaling | Astma | J |
| reviewer 1            | vrouw | 24 | Neusvleugelen, Koorts, Kortademig,Vermoeidheid | Longontsteking | J |
| reviewer 1            | man | 44 | Hoesten, Keelpijn, Pijn bij borst, Piepende ademhaling | Bronchitis | N (Longontsteking) |
| reviewer 1            | vrouw | 61 | Gebrek aan eetlust, Hoesten,  Koorts, Niezen | Verkoudheid | N (Griep) |
| reviewer 2            |                       |                    |                   |                        |                                 |
| reviewer 2            |                       |                    |                   |                        |                                 |
| reviewer 2            |                       |                    |                   |                        |                                 |
| reviewer 2            |                       |                    |                   |                        |                                 |

| 5 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ----------------- | ---------------------- | ------------------------------- |
| developer             | man                   | 44                 | benauwdheid, piepende ademhaling, hoesten, kortademig, koorts | astma | n (bronchitis) |
| developer             | man                   | 22                 | hoesten, hoge slijmproductie, piepende ademhaling, koorts, spierpijn | bronchitis | j |
| developer             | vrouw                 | 56                 | hoesten, gebrek aan eetlust, koorts, keelpijn, verstopte neus | verkoudheid | n (griep) |
| developer             | vrouw                 | 33                 | koorts, hoesten, keelpijn, spierpijn, verstopte neus | griep | j             |
| reviewer 1            | man | 21 | Koorts, Hoesten, Hoofdpijn, Keelpijn,  Hoge slijmproductie | Griep | J |
| reviewer 1            | man | 66 | Hoesten, Keelpijn,  Hoge slijmproductie,  Pijn bij borst,  Kortademig | Bronchitis | N (Griep) |
| reviewer 1            | man | 45 | Keelpijn, Gebrek aan eetlust, Spierpijn,  Vermoeidheid,  Verstopte Neus | Verkoudheid | N (Griep) |
| reviewer 1            | vrouw | 28 | Hoesten,  Benauwdheid,  Gebrek aan eetlust,  Kortademig,  Neusvleugelen | Astma | N (Griep) |
| reviewer 2            |                       |                    |                   |                        |                                 |
| reviewer 2            |                       |                    |                   |                        |                                 |
| reviewer 2            |                       |                    |                   |                        |                                 |
| reviewer 2            |                       |                    |                   |                        |                                 |
