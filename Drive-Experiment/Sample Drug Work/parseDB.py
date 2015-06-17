##### SAM ROSKO'S PYTHON FILE TO PARSE DRUGBANK'S XML
##### LAST UPDATED: 6/15/2015
##### TO DO: I believe I'm done with DrugBank. Look at other sources.

import xml.etree.ElementTree as ET
import sys

sys.path = sys.path + ['.']

f = open('drug_bank_out.txt', 'w')

tree = ET.parse('drugbank.xml')
root = tree.getroot()

NS = {'db': 'http://www.drugbank.ca'} 

drug_list = ['Haloperidol', 'Risperidone', 'Quetiapine', 'Duloxetine', 'Paroxetine', 'Bupropion', 'Citalopram', 'Triazolam', 'Alprazolam', 'Simvastatin', 'Pravastatin']

##### Retrieval Starts ######
for chem in root.findall('db:drug', NS):
    for my_drug in drug_list:
        if (chem.find('db:name', NS).text == my_drug):
                sub_list = []
                f.write(chem.find('db:name', NS).text + '\n') ### writes drug name to the file
                
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

                f.write('\nMolecular Weight:\n')
                prop_list = chem.find('db:calculated-properties', NS)
                for prop in prop_list.findall('db:property', NS):
                    if (prop.find('db:kind', NS).text == 'Molecular Weight'):
                        f.write(prop.find('db:value', NS).text+'\n')

                f.write('\nATC Code:\n')
                code_list = chem.find('db:atc-codes', NS)
                code = code_list.find('db:atc-code', NS)
                f.write(code.get('code')+'\n')
                for level in code.findall('db:level', NS):
                        f.write(level.get('code') + " - " + level.text + "\n")
                                
                f.write('\nAHFS Code:\n')
                ahfs_list = chem.find('db:ahfs-codes', NS)
                for ahfs in ahfs_list.findall('db:ahfs-code', NS):
                        f.write(ahfs.text+'\n')

                f.write('\nInChI Key:\n')
                prop_list = chem.find('db:calculated-properties', NS)
                for prop in prop_list.findall('db:property', NS):
                    if (prop.find('db:kind', NS).text == 'InChIKey'):
                        f.write(prop.find('db:value', NS).text+'\n')
                        
                f.write('\n')
                
##### Retrieval Ends ######
print 'Done! No Errors'
                
##### END OF FILE ######
f.close()
