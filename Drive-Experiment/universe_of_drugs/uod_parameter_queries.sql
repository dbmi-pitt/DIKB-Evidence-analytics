-- Query DrugBank for ATC classes
SELECT DISTINCT level_code, count(*)
FROM drugbank.drug_atc_code_levels
WHERE primary_drugbank_id in ()
AND Length(level_code) = 1
ORDER BY level_code
;

-- Query DrugBank for CYP enzymes targeted
SELECT name, count(*)
FROM drugbank.drug_enzymes
WHERE primary_drugbank_id in ()
AND name like 'Cytochrome P450%'
GROUP BY name
ORDER BY name
;

-- Query DrugCentral for CYP enzymes targeted
SELECT target_name, count(target_name)
FROM act_table_full
WHERE struct_id in ()
and target_class = 'Enzyme' and target_name LIKE 'Cytochrome P450%'
GROUP BY target_name
ORDER BY target_name
;

-- Query DrugBank for action on CYP enzymes
SELECT action, count(*)
FROM drugbank.drug_enzyme_actions
WHERE primary_drugbank_id in ()
AND id in 
(SELECT id
FROM drugbank.drug_enzymes
WHERE primary_drugbank_id in ()
AND name like 'Cytochrome P450%'
ORDER BY name)
GROUP BY action
ORDER BY action
;

-- Query DrugBank for transporters targeted
SELECT gene_name, count(gene_name)
FROM drugbank.drug_transporter_polypeptides
WHERE primary_drugbank_id in ()
and gene_name in ('ABCB1', 'ABCG2', 'SLC22A2', 'SLC22A6', 'SLC22A8', 'SLCO1B1', 'SLCO1B3')
GROUP BY  gene_name
ORDER BY  gene_name
;

-- Query DrugBank for actions on targeted transporters
SELECT action, count(*)
FROM drugbank.drug_transporter_actions
WHERE primary_drugbank_id in () 
and id in ('BE0001067', 'BE0001032', 'BE0001066', 'BE0003659', 'BE0003647', 
'BE0001004', 'BE0003645')
GROUP BY action
ORDER BY action
;

-- Query DrugCentral for transporters targeted
SELECT gene, count(gene)
FROM act_table_full
WHERE struct_id in ()
and target_class = 'Transporter'
GROUP BY gene
ORDER BY gene
;
