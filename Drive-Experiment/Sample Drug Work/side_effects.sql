----- SAM ROSKO'S SQL FILE FOR SPLICER/SIDER QUERIES
----- LAST UPDATED: 6/10/2015
----- TO DO: None


---------- LAERTES/SPLICER INFO ----------
--- Dr. Boyce pointed me to using the laertes_summary table to get the drug info and then combining with other tables... here’s the new selection code samples:


SELECT *
FROM laertes_summary
WHERE report_order = 1 AND ingredient = 'Haloperidol';


--- this allows me to get rolled up ingredient_id, which is an RxNorm concept number, which is, in this example using haloperidol, ID# 766529


SELECT DISTINCT snomed_hoi
FROM drug_hoi_relationship
WHERE drug = 766529
ORDER BY snomed_hoi;


--- this gets me the list of unique side effects for a given rolled up drug entity, this number differs from any counts shown in laertes_summary, though
--- condensed into one step (example for haloperidol):


SELECT DISTINCT snomed_hoi
FROM drug_hoi_relationship
WHERE drug = (SELECT ingredient_id
   FROM laertes_summary
   WHERE report_order = 1 AND ingredient = 'Haloperidol')
ORDER BY snomed_hoi;


---------- SIDER INFO ----------


-- OLD CODE:
-- problem with this code: it only yields results for one version of the drug in question, not rolled up like splicer
-- have to find a way to get a level above where I'm searching now


SELECT DISTINCT ?dLabel
WHERE {
  ?d a <http://bio2rdf.org/sider_vocabulary:Drug>;
     <http://bio2rdf.org/sider_vocabulary:generic-name> ?dNameURI.

  ?dNameURI <http://www.w3.org/2000/01/rdf-schema#label> ?dLabel.
}


-- above can be used to find the resource name for the generic form of both gemfibrozil/ketoconazole
-- below finds the side effect list for risperidone, for example


SELECT DISTINCT ?dSide
WHERE {
  ?d a <http://bio2rdf.org/sider_vocabulary:Drug>;
     <http://bio2rdf.org/sider_vocabulary:generic-name> ?dNameURI;
     <http://bio2rdf.org/sider_vocabulary:side-effect> ?dSide.

  ?dNameURI <http://www.w3.org/2000/01/rdf-schema#label> "risperidone [sider_resource:2182fe965943f2056b7eb2cd9515bce9]"@en.
}
ORDER BY ?dSide


-- NEW CODE:
-- unless I am just unaware of it, I do not believe that SIDER has rolled up results, so I have to manually roll them up using REGEX


SELECT DISTINCT ?dSide
WHERE {
  ?d a <http://bio2rdf.org/sider_vocabulary:Drug>;
     <http://bio2rdf.org/sider_vocabulary:generic-name> ?dNameURI;
     <http://bio2rdf.org/sider_vocabulary:side-effect> ?dSideURI.

  ?dNameURI <http://www.w3.org/2000/01/rdf-schema#label> ?dLabel.
  ?dSideURI <http://www.w3.org/2000/01/rdf-schema#label> ?dSide.

  FILTER regex(?dLabel, "haloperidol", "i")
}
ORDER BY ?dSide


-- for comparing the lists (this just has the extra ?dLabel, which shows which forms of drug are included and which side effects correspond to which form):


SELECT DISTINCT ?dLabel ?dSide
WHERE {
  ?d a <http://bio2rdf.org/sider_vocabulary:Drug>;
     <http://bio2rdf.org/sider_vocabulary:generic-name> ?dNameURI;
     <http://bio2rdf.org/sider_vocabulary:side-effect> ?dSideURI.

  ?dNameURI <http://www.w3.org/2000/01/rdf-schema#label> ?dLabel.
  ?dSideURI <http://www.w3.org/2000/01/rdf-schema#label> ?dSide.

  FILTER regex(?dLabel, "haloperidol", "i")
}
ORDER BY ?dSide


-- special case, cause escitalopram comes up due to regex and interferes with citalopram results


SELECT DISTINCT ?dSide
WHERE {
  ?d a <http://bio2rdf.org/sider_vocabulary:Drug>;
     <http://bio2rdf.org/sider_vocabulary:generic-name> ?dNameURI;
     <http://bio2rdf.org/sider_vocabulary:side-effect> ?dSideURI.

  ?dNameURI <http://www.w3.org/2000/01/rdf-schema#label> ?dLabel.
  ?dSideURI <http://www.w3.org/2000/01/rdf-schema#label> ?dSide.

  FILTER (!regex(?dLabel, "escitalopram", "i"))
  FILTER regex(?dLabel, "citalopram", "i")
}
ORDER BY ?dSide


---------- END ----------
