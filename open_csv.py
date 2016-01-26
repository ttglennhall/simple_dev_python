import csv

with open('data/lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv','rU') as inputFile:
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        #line = line.rstrip().split(',')
        print(line)