# Decision tree (ziekten)

## Vereisten
> Leg uit wat de vereisten zijn om de code te kunnen draaien

Het prototype is gebouwd en getest op 64-bits Windows- en 64-bits Linux-systemen om de werking van de code te verifiëren.

Voor deze demo dienen een aantal zaken geïnstalleerd te zijn op de omgeving waarin deze demo wordt uitgevoerd.

- Python versie 3.6   (https://www.python.org/downloads/release/python-364/)
- Pip versie 10.0     (https://pip.pypa.io/en/stable/installing/)

## Installatie
> Leg uit hoe je de code kan draaien

Om de programmacode te draaien heb je de volgende Python-modulen nodig:

- csv (voor het lezen van de dataset)
- sklearn (voor het aanleveren van functies om machine learning mogelijk te maken in Python)
- random (voor het shufflen van de dataset voordat je scheidt naar training- en testset)

Door het commando `pip install -r requirements.txt --user` uit te voeren in een opdrachtvenster worden alle modules in één keer gedownload.

## Data
De dataset is zelfbedacht en de gegevens zijn geen echte gegevens, maar er wordt geprobeerd zo realistisch mogelijk de symptomen te linken met de ziekten. De dataset kan onderscheid maken tussen hooikoorts, longontsteking en het hebben van geen ziekte. Dit wordt voor de gebruiker gedaan door de symptomen die hij of zij invult gecorrespondeert worden met de ja/nee-waarden van de symptomen in de dataset.

## Demo code
```python
import csv
from random import shuffle
from sklearn import tree

# read csv files
available_symptoms = []
with open('longontsteking_data.csv', 'r') as DataFile:
    csv_file = list(csv.reader(DataFile))
    available_symptoms = list(
        map(lambda v: v.strip().lower(), csv_file[0]))[2:-1]
    csvList = csv_file[1:]
    shuffle(csvList)
    trainDataCount = round(len(csvList) * 7 / 10) + 1
    print("Er worden " + str(trainDataCount) +
          " rijen gebruikt om de applicatie te trainen.")
    print("Er worden " + str(len(csvList) - trainDataCount) +
          " rijen gebruikt om de applicatie te testen.")
    trainData = csvList[0:trainDataCount].copy()
    testData = csvList[trainDataCount:].copy()

# datasets
test_features = []
test_labels = []

features = []
labels = []

# split labels from features
for item in testData:
    test_labels.append(item[-1])
    test_features.append(item[:-1].copy())

for item in trainData:
    labels.append(item[-1])
    features.append(item[:-1].copy())

# create a decision tree classifier
DT_clf = tree.DecisionTreeClassifier()
# train the classifier with the trainingsdata
DT_clf = DT_clf.fit(features, labels)

print("\nDeze applicatie kan bekijken of je longontsteking, hooikoorts of geen ziekte hebt. Hiervoor worden er een aantal vragen gesteld.")

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

    prediction = int(DT_clf.predict([symptoms_array])[0])

    print("\n\n👉 De applicatie geeft aan dat u de volgende ziekte heeft:")
    if prediction == 1:
        print("Longontsteking")
    elif prediction == 2:
        print("Hooikoorts")
    else:
        print("Helemaal niets")

    print("\nUw ziekte is bepaald. Druk op 'j' om de applicatie te herstarten.")
    again = input("")
    if again.upper() != "J":
        break

print("\nU heeft aangegeven dat u geen behoefte meer heeft om de applicatie te herstarten. Fijne dag.")
```

## Resultaat van de applicatie
![Illustratie van het plot](longontsteking.png)

De code geeft je een vragenlijst die je kunt beantwoorden met `0` (nee) of `1` (ja). De vragen zijn wat je geslacht is, je leeftijd, en welke symptomen je ondervindt. Gebaseerd daarop vertelt de applicatie of je een hooikoorts, longontsteking of geen ziekte hebt.