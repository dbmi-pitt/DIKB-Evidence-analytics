##### SAM ROSKO'S PYTHON FILE TO PARSE BIO2RDF CUIs
##### LAST UPDATED: 6/10/2015
##### TO DO: None

import sys
sys.path = sys.path + ['.']

f = open('cuiFile.txt', 'w')

def cutCUI( i_file ) :
    HOIs = open( i_file ).readlines()
    for HOI in HOIs :
        indexCUI = HOI.index(' [')
        f.write(HOI[1:indexCUI]+'\n') 

cutCUI('drugFile.txt')

f.close()

















        
