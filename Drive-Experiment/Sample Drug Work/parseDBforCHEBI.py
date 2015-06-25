##### SAM ROSKO'S PYTHON FILE TO PARSE DRUGBANK'S XML FOR CHEBI CODES
##### LAST UPDATED: 6/24/2015
##### TO DO: Done

import xml.etree.ElementTree as ET
import sys

sys.path = sys.path + ['.']

f = open('chebi_mapping.txt', 'w')

tree = ET.parse('drugbank.xml')
root = tree.getroot()

NS = {'db': 'http://www.drugbank.ca'}

##### Retrieval Starts ######
for chem in root.findall('db:drug', NS):
    id_list = chem.find('db:external-identifiers', NS)       
    for ids in id_list.findall('db:external-identifier', NS):
        if(ids.find('db:resource', NS).text == 'ChEBI'):
            f.write("http://purl.obolibrary.org/obo/CHEBI_"+ids.find('db:identifier', NS).text + '\t')
            f.write(chem.find('db:name', NS).text)
            f.write('\n')
                
##### Retrieval Ends ######
print 'Done! No Errors'
                
##### END OF FILE ######
f.close()
