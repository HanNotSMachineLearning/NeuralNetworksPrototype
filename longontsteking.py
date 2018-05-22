import csv
from random import shuffle
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# read csv files
available_symptoms = []
with open('trainingsdata.csv', 'r') as DataFile:
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

ziektes = ['Astma', 'Bronchitis', 'Griep', 'Longontsteking', 'Verkoudheid']

# split labels from features
for item in testData:
    item = list(map(lambda v: int(v), item))
    test_labels.append(item[-1])
    test_features.append(item[:-1].copy())

for item in trainData:
    item = list(map(lambda v: int(v), item))
    labels.append(item[-1])
    features.append(item[:-1].copy())

# create a decision tree classifier
# clf = tree.DecisionTreeClassifier()
clf = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=100000)
# train the classifier with the trainingsdata
clf = clf.fit(features, labels)

# Verkrijg de accuraatheid
y_pred = clf.predict(test_features)
print("Accuraatheid is: " + str(metrics.accuracy_score(test_labels, y_pred)))

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

    prediction = int(clf.predict([symptoms_array])[0])

    print("\n\n👉 De applicatie geeft aan dat u de volgende ziekte heeft:")
    print(ziektes[prediction])
    print("\nUw ziekte is bepaald. Druk op 'j' om de applicatie te herstarten.")
    again = input("")
    if again.upper() != "J":
        break

print("\nU heeft aangegeven dat u geen behoefte meer heeft om de applicatie te herstarten. Fijne dag.")
