from collections import defaultdict

population_dict_2010 = defaultdict(int)
population_dict_2100 = defaultdict(int)
population_dict_difference = defaultdict(int)

with open('data/lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
	header = next(inputFile)
	
	for line in inputFile:
		line = line.rstrip().split(',')
		line[5] = int(line[5])
		line[6] = int(line[6])
		if line[1] == 'Total National Population':
			population_dict_2010[line[0]] += line[5]
			population_dict_2100[line[0]] +=line[6]
	print(population_dict_2010)
	print(population_dict_2100)

population_dict_difference = {key: population_dict_2100[key] - population_dict_2010.get(key, 0) for key in population_dict_2100.keys()}

with open('national_population.csv','w') as outputFile:
	outputFile.write('continent,population_difference\n')

	for k, v in population_dict_difference.iteritems():
		outputFile.write(k + ',' + str(v) + '\n')

