import os
import sys

main_drugs = ["alprazolam",	"aripiprazole",	"asenapine", "atorvastatin",	"bupropion",	"chlorpromazine",	"citalopram",	"clozapine",	"desipramine",	"desvenlafaxine",	"duloxetine",	"escitalopram",	"eszopiclone",	"fluoxetine",	"fluphenazine",	"fluvastatin",	"fluvoxamine",	"haloperidol",	"iloperidone",	"lovastatin",	"lurasidone",	"midazolam",	"mirtazapine",	"nefazodone",	"olanzapine",	"paliperidone",	"paroxetine",	"perphenazine",	"pimozide",	"pitavastatin",	"pravastatin",	"quetiapine",	"risperidone",	"rosuvastatin",	"sertraline",	"simvastatin",	"thioridazine",	"thiothixene",	"trazodone",	"triazolam",	"venlafaxine",	"zaleplon",	"ziprasidone",	"zolpidem"]

all_drugs = ["acyclovir",	"aliskiren",	"allopurinol",	"alosetron",	"alprazolam",	"ambrisentan",	"amiodarone",	"amprenavir",	"aprepitant",	"aripiprazole",	"armodafinil",	"asenapine",	"atazanavir",	"atomoxetine",	"atorvastatin",	"atrasentan",	"azithromycin",	"bicalutamide",	"boceprevir",	"bupropion",	"caffeine",	"capecitabine",	"celecoxib",	"chlorpromazine",	"cimetidine",	"cinacalcet",	"ciprofloxacin",	"citalopram",	"clarithromycin",	"clobazam",	"clopidogrel",	"clozapine",	"colchicine",	"conivaptan",	"cotrimoxazole",	"crizotinib",	"cyclosporine",	"dabigatran",	"dabigatran-etexilate",	"darifenacin",	"dasatinib",	"desipramine",	"desloratadine",	"desvenlafaxine",	"dextromethorphan",	"dihydroergotamine",	"diltiazem",	"diphenhydramine",	"disulfiram",	"dronedarone",	"duloxetine",	"efavirenz",	"eltrombopag",	"erythromycin",	"escitalopram",	"esomeprazole",	"eszopiclone",	"etravirine",	"everolimus",	"ezetimibe",	"famotidine",	"febuxostat",	"felbamate",	"fexofenadine",	"fluconazole",	"fluoxetine",	"fluphenazine",	"fluticasone",	"fluvastatin",	"fluvoxamine",	"fosamprenavir",	"gemfibrozil",	"haloperidol",	"hydralazine",	"hydroxychloroquine",	"iloperidone",	"imatinib",	"indinavir",	"indomethacin",	"irinotecan",	"isoniazid",	"itraconazole",	"ketoconazole",	"lansoprazole",	"lapatinib",	"leflunomide",	"lithium",	"lovastatin",	"lurasidone",	"maraviroc",	"melatonin",	"methadone",	"methoxsalen",	"metronidazole",	"mexiletine",	"miconazole",	"midazolam",	"midodrine",	"mirtazapine",	"modafinil",	"molindone",	"montelukast",	"nebivolol",	"nefazodone",	"nelfinavir",	"nicardipine",	"nilotinib",	"norfloxacin",	"olanzapine",	"omeprazole",	"oxandrolone",	"paclitaxel",	"paliperidone",	"pantoprazole",	"paroxetine",	"pazopanib",	"perphenazine",	"phenylpropanolamine",	"phenytoin",	"pimozide",	"pitavastatin",	"posaconazole",	"prasugrel",	"pravastatin",	"promethazine",	"propafenone",	"propoxyphene",	"quetiapine",	"quinidine",	"R-citalopram",	"rabeprazole",	"ramelteon",	"ranitidine",	"ranolazine",	"rifampin",	"risperidone",	"ritonavir",	"rosiglitazone",	"rosuvastatin",	"saxagliptin",	"sertraline",	"sildenafil",	"simvastatin",	"sirolimus",	"sitagliptin",	"sulfinpyrazone",	"tacrine",	"tacrolimus",	"talinolol",	"tamoxifen",	"telaprevir",	"telithromycin",	"terbinafine",	"theophylline",	"thioridazine",	"thiothixene",	"ticagrelor",	"ticlopidine",	"tigecycline",	"tizanidine",	"tolbutamide",	"tolvaptan",	"topiramate",	"topotecan",	"trazodone",	"triazolam",	"trimethoprim",	"valproate",	"vemurafenib",	"venlafaxine",	"verapamil",	"voriconazole",	"warfarin",	"zafirlukast",	"zaleplon",	"zileuton",	"ziprasidone",	"zolpidem"]

done_drugs = []

ddi_obs = ["alprazolam - erythromycin",	"alprazolam - fluoxetine",	"alprazolam - itraconazole",	"alprazolam - ketoconazole",	"alprazolam - nefazodone",	"aripiprazole - escitalopram",	"aripiprazole - venlafaxine",	"atorvastatin - clarithromycin",	"atorvastatin - erythromycin",	"atorvastatin - itraconazole",	"bupropion - clopidogrel",	"bupropion - desipramine",	"bupropion - prasugrel",	"bupropion - ticlopidine",	"citalopram - cimetidine",	"citalopram - desipramine",	"clozapine - fluvoxamine",	"desipramine - desvenlafaxine",	"desipramine - fluoxetine",	"desipramine - paroxetine",	"desipramine - sertraline",	"desipramine - venlafaxine",	"desvenlafaxine - ketoconazole",	"duloxetine - fluvoxamine",	"duloxetine - paroxetine",	"duloxetine - theophylline",	"escitalopram - cimetidine",	"escitalopram - omeprazole",	"fluoxetine - olanzapine",	"fluoxetine - propafenone",	"fluvastatin - fluconazole",	"fluvoxamine - lansoprazole",	"fluvoxamine - mexiletine",	"fluvoxamine - omeprazole",	"fluvoxamine - quinidine",	"fluvoxamine - theophylline",	"fluvoxamine - thioridazine",	"fluvoxamine - tolbutamide",	"haloperidol - venlafaxine",	"lovastatin - itraconazole",	"midazolam - clarithromycin",	"midazolam - diltiazem",	"midazolam - erythromycin",	"midazolam - fluconazole",	"midazolam - itraconazole",	"midazolam - ketoconazole",	"midazolam - nefazodone",	"mirtazapine - cimetidine",	"mirtazapine - paroxetine",	"nefazodone - triazolam",	"paliperidone - paroxetine",	"paroxetine - cimetidine",	"paroxetine - risperidone",	"paroxetine - terbinafine",	"pravastatin - clarithromycin",	"pravastatin - itraconazole",	"quetiapine - cimetidine",	"quetiapine - erythromycin",	"risperidone - venlafaxine",	"risperidone - verapamil",	"rosuvastatin - itraconazole",	"sertraline - cimetidine",	"simvastatin - diltiazem",	"simvastatin - erythromycin",	"simvastatin - ketoconazole",	"trazodone - clarithromycin",	"trazodone - ritonavir",	"triazolam - clarithromycin",	"triazolam - diltiazem",	"triazolam - erythromycin",	"triazolam - fluconazole",	"triazolam - itraconazole",	"triazolam - ketoconazole",	"venlafaxine - cimetidine",	"venlafaxine - diphenhydramine",	"venlafaxine - ketoconazole",	"venlafaxine - quinidine",	"venlafaxine - terbinafine",	"ziprasidone - cimetidine",	"zolpidem - itraconazole",	"zolpidem - ketoconazole"]

ddi_update = ["atorvastatin - aliskiren",	"atorvastatin - gemfibrozil",	"atorvastatin - telaprevir",	"atorvastatin - ticagrelor",	"pitavastatin - rifampin",	"pravastatin - rifampin",	"risperidone - ketoconazole",	"rosuvastatin - cyclosporine",	"rosuvastatin - eltrombopag",	"rosuvastatin - gemfibrozil",	"simvastatin - gemfibrozil",	"simvastatin - ranolazine",	"simvastatin - ticagrelor"]

ddi_case = ["clozapine - cimetidine",	"clozapine - ciprofloxacin",	"clozapine - isoniazid",	"clozapine - phenytoin",	"duloxetine - olanzapine",	"quetiapine - clarithromycin",	"quetiapine - valproate",	"simvastatin - amiodarone",	"simvastatin - ciprofloxacin",	"simvastatin - clarithromycin",	"simvastatin - cyclosporine", "simvastatin - nelfinavir"]

nonddi_obs = ["alprazolam - citalopram",	"alprazolam - sertraline",	"alprazolam - venlafaxine",	"aripiprazole - valproate",	"bupropion - ritonavir",	"bupropion - valproate",	"citalopram - ketoconazole",	"clozapine - sertraline",	"desipramine - atomoxetine",	"desipramine - ketoconazole",	"desipramine - nefazodone",	"fluoxetine - alosetron",	"fluoxetine - desloratadine",	"fluvastatin - erythromycin",	"haloperidol - quetiapine",	"nefazodone - cimetidine",	"quetiapine - risperidone",	"risperidone - erythromycin",	"sertraline - zolpidem",	"venlafaxine - indinavir",	"zolpidem - fluconazole"]

nonddi_dis = ["fluvastatin - itraconazole",	"nefazodone - pravastatin",	"pravastatin - diltiazem",	"pravastatin - fluconazole",	"rosuvastatin - erythromycin",	"rosuvastatin - fluconazole"]

nonddi_update = ["asenapine - valproate",	"atorvastatin - dabigatran",	"duloxetine - warfarin",	"pravastatin - nelfinavir",	"rosuvastatin - ketoconazole",	"rosuvastatin - warfarin",	"sertraline - phenytoin",	"simvastatin - sitagliptin"]

fileout = "./scr25-validation-set.tsv"
f = open(fileout,'w')
f.write("Pceut entity combination"+"\t"+"VALIDATION_SET_DDI"+"\t"+"VALIDATION_SET_NON_DDI"+"\t"+"DDI_DIKB"+"\t"+"NON_DDI_DIKB"+"\t"+"True_pos"+"\t"+"False_pos"+"\t"+"True_neg"+"\t"+"False_neg"+"\n")

fileout2 = "./scr25-combination-list.txt"
f2 = open(fileout2,'w')

for drug1 in main_drugs:
    for drug2 in all_drugs:
        if (drug1 == drug2):
            continue
        elif(drug2 in done_drugs):
            continue
        else:
            interaction = (drug1+' - '+drug2)
            f.write('"'+interaction+'"'+'\t')
            f2.write('"'+interaction+'"'+':None, ')
            if(interaction in ddi_obs):
                f.write("DIKB")
            elif(interaction in ddi_update):
                f.write("R01")
            elif(interaction in ddi_case):
                f.write("CR")
            elif(interaction in nonddi_obs):
                f.write("\tDIKB")
            elif(interaction in nonddi_dis):
                f.write("\tDIS")
            elif(interaction in nonddi_update):
                f.write("\tR01")
            f.write('\n')
    done_drugs.append(drug1)
        
f.close()
