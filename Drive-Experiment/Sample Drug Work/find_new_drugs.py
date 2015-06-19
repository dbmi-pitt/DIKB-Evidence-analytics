### SAM ROSKO'S FILE FOR FINDING WHAT NEW OBJECTS NEED TO BE ENTERED TO USE WITH FDA2012 GUIDELINES
### LAST UPDATED: 6/18/2015
### TO DO: Done, figure out where to put results!

import sys
sys.path = sys.path + ['.']

f = open('drug_results.txt', 'w')

def cutQuotes( i_file ) :
    drugs = open( i_file ).readlines()
    for drug in drugs:
        if((drug[1:(len(drug)-2)] not in results)):
            results.append(drug[1:(len(drug)-2)])

def compareDrugs( i_file ) :
    drugs = open( i_file ).readlines()
    for drug in drugs:
        if(drug[:len(drug)-1] in final_results):
            final_results.remove(drug[:len(drug)-1])
                        
results = []

cutQuotes('fda_2012_drugs.txt')

final_results = results[:]

compareDrugs('dikb_drugs.txt')
    
final_results.sort()

print "Initial/Final", len(results), len(final_results)

for x in final_results:
    f.write(x + '\n')
    
f.close()
