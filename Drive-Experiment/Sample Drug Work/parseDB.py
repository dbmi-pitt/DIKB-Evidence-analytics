##### SAM ROSKO'S PYTHON FILE TO PARSE DRUGBANK'S XML
##### LAST UPDATED: 6/12/2015
##### TO DO: Figure out what else I want to pull

import xml.etree.ElementTree as ET
import sys

sys.path = sys.path + ['.']

f = open('drug_bank_out.txt', 'w')

tree = ET.parse('drugbank.xml')
root = tree.getroot()

NS = {'db': 'http://www.drugbank.ca'} 

drug_list = ['Haloperidol', 'Risperidone', 'Quetiapine', 'Duloxetine', 'Paroxetine', 'Bupropion', 'Citalopram', 'Triazolam', 'Alprazolam', 'Simvastatin', 'Pravastatin']

##### Retrieving Substiuents/Targets ######
for chem in root.findall('db:drug', NS):
    for my_drug in drug_list:
        if (chem.find('db:name', NS).text == my_drug):
                sub_list = []
                f.write(chem.find('db:name', NS).text + '\n')
                class_list = chem.find('db:classification', NS)
                for sub in class_list.findall('db:substituent', NS):
                        sub_list.append(sub.text)           
                sub_list.sort()
                f.write('\nSubstituents:\n')
                for sub in sub_list:
                        f.write(sub + '\n')
                f.write('\nTargets:\n')
                target_list = chem.find('db:targets', NS)
                for target in target_list.findall('db:target', NS):
                        f.write(target.find('db:name', NS).text + '\n')
                f.write('\nAction on Target:\n')
                for target in target_list.findall('db:target', NS):                        
                        for action in target.findall('db:actions', NS):
                                f.write(action.find('db:action', NS).text+'\n')                
                f.write('\n')
                
##### Retrieving ATC-CODES(WIP) ######
for chem in root.findall('db:drug', NS):
    for my_drug in drug_list:
        if (chem.find('db:name', NS).text == my_drug):
                print chem.find('db:name', NS).text
                code_list = chem.find('db:atc-codes', NS)
                code = code_list.find('db:atc-code', NS)
                print code.attrib
                for level in code.findall('db:level', NS):
                        print level.attrib
                        print level.text
                print '\n'
                
##### END OF FILE ######
f.close()
