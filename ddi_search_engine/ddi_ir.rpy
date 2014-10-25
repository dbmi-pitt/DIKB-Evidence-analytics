## -*-Mode:python-*-

from twisted.web import resource
from Bio.EUtils  import HistoryClient
import re

###html segments
head = '''<html><head><title>Query Results</title></head>'''
descr = '''<body>
                  <p>Results of Query for DDI</p>'''
tail = '''</body></html>'''

rct_images = '''<img src="./images/EVhigh.jpg" width=50 height=25>&nbsp;<img src="./images/IVmid.jpg" width=50 height=25>&nbsp;<img src="./images/SCVhigh.jpg" width=50 height=25>'''
crpt_images = '''
<img src="./images/EVlow.jpg" width=50 height=25>&nbsp;<img src="./images/IVlow.jpg" width=50 height=25>&nbsp;<img src="./images/SCVlow.jpg" width=50 height=25>
'''
epi_images = '''
<img src="./images/EVmid.jpg" width=50 height=25>&nbsp;<img src="./images/IVlow.jpg" width=50 height=25>&nbsp;<img src="./images/SCVlow.jpg" width=50 height=25>
'''
pk_invitro = '''
<img src="./images/EVlow.jpg" width=50 height=25>&nbsp;<img src="./images/IVlow.jpg" width=50 height=25>&nbsp;<img src="./images/SCVlow.jpg" width=50 height=25>
'''
pk_invivo = '''
<img src="./images/EVmid.jpg" width=50 height=25>&nbsp;<img src="./images/IVmid.jpg" width=50 height=25>&nbsp;<img src="./images/SCVlow.jpg" width=50 height=25>
'''
r_table_start = '''<table>'''
r_table_end = '''</table>'''
res_start_even = '''<tr>
<td>
<a href="'''
a_target = '''" target = "_blank">'''
res_start_odd  = '''<tr>
<td bgcolor="ccccff">
<a href=" ''' 
res_end = '''</tr>'''

lres_start_even = '''<tr>
<td>'''
lres_start_odd  = '''<tr>
<td bgcolor="ccccff">''' 
lres_end = '''</td></tr>'''


a_end = '''</a>'''
link_head = '''http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=pubmed&dopt=Abstract&list_uids='''
link_tail = '''&query_hl=1'''

form = '''
<br>
<b>Search for another interaction:</b><br>
<form action="ddi_ir.rpy" method="POST">      
     <table cellpadding="0" cellspacing="0">
	<tr>
        <td>
          &nbsp;&nbsp;<span class="smallFont">Pharmaceutical entity 1:</span><br>
          &nbsp;&nbsp;<input type="text" name="object" size="30">
	</td>
        </tr>
	<tr>
	<td>
        &nbsp;&nbsp;<span class="smallFont">Pharmaceutical entity 2:</span><br>
	 &nbsp;&nbsp;<input type="text" name="precipitant" size="30">
      	</td>
	<td>
         &nbsp;&nbsp;&nbsp;<input type="submit" name="Go" value="Go">
        </td>

      </tr>
     
      <!-- <tr>
      <td>
      <b>Display results with <select name = "or">
      <option value = "false" selected="true">any</option>
      <option value = "true">all</option>
      </select> of the following:</b><br>
      </td>
      </tr> -->

      <tr>
      <td><input type="checkbox" name = "rct">
      Randomized controlled trials</td><td>&nbsp;</td>
      </tr>
      <!-- <tr>
      <td><input type="checkbox" name = "epi">
      Epidemiological trials</td><td>&nbsp;</td>
      </tr>
      <tr> -->
      <td><input type="checkbox" name = "case">
      Case Report</td><td>&nbsp;</td>
      </tr>
      <!-- <tr>
      <td><input type="checkbox" name = "pharmk_vitro">
      Pharmokinetics in vitro</td><td>&nbsp;</td>
      </tr>
      <tr>
      <td><input type="checkbox" name="pharmk_vivo">
      Pharmokinetics in vivo</td><td>&nbsp;</td>
      </tr> -->
      <tr>
	<td><input type="checkbox" name = "label">
	Product Labeling</td><td>&nbsp;</td>
      </tr>
     </table>
    </form>
        <br>
<table>
<tr>
<td colspan = 2">Legend</td>
</tr>
<tr>
<td><img src="./images/low.jpg" width=50 height=25></td>
<td>Low in validity</td>
</tr>
<tr>
<td><img src="./images/mid.jpg" width=50 heigth=25></td>
<td>Medium in validity</td>
</tr>
<tr>
<td><img src="./images/high.jpg" width=50 height=25></td>
<td>High in validity</td>
</tr>
<tr>
<td><img src = "./images/IVtemplate.jpg" width=50 height=25></td>
<td>Internal Validity</td>
</tr>
<tr>
<td><img src="./images/EVtemplate.jpg" width=50 height=25></td>
<td>External Validity</td>
</tr>
<tr>
<td><img src="./images/SCVtemplate.jpg" width=50 height=25></td>
<td>Statistical Conclusion Validity</td>
</tr>
</table>
'''

DRUGS = {'alprazolam':['ALPRAZOLAM', 'ALPRAZOLAM INTENSOL', 'NIRAVAM', 'XANAX', 'XANAX XR'],
         'atorvastatin':['ATORVASTATIN','CADUET','LIPITOR'],
         'clarithromycin':['CLARITHROMYCIN', 'CLARITHROMYCIN EXTENDED RELEASE', 'BIAXIN', 'BIAXIN XL'],
         'diltiazem':['DILTIAZEM', 'DILTIAZEM HYDROCHLORIDE', 'CARDIZEM','CARDIZEM CD', 'CARDIZEM LA', 'CARDIZEMLYO-JECT', 'CARDIZEM MONOVIAL', 'CARDIZEM SR', 'CARTIA', 'CARTIA XT', 'DILACOR XR', 'DILT', 'DILT-CD', 'DILT-XR', 'DILTIA XT', 'DILTZAC',  'TAZTIA', 'TAZTIA XT', 'TECZEM', 'TIAMATE', 'TIAZAC'],
         'erythromycin':['ERYTHROMYCIN',  'AKNEMYCIN', 'BRISTAMYCIN', 'E-SOLVE-2', 'E-BASE', 'E-MYCIN', 'E-MYCINE', 'E-SOLVE 2', 'E.E.S', 'E.E.S. 400 FILMTAB', 'E.E.S. GRANULES', 'E.E.S.-200', 'E.E.S.-400', 'EMGEL', 'ERY-SOL', 'ERY-TAB', 'ERYPED', 'ERYC', 'ERYC 125', 'ERYC SPRINKLES', 'ERYMAX', 'ERYPAR', 'ERYPED', 'ERYTHROCIN', 'ERYTHROCIN STEARATE', 'ERYTHROMYCIN ESTOLATE ', 'ERYTHROMYCIN ETHYLSUCCINATE', 'ERYTHROMYCIN LACTOBIONATE', 'ERYTHROMYCIN STEARATE', 'ETHRIL 250', 'ETHRIL 500', 'ERYZOLE', 'ILOSONE', 'ILOTYCIN', 'PCE', 'PCE BRAND OF ERYTHROMYCIN', 'PEDIAMYCIN', 'PEDIAMYCIN 400', 'ROBIMYCIN', 'ROMYCIN', 'WYAMYCIN E', 'WYAMYCIN S'],
         'fluconazole':['FLUCONAZOLE', 'DIFLUCAN', 'DIFLUCAN IN DEXTROSE 5% IN PLASTIC CONTAINER', 'DIFLUCAN IN SODIUM CHLORIDE 0.9%', 'DIFLUCAN IN SODIUM CHLORIDE 0.9% IN PLASTIC CONTAINER', 'FLUCONAZALE', 'FLUCONAZOLE IN DEXTROSE 5% IN PLASTIC CONTAINER', 'FLUCONAZOLE IN SODIUM CHLORIDE 0.9%', 'FLUCONAZOLE IN SODIUM CHLORIDE 0.9% IN PLASTIC CONTAINER'],
         'gemfibrozil':['gemfibrozil','lopid'],
         'itraconazole':['ITRACONAZOLE','SPORANOX','SPORANOX-PULSE'],
         'ketoconazole':['KETOCONAZOLE'],
         'lovastatin':['LOVASTATIN', 'ADVICOR', 'ALTOPREV', 'MEVACOR'],
         'midazolam':['MIDAZOLAM', 'MIDAZOLAM HYDROCHLORIDE', 'MIDAZOLAM HYDROCHLORIDE PRESERVATIVE FREE', 'VERSED'],
         'paclitaxel':['paclitaxel','abraxane','onxol','taxol'],
         'pravastatin':['PRAVASTATIN', 'PRAVASTATIN SODIUM', 'PRAVACHOL'],
         'rosuvastatin':['ROSUVASTATIN', 'CRESTOR'],
         'simvastatin':['SIMVASTATIN', 'ZOCOR'],
         'fluvastatin':['FLUVASTATIN', 'FLUVASTATIN XI', 'LESCOL'],
         'triazolam':['TRIAZOLAM', 'HALCION'],
         'nefazodone':['NEFAZODONE', 'NEFAZODONE HYDROCHLORIDE', 'SERZONE'],
         'warfarin':['warfarin'],
         'bosentan':['bosentan'],
         'acebutolol':['acebutolol'],
         'alfentanil':['alfentanil'],
         'aminoglutethimide':['aminoglutethimide'],
         'amiodarone':['amiodarone'],
         'amitriptyline':['amitriptyline'],
         'amlodipine':['amlodipine'],
         'amprenavir':['amprenavir'],
         'aprepitant':['aprepitant'],
         'aripiprazole':['aripiprazole'],
         'astemizole':['astemizole'],
         'atazanavir':['atazanavir'],
         'atenolol':['atenolol'],
         'atomoxetine':['atomoxetine'],
         'atovastatin':['atovastatin'],
         'benazepril':['benazepril'],
         'bepridil':['bepridil'],
         'bexarotene':['bexarotene'],
         'bisoprolol':['bisoprolol'],
         'bromocriptine':['bromocriptine'],
         'budesonide':['budesonide'],
         'bupivacaine':['bupivacaine'],
         'buprenorphine':['buprenorphine'],
         'bupropion':['bupropion'],
         'buspirone':['buspirone'],
         'caffeine':['caffeine'],
         'candesartan':['candesartan'],
         'captopril':['captopril'],
         'carbamazepine':['carbamazepine'],
         'carisoprodol':['carisoprodol'],
         'carvedilol':['carvedilol'],
         'celecoxib':['celecoxib'],
         'cevimeline':['cevimeline'],
         'chloroquine':['chloroquine'],
         'chlorpheniramine':['chlorpheniramine'],
         'chlorpromazine':['chlorpromazine'],
         'chlorpropamide':['chlorpropamide'],
         'cilostazol':['cilostazol'],
         'cimetidine':['cimetidine'],
         'ciprofloxacin':['ciprofloxacin'],
         'cisapride':['cisapride'],
         'citalopram':['citalopram'],
         'clomipramine':['clomipramine'],
         'clopidogrel':['clopidogrel'],
         'clotrimazole':['clotrimazole'],
         'clozapine':['clozapine'],
         'codeine':['codeine'],
         'colchicine':['colchicine'],
         'cotrimoxazole':['cotrimoxazole'],
         'cyclosporine':['cyclosporine'],
         'danazol':['danazol'],
         'dapsone':['dapsone'],
         'daunorubicin':['daunorubicin'],
         'debrisoquin':['debrisoquin'],
         'debrisoquine':['debrisoquine'],
         'delavirdine':['delavirdine'],
         'desipramine':['desipramine'],
         'desvenlafaxine':['desvenlafaxine'],
         'dexamethasone':['dexamethasone'],
         'dextromethorphan':['dextromethorphan'],
         'diazepam':['diazepam'],
         'diclofenac':['diclofenac'],
         'digoxin':['digoxin'],
         'dihydrocodeine':['dihydrocodeine'],
         'diphenhydramine':['diphenhydramine'],
         'disopyramide':['disopyramide'],
         'disulfiram':['disulfiram'],
         'docetaxel':['docetaxel'],
         'dofetilide':['dofetilide'],
         'donepezil':['donepezil'],
         'doxepin':['doxepin'],
         'doxorubicin':['doxorubicin'],
         'dronabinol':['dronabinol'],
         'droperidol':['droperidol'],
         'duloxetine':['duloxetine'],
         'dutasteride':['dutasteride'],
         'efavirenz':['efavirenz'],
         'eletriptan':['eletriptan'],
         'enalapril':['enalapril'],
         'encainide':['encainide'],
         'enoxacin':['enoxacin'],
         'eplerenone':['eplerenone'],
         'ergotamine':['ergotamine'],
         'escitalopram':['escitalopram'],
         'estradiol':['estradiol'],
         'ethanol':['ethanol'],
         'etoposide':['etoposide'],
         'felbamate':['felbamate'],
         'felodipine':['felodipine'],
         'fentanyl':['fentanyl'],
         'fexofenadine':['fexofenadine'],
         'finasteride':['finasteride'],
         'flecainide':['flecainide'],
         'fluorouracil':['fluorouracil'],
         'fluoxetine':['fluoxetine'],
         'fluphenazine':['fluphenazine'],
         'flurbiprofen':['flurbiprofen'],
         'fluvoxamine':['fluvoxamine'],
         'frovatriptan':['frovatriptan'],
         'furosemide':['furosemide'],
         'gabapentin':['gabapentin'],
         'galantamine':['galantamine'],
         'gefitinib':['gefitinib'],
         'gestodene':['gestodene'],
         'glimepiride':['glimepiride'],
         'glipizide':['glipizide'],
         'glyburide':['glyburide'],
         'griseofulvin':['griseofulvin'],
         'haloperidol':['haloperidol'],
         'hydrochlorothiazide':['hydrochlorothiazide'],
         'hydrocodone':['hydrocodone'],
         'hyperforin':['hyperforin'],
         'ibuprofen':['ibuprofen'],
         'ifosfamide':['ifosfamide'],
         'imatinib':['imatinib'],
         'imipramine':['imipramine'],
         'indinavir':['indinavir'],
         'indomethacin':['indomethacin'],
         'irbesartan':['irbesartan'],
         'irinotecan':['irinotecan'],
         'isoniazid':['isoniazid'],
         'isradipine':['isradipine'],
         'lamotrigine':['lamotrigine'],
         'lansoprazole':['lansoprazole'],
         'leflunomide':['leflunomide'],
         'levetiracetam':['levetiracetam'],
         'levomethadyl':['levomethadyl'],
         'lidocaine':['lidocaine'],
         'lisinopril':['lisinopril'],
         'loperamide':['loperamide'],
         'lopinavir':['lopinavir'],
         'loratadine':['loratadine'],
         'losartan':['losartan'],
         'maprotiline':['maprotiline'],
         'meloxicam':['meloxicam'],
         'methadone':['methadone'],
         'methamphetamine':['methamphetamine'],
         'methylprednisolone':['methylprednisolone'],
         'metoprolol':['metoprolol'],
         'metronidazole':['metronidazole'],
         'mexiletine':['mexiletine'],
         'miconazole':['miconazole'],
         'mifepristone':['mifepristone'],
         'mirtazapine':['mirtazapine'],
         'mitomycin':['mitomycin'],
         'modafinil':['modafinil'],
         'molindone':['molindone'],
         'montelukast':['montelukast'],
         'morphine':['morphine'],
         'nafcillin':['nafcillin'],
         'naproxen':['naproxen'],
         'nateglinide':['nateglinide'],
         'nelfinavir':['nelfinavir'],
         'nevirapine':['nevirapine'],
         'nicardipine':['nicardipine'],
         'nifedipine':['nifedipine'],
         'nimodipine':['nimodipine'],
         'nisoldipine':['nisoldipine'],
         'norfloxacin':['norfloxacin'],
         'nortriptyline':['nortriptyline'],
         'olanzapine':['olanzapine'],
         'olmesartan':['olmesartan'],
         'omeprazole':['omeprazole'],
         'ondansetron':['ondansetron'],
         'oxcarbazepine':['oxcarbazepine'],
         'oxycarbazepine':['oxycarbazepine'],
         'oxycodone':['oxycodone'],
         'paliperidone':['paliperidone'],
         'pantoprazole':['pantoprazole'],
         'paroxetine':['paroxetine'],
         'pentamidine':['pentamidine'],
         'perhexiline':['perhexiline'],
         'perindopril':['perindopril'],
         'perphenazine':['perphenazine'],
         'phenacetin':['phenacetin'],
         'phenobarbital':['phenobarbital'],
         'phenytoin':['phenytoin'],
         'pimozide':['pimozide'],
         'pioglitazone':['pioglitazone'],
         'piroxicam':['piroxicam'],
         'plicamycin':['plicamycin'],
         'prednisolone':['prednisolone'],
         'prednisone':['prednisone'],
         'primidone':['primidone'],
         'proguanil':['proguanil'],
         'promethazine':['promethazine'],
         'propafenone':['propafenone'],
         'propoxyphene':['propoxyphene'],
         'propranolol':['propranolol'],
         'quetiapine':['quetiapine'],
         'quinacrine':['quinacrine'],
         'quinapril':['quinapril'],
         'quinidine':['quinidine'],
         'quinupristin':['quinupristin'],
         'rabeprazole':['rabeprazole'],
         'ramipril':['ramipril'],
         'repaglinide':['repaglinide'],
         'rifabutin':['rifabutin'],
         'rifampin':['rifampin'],
         'risperidone':['risperidone'],
         'ritonavir':['ritonavir'],
         'rivastigmine':['rivastigmine'],
         'rofecoxib':['rofecoxib'],
         'ropinirole':['ropinirole'],
         'rosiglitazone':['rosiglitazone'],
         'saquinavir':['saquinavir'],
         'selegiline':['selegiline'],
         'sertraline':['sertraline'],
         'sibutramine':['sibutramine'],
         'sildenafil':['sildenafil'],
         'sirolimus':['sirolimus'],
         'sotalol':['sotalol'],
         'sufentanil':['sufentanil'],
         'sulfamethizole':['sulfamethizole'],
         'sulfamethoxazole':['sulfamethoxazole'],
         'sulfinpyrazone':['sulfinpyrazone'],
         'sulphaphenazole':['sulphaphenazole'],
         'tacrine':['tacrine'],
         'tacrolimus':['tacrolimus'],
         'tadalafil':['tadalafil'],
         'tamoxifen':['tamoxifen'],
         'telmisartan':['telmisartan'],
         'teniposide':['teniposide'],
         'terbinafine':['terbinafine'],
         'terfenadine':['terfenadine'],
         'testosterone':['testosterone'],
         'theophylline':['theophylline'],
         'thioridazine':['thioridazine'],
         'thiothixene':['thiothixene'],
         'ticlopidine':['ticlopidine'],
         'timolol':['timolol'],
         'tolbutamide':['tolbutamide'],
         'tolterodine':['tolterodine'],
         'topiramate':['topiramate'],
         'torsemide':['torsemide'],
         'tramadol':['tramadol'],
         'trandolapril':['trandolapril'],
         'trazodone':['trazodone'],
         'trifluoperazine':['trifluoperazine'],
         'trimethoprim':['trimethoprim'],
         'troleandomycin':['troleandomycin'],
         'valdecoxib':['valdecoxib'],
         'valproate':['valproate'],
         'valsartan':['valsartan'],
         'vardenafil':['vardenafil'],
         'venlafaxine':['venlafaxine'],
         'verapamil':['verapamil'],
         'vinblastine':['vinblastine'],
         'vincristine':['vincristine'],
         'voriconazole':['voriconazole'],
         'zafirlukast':['zafirlukast'],
         'zaleplon':['zaleplon'],
         'zileuton':['zileuton'],
         'ziprasidone':['ziprasidone'],
         'zolpidem':['zolpidem'],
         'zonisamide':['zonisamide']
         }


###class that processes the form
class Resource(resource.Resource):
    def __init__(self):
        self.summary = ""
        self.error = "no results for this query \nsyntax: "
        self.rct_filter = "Clinical Trial [PT]"
        self.ct_filter = "Case Reports [PT]"
        self.other_filter = "NOT Case Reports [PT] NOT Clinical Trial [PT]"
    
    def render(self, request):
        if request.args.has_key("object"):
            d1 = request.args["object"][0]
        else:
            d1 = "Please enter two pharmaceutical entities."
            page = head + descr + '''<p>''' + d1 + '''</p>''' + tail
            return page
        if request.args.has_key("precipitant"):
            d2 = request.args["precipitant"][0]
        else:
            d2 = "Please enter two pharmaceutical entities."
            head + descr + '''<p>''' + d2 + '''</p>''' + tail
            return page

        #print request.args.keys()
        self.summary = ""
        (rct, case, label, other) = (None, None, None, None)
        if request.args.has_key("rct"):
            rct = 1

        if request.args.has_key("case"):
            case = 1

        if request.args.has_key("label"):
            label = 1

        if request.args.has_key("other"):
            other = 1

        if rct:
            d1_l = DRUGS[d1]
            d2_l = DRUGS[d2]
            for d_1 in d1_l:
                for d_2 in d2_l:
                    phar1 = None
                    
                    client1 = HistoryClient.HistoryClient()
                    q = '''%s AND ("%s" [MeSH Terms] OR %s [Text Word]) AND ("%s" [MeSH Terms] OR %s [Text Word])''' % (self.rct_filter, d_1, d_1, d_2, d_2)
                    phar1 = client1.search(q)

                    rc_results = ""
                    self.summary = self.summary + '''<p><h3>randomized controlled trials for %s and %s: %s results </h3><br></p><table>''' % (d_1, d_2, str(len(phar1)))
                    for i in range(0,len(phar1)):
                        rec = phar1[i].efetch(retmode = "text", rettype = "abstract").read()
                        id = re.findall("PMID: \d+",rec)
                        id = " ".join(id)
                        id = id[6:]
                        if i % 2 == 0:
                            rc_results = " ".join([rc_results,
                                                   res_start_even,
                                                   "".join([link_head,id,link_tail]),
                                                   a_target,
                                                   "".join(["PubMed ID:",id]),
                                                   a_end,
                                                   rct_images,
                                                   '''<br>''',
                                                   rec,
                                                   '''</td>''',
                                                   res_end,
                                                   r_table_end,
                                                   '''<br><br>'''])
                        else:
                            rc_results = " ".join([rc_results,
                                                   r_table_start,
                                                   res_start_odd,
                                                   "".join([link_head,id,link_tail]),
                                                   a_target,
                                                   "".join(["PubMed ID:",id]),
                                                   a_end,
                                                   rct_images,
                                                   '''<br>''',
                                                   rec,
                                                   '''</td>''',
                                                   res_end,
                                                   '''<br><br>'''])
                    self.summary = " ".join([self.summary,rc_results,'''</table>'''])

        if case:
            d1_l = DRUGS[d1]
            d2_l = DRUGS[d2]
            for d_1 in d1_l:
                for d_2 in d2_l:
                    phar2 = None
                    client2 = HistoryClient.HistoryClient()
                    q = '''%s AND ("%s" [MeSH Terms] OR %s [Text Word]) AND ("%s" [MeSH Terms] OR %s [Text Word])''' % (self.ct_filter, d_1, d_1, d_2, d_2)
                    phar2 = client2.search(q)

                    ct_results = ""
                    self.summary =  self.summary + '''<p><h3>case reports for %s and %s: %s results </h3><br></p><table>''' % (d_1, d_2, str(len(phar2)))
                   
                    for i in range(0,len(phar2)):
                        rec = phar2[i].efetch(retmode = "text", rettype = "abstract").read()
                        id = re.findall("PMID: \d+",rec)
                        id = " ".join(id)
                        id = id[6:]
                        if i % 2 == 0:
                            ct_results = " ".join([ct_results,
                                                   res_start_even,
                                                   "".join([link_head,id,link_tail]),
                                                   a_target,
                                                   "".join(["PubMed ID:",id]),
                                                   a_end,
                                                   crpt_images,
                                                   '''<br>''',
                                                   rec,
                                                   '''</td>''',
                                                   res_end,
                                                   r_table_end,
                                                   '''<br><br>'''])
                        else:
                            ct_results = " ".join([ct_results,
                                                   r_table_start,
                                                   res_start_odd,
                                                   "".join([link_head,id,link_tail]),
                                                   a_target,
                                                   "".join(["PubMed ID:",id]),
                                                   a_end,
                                                   crpt_images,
                                                   '''<br>''',
                                                   rec,
                                                   '''</td>''',
                                                   res_end,
                                                   '''<br><br>'''])
                    self.summary = self.summary + ct_results

        if label:
            from urllib import urlopen
            st_d1 = urlopen('''http://dailymed.nlm.nih.gov/dailymed/search.cfm?startswith=%s&x=0&y=0''' % d1).read()
            n_std1 = st_d1.replace("\n", "").replace("\r","").replace("\t","")

            st_d2 = urlopen('''http://dailymed.nlm.nih.gov/dailymed/search.cfm?startswith=%s&x=0&y=0''' % d2).read()
            n_std2 = st_d2.replace("\n", "").replace("\r","").replace("\t","")
            lab_results = "" 
            r = re.compile('(<a href=\"drugInfo\.cfm.*</p></a>)')
            d1_lab_l = r.findall(n_std1)
            d2_lab_l = r.findall(n_std2)

            
            self.summary = self.summary + '''<br><br><h3>drug labels: ''' +  str(len(d1_lab_l) + len(d2_lab_l)) + ''' results </h3><br>'''
                
            for i in range(0,len(d1_lab_l)):
                if i % 2 == 0:
                    lab_results = " ".join([lab_results,
                                           lres_start_even,
                                            d1_lab_l[i].replace("drugInfo.cfm", "http://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm"),
                                            '''</td>''',
                                            lres_end,
                                            r_table_end,
                                            '''<br><br>'''])
                else:
                    lab_results = " ".join([lab_results,
                                            r_table_start,
                                            lres_start_odd,
                                            d1_lab_l[i].replace("drugInfo.cfm", "http://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm"),
                                            '''</td>''',
                                            lres_end,
                                            '''<br><br>'''])
            for i in range(0,len(d2_lab_l)):
                if i % 2 == 0:
                    lab_results = " ".join([lab_results,
                                            lres_start_even,
                                            d2_lab_l[i].replace("drugInfo.cfm", "http://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm"),
                                            '''</td>''',
                                            lres_end,
                                            r_table_end,
                                            '''<br><br>'''])
                else:
                    lab_results = " ".join([lab_results,
                                           r_table_start,
                                           lres_start_odd,
                                            d2_lab_l[i].replace("drugInfo.cfm", "http://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm"),
                                            '''</td>''',
                                            lres_end,
                                            '''<br><br>'''])
                    
            self.summary = self.summary + lab_results

        if other:
            d1_l = DRUGS[d1]
            d2_l = DRUGS[d2]
            for d_1 in d1_l:
                for d_2 in d2_l:
                    phar1 = None
                    
                    client1 = HistoryClient.HistoryClient()
                    q = '''("%s" [MeSH Terms] OR %s [Text Word]) AND ("%s" [MeSH Terms] OR %s [Text Word]) %s ''' % (d_1, d_1, d_2, d_2, self.other_filter)
                    phar1 = client1.search(q)

                    rc_results = ""
                    self.summary = self.summary + '''<p><h3>Non-clinical trial/case report results for %s and %s: %s results </h3><br></p><table>''' % (d_1, d_2, str(len(phar1)))
                    for i in range(0,len(phar1)):
                        rec = phar1[i].efetch(retmode = "text", rettype = "abstract").read()
                        id = re.findall("PMID: \d+",rec)
                        id = " ".join(id)
                        id = id[6:]
                        if i % 2 == 0:
                            rc_results = " ".join([rc_results,
                                                   res_start_even,
                                                   "".join([link_head,id,link_tail]),
                                                   a_target,
                                                   "".join(["PubMed ID:",id]),
                                                   a_end,
                                                   rct_images,
                                                   '''<br>''',
                                                   rec,
                                                   '''</td>''',
                                                   res_end,
                                                   r_table_end,
                                                   '''<br><br>'''])
                        else:
                            rc_results = " ".join([rc_results,
                                                   r_table_start,
                                                   res_start_odd,
                                                   "".join([link_head,id,link_tail]),
                                                   a_target,
                                                   "".join(["PubMed ID:",id]),
                                                   a_end,
                                                   rct_images,
                                                   '''<br>''',
                                                   rec,
                                                   '''</td>''',
                                                   res_end,
                                                   '''<br><br>'''])
                    self.summary = " ".join([self.summary, rc_results,'''</table>'''])

            
        page = head + descr + form + self.summary + tail
        return page

resource = Resource()

