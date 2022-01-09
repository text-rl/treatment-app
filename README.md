# treatment-app
Text treatment application which use trained IA models


# dependencies : 
* pyhumps
* pika

# datasets :
Blacklist :
- "first_names.all.csv" in "core/Blacklist/data/person/" https://github.com/philipperemy/name-dataset/raw/c0fee3a853d67cab7464f5bfe7dae7b355136131/names_dataset/v2/first_names.zip
- "last_names.all.csv" in "core/Blacklist/data/person/" https://github.com/philipperemy/name-dataset/raw/c0fee3a853d67cab7464f5bfe7dae7b355136131/names_dataset/v2/last_names.zip
- "allCountries.txt" in "core/Blacklist/data/location/" - "allCountries.txt" in "core/Blacklist/data/location/" http://download.geonames.org/export/dump/allCountries.zip

Testing :
- "ner_datasetreference.csv" in "data/" https://www.kaggle.com/namanj27/ner-dataset/download 
