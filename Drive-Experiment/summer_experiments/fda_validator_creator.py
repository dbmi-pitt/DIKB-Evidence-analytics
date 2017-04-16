import os
import sys
import csv

main_dikb_drugs = ['alprazolam', 'aripiprazole', 'asenapine', 'atorvastatin', 'bupropion', 'chlorpromazine', 'citalopram', 'clozapine', 'desipramine', 'desvenlafaxine', 'diltiazem', 'duloxetine', 'escitalopram', 'eszopiclone', 'fluconazole', 'fluoxetine', 'fluphenazine', 'fluvastatin', 'fluvoxamine', 'haloperidol', 'itraconazole', 'ketoconazole', 'iloperidone', 'lovastatin', 'lurasidone', 'midazolam', 'mirtazapine', 'nefazodone', 'olanzapine', 'paliperidone', 'paroxetine', 'perphenazine', 'pimozide', 'pravastatin', 'quetiapine', 'risperidone', 'rosuvastatin', 'sertraline', 'simvastatin', 'thioridazine', 'thiothixene', 'trazodone', 'triazolam', 'venlafaxine', 'zaleplon', 'ziprasidone', 'zolpidem']

all_dikb_drugs = ["acyclovir", "aliskiren", "allopurinol", "alosetron", "alprazolam", "ambrisentan", "amiodarone", "amprenavir", "aprepitant", "aripiprazole", "armodafinil", "asenapine", "atazanavir", "atomoxetine", "atorvastatin", "atrasentan", "azithromycin", "basiliximab", "bicalutamide", "boceprevir", "bupropion", "caffeine", "capecitabine", "celecoxib", "chloramphenicol", "chloroquine", "chlorpheniramine", "chlorpromazine", "chlorzoxazone", "cimetidine", "cinacalcet", "ciprofloxacin", "citalopram", "clarithromycin", "clobazam", "clomipramine", "clopidogrel", "clotrimazole", "clozapine", "colchicine", "conivaptan", "cotrimoxazole", "crizotinib", "cyclosporine", "dabigatran", "dabigatran-etexilate", "danazol", "darifenacin", "darunavir", "dasatinib", "debrisoquine", "delavirdine", "desipramine", "desloratadine", "desvenlafaxine", "dextromethorphan", "diethyldithiocarbamate", "digoxin", "dihydroergotamine", "diltiazem", "diphenhydramine", "disulfiram", "doxorubicin", "dronedarone", "droperidol", "duloxetine", "efavirenz", "elacridar", "eltrombopag", "erythromycin", "escitalopram", "esomeprazole", "eszopiclone", "ethanol", "etravirine", "everolimus", "ezetimibe", "famotidine", "febuxostat", "felbamate", "fexofenadine", "flecainide", "fluconazole", "fluorouracil", "fluoxetine", "fluphenazine", "fluticasone", "fluvastatin", "fluvoxamine", "fosamprenavir", "gemfibrozil", "haloperidol", "hydralazine", "hydroxychloroquine", "ibuprofen", "iloperidone", "imatinib", "indinavir", "indomethacin", "irinotecan", "isoniazid", "itraconazole", "ketoconazole", "lansoprazole", "lapatinib", "leflunomide", "lithium", "lovastatin", "lurasidone", "maraviroc", "melatonin", "mephenytoin", "methadone", "methoxsalen", "metronidazole", "mexiletine", "miconazole", "midazolam", "midodrine", "mifepristone", "mirtazapine", "modafinil", "molindone", "montelukast", "nebivolol", "nefazodone", "nelfinavir", "nicardipine", "nilotinib", "norfloxacin", "olanzapine", "omeprazole", "oxandrolone", "oxcarbazepine", "oxycarbazepine", "paclitaxel", "paliperidone", "pantoprazole", "paroxetine", "pazopanib", "perphenazine", "phenacetin", "phencyclidine", "phenylpropanolamine", "phenytoin", "pilocarpine", "pimozide", "pioglitazone", "pitavastatin", "posaconazole", "prasugrel", "pravastatin", "promethazine", "propafenone", "propoxyphene", "quercetin", "quetiapine", "quinidine", "quinine", "quinupristin", "R-citalopram", "R-warfarin", "rabeprazole", "ramelteon", "ranitidine", "ranolazine", "reserpine", "rifampin", "risperidone", "ritonavir", "rosiglitazone", "rosuvastatin", "S-warfarin", "saquinavir", "saxagliptin", "sertraline", "sildenafil", "simvastatin", "sirolimus", "sitagliptin", "sulfamethizole", "sulfamethoxazole", "sulfinpyrazone", "sulphaphenazole", "tacrine", "tacrolimus", "talinolol", "tamoxifen", "telaprevir", "telithromycin", "teniposide", "terbinafine", "testosterone", "theophylline", "thiabendazole", "thioridazine", "thiotepa", "thiothixene", "ticagrelor", "ticlopidine", "tigecycline", "tipranavir", "tizanidine", "tolbutamide", "tolvaptan", "topiramate", "topotecan", "tranylcypromine", "trazodone", "triazolam", "trifluoperazine", "trimethoprim", "troleandomycin", "valproate", "valspodar", "vemurafenib", "venlafaxine", "verapamil", "voriconazole", "warfarin", "zafirlukast", "zaleplon", "zileuton", "ziprasidone", "zolpidem", "zosuquidar"]

with open('fda_oi_di_db_pairs.csv', 'rb') as f:
    reader = csv.reader(f)
    input_list = list(reader)

output_list = []

for pair in input_list:
  if(pair[0] in all_dikb_drugs) and (pair[1] in all_dikb_drugs):
    if (pair[0] in main_dikb_drugs) or (pair[1] in main_dikb_drugs):
        output_list.append((pair[0] + ' - ' + pair[1]))

with open('fda_oi_di_db_pairs_cleaned.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(output_list)
