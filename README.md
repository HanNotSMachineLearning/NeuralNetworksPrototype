# Documentatie neural network algoritme prototype

Dit prototype is onderdeel van een reeks van prototypes die gebouwd zijn ter ondersteuning van deelvraag 8: 'Welke algoritmes van machine learning sluiten het beste aan op deze casus? ' van het onderzoek 'Machine learning voor de huisarts'. Door middel van deze prototypes wordt getest welk machine learning algoritme het meest geschikt is om te gebruiken binnen de casus van het onderzoek. Alle prototypes worden geschreven in Python en maken gebruik van het TensorFlow machine learning framework.



## Algoritme

Het algoritme dat gebruikt wordt is een 'meerlagige perceptron' (MLP), en is een vorm van een neuraal netwerk waarbij informatie altijd in dezelfde richting loopt. Een neuraal netwerk is een groep van neuronen of zenuwcellen die verbonden met elkaar zijn. Het algoritme bestaat uit minstens drie lagen nodes. Deze lagen zijn de input, output laag met een of meerdere verborgen lagen. Behalve voor de input node is elke node een neuroon. MLP gebruikt een supervised learning techniek genaamd backpropagation om te leren.

## Trainingsdata

Om het machine learning algoritme te trainen wordt er gebruik gemaakt van een dataset bestaande uit ziektes en hun bijbehorende symptomen. De dataset is terug te vinden in de folder `Data`  binnen de projectfolder van het prototype.



## Afhankelijkheden

Zoals eerder genoemd is het prototype geschreven in python, om precies te zijn versie 3.6. Daarnaast wordt PIP versie 10.0 gebruikt voor het installeren en beheren van de verschillende externe packages die gebruikt worden in het prototype. Het is dus van belang dat de volgende zaken aanwezig zijn op machine waarop het prototype gedraaid wordt.

- Python versie 3.6   	(https://www.python.org/downloads/release/python-364/)
- Pip versie 10.0              (https://pip.pypa.io/en/stable/installing/)

```
!-- LETOP --!
Het is van belang dat python wordt toegevoegd aan je Windows Path variable. 
Hiervoor is een optie te vinden in de installatiewizzard van Python.
```



## Installatie

Om het prototype te draaien dienen er een aantal externe packages geïnstalleerd te worden:

- csv (voor het lezen van de dataset)
- sklearn (voor het aanleveren van functies om machine learning mogelijk te maken in Python)
- random (voor het shufflen van de dataset voordat je scheidt naar training- en testset)

Al deze packages zijn te installeren door het commando `pip install -r requirements.txt --user` uit te voeren in een Terminal venster in de projectfolder van het prototype. Dit commando zorgt ervoor dat alle benodigde packages in een keer gedownload worden.



## Opstarten

Het prototype kan gestart worden door het commando `python prototype.py` uit te voeren in een Terminal verster in de projectfolder van het prototype.



## Code
```python
import csv
from random import shuffle
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# read csv files
available_symptoms = []
with open('Data/Dataset.csv', 'r') as DataFile:
    train_data = list(csv.reader(DataFile))
    available_symptoms = list(
        map(lambda v: v.strip().lower(), train_data[0]))[2:-1]
    train_data = train_data[1:]
    print("Er worden " + str(len(train_data) - 1) +
          " rijen gebruikt om de applicatie te trainen.")

    with open('Testdata.csv', 'r') as TestDataFile:
        test_data = list(csv.reader(TestDataFile))[1:]
        print("Er worden " + str(len(test_data) - 1) +
          " rijen gebruikt om de applicatie te testen.")

# datasets
test_features = []
test_labels = []

features = []
labels = []

ziektes = ['Astma', 'Bronchitis', 'Griep', 'Longontsteking', 'Verkoudheid']

# split labels from features
for item in test_data:
    item = list(map(lambda v: int(v), item))
    test_labels.append(item[-1])
    test_features.append(item[:-1].copy())

for item in train_data:
    item = list(map(lambda v: int(v), item))
    labels.append(item[-1])
    features.append(item[:-1].copy())

# create a decision tree classifier
clf = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=100000)
# train the classifier with the trainingsdata
clf = clf.fit(features, labels)

# Verkrijg de accuraatheid
y_pred = clf.predict(test_features)
print("Accuraatheid is: " + str(metrics.accuracy_score(test_labels, y_pred)))

print("\nDeze applicatie kan bekijken of je de volgende ziektes hebt:")
print(", ".join(ziektes))

print("\nOm de ziekte te bepalen worden er een aantal vragen gesteld.")

while True:
    print("\nWat is jouw geslacht? (0 voor VROUW, 1 voor MAN)")
    geslacht = int(input(""))

    print("\nWat is jouw leeftijd?")
    leeftijd = int(input(""))

    symptoms = None
    while symptoms is None:
        print("\nDe beschikbare symptomen zijn:")
        print(", ".join(available_symptoms))
        print("\nVul je symptomen in, gescheiden door een comma:")
        symptoms = list(map(lambda v: v.strip().lower(), input("").split(",")))

        existing_symptoms = list(
            filter(lambda v: v in available_symptoms, symptoms))

        if len(existing_symptoms) != len(symptoms):
            print("\nU mag alleen symptomen opnoemen die bij ons geregistreerd zijn. De symptomen die u invulde maar niet bij ons geregistreerd staan zijn:")
            not_existing_symptoms = list(
                set(symptoms) - set(existing_symptoms))
            print (", ".join(not_existing_symptoms))

            symptoms = None

    symptoms_array = [geslacht, leeftijd]
    for available_symptom in available_symptoms:
        symptoms_array.append(1 if available_symptom in symptoms else 0)

    prediction = int(clf.predict([symptoms_array])[0])

    print("\n\n👉 De applicatie geeft aan dat u de volgende ziekte heeft:")
    print(ziektes[prediction])
    print("\nUw ziekte is bepaald. Druk op 'j' om de applicatie te herstarten.")
    again = input("")
    if again.upper() != "J":
        break

print("\nU heeft aangegeven dat u geen behoefte meer heeft om de applicatie te herstarten. Fijne dag.")
```

&copy;2018 - NotS project machine learning 2018