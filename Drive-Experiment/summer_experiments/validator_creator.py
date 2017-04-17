import os
import sys

main_dikb_drugs = ['alprazolam', 'aripiprazole', 'asenapine', 'atorvastatin', 'bupropion', 'chlorpromazine', 'citalopram', 'clozapine', 'desipramine', 'desvenlafaxine', 'diltiazem', 'duloxetine', 'escitalopram', 'eszopiclone', 'fluconazole', 'fluoxetine', 'fluphenazine', 'fluvastatin', 'fluvoxamine', 'haloperidol', 'itraconazole', 'ketoconazole', 'iloperidone', 'lovastatin', 'lurasidone', 'midazolam', 'mirtazapine', 'nefazodone', 'olanzapine', 'paliperidone', 'paroxetine', 'perphenazine', 'pimozide', 'pravastatin', 'quetiapine', 'risperidone', 'rosuvastatin', 'sertraline', 'simvastatin', 'thioridazine', 'thiothixene', 'trazodone', 'triazolam', 'venlafaxine', 'zaleplon', 'ziprasidone', 'zolpidem']

all_dikb_drugs = ["acyclovir", "aliskiren", "allopurinol", "alosetron", "alprazolam", "ambrisentan", "amiodarone", "amprenavir", "aprepitant", "aripiprazole", "armodafinil", "asenapine", "atazanavir", "atomoxetine", "atorvastatin", "atrasentan", "azithromycin", "basiliximab", "bicalutamide", "boceprevir", "bupropion", "caffeine", "capecitabine", "celecoxib", "chloramphenicol", "chloroquine", "chlorpheniramine", "chlorpromazine", "chlorzoxazone", "cimetidine", "cinacalcet", "ciprofloxacin", "citalopram", "clarithromycin", "clobazam", "clomipramine", "clopidogrel", "clotrimazole", "clozapine", "colchicine", "conivaptan", "cotrimoxazole", "crizotinib", "cyclosporine", "dabigatran", "dabigatran-etexilate", "danazol", "darifenacin", "darunavir", "dasatinib", "debrisoquine", "delavirdine", "desipramine", "desloratadine", "desvenlafaxine", "dextromethorphan", "diethyldithiocarbamate", "digoxin", "dihydroergotamine", "diltiazem", "diphenhydramine", "disulfiram", "doxorubicin", "dronedarone", "droperidol", "duloxetine", "efavirenz", "elacridar", "eltrombopag", "erythromycin", "escitalopram", "esomeprazole", "eszopiclone", "ethanol", "etravirine", "everolimus", "ezetimibe", "famotidine", "febuxostat", "felbamate", "fexofenadine", "flecainide", "fluconazole", "fluorouracil", "fluoxetine", "fluphenazine", "fluticasone", "fluvastatin", "fluvoxamine", "fosamprenavir", "gemfibrozil", "haloperidol", "hydralazine", "hydroxychloroquine", "ibuprofen", "iloperidone", "imatinib", "indinavir", "indomethacin", "irinotecan", "isoniazid", "itraconazole", "ketoconazole", "lansoprazole", "lapatinib", "leflunomide", "lithium", "lovastatin", "lurasidone", "maraviroc", "melatonin", "mephenytoin", "methadone", "methoxsalen", "metronidazole", "mexiletine", "miconazole", "midazolam", "midodrine", "mifepristone", "mirtazapine", "modafinil", "molindone", "montelukast", "nebivolol", "nefazodone", "nelfinavir", "nicardipine", "nilotinib", "norfloxacin", "olanzapine", "omeprazole", "oxandrolone", "oxcarbazepine", "oxycarbazepine", "paclitaxel", "paliperidone", "pantoprazole", "paroxetine", "pazopanib", "perphenazine", "phenacetin", "phencyclidine", "phenylpropanolamine", "phenytoin", "pilocarpine", "pimozide", "pioglitazone", "pitavastatin", "posaconazole", "prasugrel", "pravastatin", "promethazine", "propafenone", "propoxyphene", "quercetin", "quetiapine", "quinidine", "quinine", "quinupristin", "R-citalopram", "R-warfarin", "rabeprazole", "ramelteon", "ranitidine", "ranolazine", "reserpine", "rifampin", "risperidone", "ritonavir", "rosiglitazone", "rosuvastatin", "S-warfarin", "saquinavir", "saxagliptin", "sertraline", "sildenafil", "simvastatin", "sirolimus", "sitagliptin", "sulfamethizole", "sulfamethoxazole", "sulfinpyrazone", "sulphaphenazole", "tacrine", "tacrolimus", "talinolol", "tamoxifen", "telaprevir", "telithromycin", "teniposide", "terbinafine", "testosterone", "theophylline", "thiabendazole", "thioridazine", "thiotepa", "thiothixene", "ticagrelor", "ticlopidine", "tigecycline", "tipranavir", "tizanidine", "tolbutamide", "tolvaptan", "topiramate", "topotecan", "tranylcypromine", "trazodone", "triazolam", "trifluoperazine", "trimethoprim", "troleandomycin", "valproate", "valspodar", "vemurafenib", "venlafaxine", "verapamil", "voriconazole", "warfarin", "zafirlukast", "zaleplon", "zileuton", "ziprasidone", "zolpidem", "zosuquidar"]

done_drugs = []

ddi_obs = ["alprazolam - erythromycin", "alprazolam - fluoxetine", "alprazolam - itraconazole", "alprazolam - ketoconazole", "alprazolam - nefazodone", "aripiprazole - escitalopram", "aripiprazole - venlafaxine", "atorvastatin - clarithromycin", "atorvastatin - erythromycin", "atorvastatin - itraconazole", "bupropion - clopidogrel", "bupropion - desipramine", "bupropion - prasugrel", "bupropion - ticlopidine", "citalopram - cimetidine", "citalopram - desipramine", "clozapine - fluvoxamine", "desipramine - desvenlafaxine", "desipramine - fluoxetine", "desipramine - paroxetine", "desipramine - sertraline", "desipramine - venlafaxine", "desvenlafaxine - ketoconazole", "diltiazem - midazolam", "diltiazem - simvastatin", "diltiazem - triazolam", "duloxetine - fluvoxamine", "duloxetine - paroxetine", "duloxetine - theophylline", "escitalopram - cimetidine", "fluconazole - fluvastatin", "fluconazole - midazolam", "fluconazole - triazolam", "fluoxetine - olanzapine", "fluoxetine - propafenone", "fluvoxamine - lansoprazole", "fluvoxamine - mexiletine", "fluvoxamine - omeprazole", "fluvoxamine - quinidine", "fluvoxamine - theophylline", "fluvoxamine - thioridazine", "fluvoxamine - tolbutamide", "haloperidol - venlafaxine", "itraconazole - lovastatin", "itraconazole - midazolam", "itraconazole - pravastatin", "itraconazole - rosuvastatin", "itraconazole - triazolam", "itraconazole - zolpidem", "ketoconazole - midazolam", "ketoconazole - simvastatin", "ketoconazole - triazolam", "ketoconazole - venlafaxine", "ketoconazole - zolpidem", "midazolam - clarithromycin", "midazolam - erythromycin", "midazolam - nefazodone", "mirtazapine - cimetidine", "mirtazapine - paroxetine", "nefazodone - triazolam", "paliperidone - paroxetine", "paroxetine - cimetidine", "paroxetine - risperidone", "paroxetine - terbinafine", "pravastatin - clarithromycin", "quetiapine - cimetidine", "quetiapine - erythromycin", "risperidone - venlafaxine", "risperidone - verapamil", "sertraline - cimetidine", "simvastatin - erythromycin", "trazodone - clarithromycin", "trazodone - ritonavir", "triazolam - clarithromycin", "triazolam - erythromycin", "venlafaxine - cimetidine", "venlafaxine - diphenhydramine", "venlafaxine - terbinafine", "ziprasidone - cimetidine"] 

ddi_fda = ["fluconazole - etravirine", "fluconazole - omeprazole", "fluoxetine - nebivolol", "fluoxetine - risperidone", "fluvoxamine - caffeine", "fluvoxamine - rabeprazole", "fluvoxamine - tizanidine", "itraconazole - aliskiren", "itraconazole - telithromycin", "ketoconazole - cinacalcet", "ketoconazole - clobazam", "ketoconazole - everolimus", "ketoconazole - fluticasone", "ketoconazole - imatinib", "ketoconazole - lapatinib", "ketoconazole - nilotinib", "ketoconazole - pazopanib", "ketoconazole - ranolazine", "ketoconazole - tolvaptan", "ketoconazole - ziprasidone", "paroxetine - atomoxetine"]

ddi_update = ["atorvastatin - aliskiren", "atorvastatin - gemfibrozil", "atorvastatin - telaprevir", "atorvastatin - ticagrelor", "diltiazem - ranolazine", "ketoconazole - risperidone", "pravastatin - rifampin", "rosuvastatin - cyclosporine", "rosuvastatin - eltrombopag", "rosuvastatin - gemfibrozil", "simvastatin - gemfibrozil", "simvastatin - ranolazine"]

ddi_case = ["clozapine - cimetidine", "clozapine - ciprofloxacin", "clozapine - isoniazid", "clozapine - phenytoin", "duloxetine - olanzapine", "quetiapine - clarithromycin", "quetiapine - valproate", "simvastatin - amiodarone", "simvastatin - ciprofloxacin", "simvastatin - clarithromycin", "simvastatin - nelfinavir"]

nonddi_obs = ["alprazolam - citalopram", "alprazolam - sertraline", "alprazolam - venlafaxine", "aripiprazole - valproate", "bupropion - ritonavir", "bupropion - valproate", "citalopram - ketoconazole", "clozapine - sertraline", "desipramine - atomoxetine", "desipramine - ketoconazole", "desipramine - nefazodone", "diltiazem - pravastatin", "fluconazole - pravastatin", "fluconazole - rosuvastatin", "fluconazole - zolpidem", "fluoxetine - alosetron", "fluoxetine - desloratadine", "fluvastatin - erythromycin", "fluvastatin - itraconazole", "haloperidol - quetiapine", "nefazodone - cimetidine", "nefazodone - pravastatin", "quetiapine - risperidone", "risperidone - erythromycin", "rosuvastatin - erythromycin", "sertraline - zolpidem", "venlafaxine - indinavir"]

nonddi_update = ["asenapine - valproate", "atorvastatin - dabigatran", "duloxetine - warfarin", "ketoconazole - rosuvastatin", "pravastatin - nelfinavir", "rosuvastatin - warfarin", "sertraline - phenytoin", "simvastatin - sitagliptin"]

fileout = "./scr25-validation-set.tsv"
f = open(fileout,'w')
f.write("Pceut entity combination"+"\t"+"VALIDATION_SET_DDI"+"\t"+"VALIDATION_SET_NON_DDI"+"\t"+"DDI_DIKB"+"\t"+"NON_DDI_DIKB"+"\t"+"True_pos"+"\t"+"False_pos"+"\t"+"True_neg"+"\t"+"False_neg"+"\n")

fileout2 = "./scr25-combination-list.txt"
f2 = open(fileout2,'w')

for drug1 in main_dikb_drugs:
    for drug2 in all_dikb_drugs:
        if (drug1 == drug2):
            continue
        elif(drug2 in done_drugs):
            continue
        else:
            interaction = (drug1+' - '+drug2)
            f.write('"'+interaction+'"'+'\t')
            f2.write('"'+interaction+'"'+':None, ')
            if(interaction in ddi_obs):
                f.write("TRUE")
            elif(interaction in ddi_update):
                f.write("TRUE")
            elif(interaction in ddi_case):
                f.write("TRUE")
	    elif(interaction in ddi_fda):
                f.write("TRUE")	      
            elif(interaction in nonddi_obs):
                f.write("\tTRUE")
            elif(interaction in nonddi_update):
                f.write("\tTRUE")
            f.write('\n')
    done_drugs.append(drug1)
        
f.close()
