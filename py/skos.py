__author__ = "Florian Thiery"
__copyright__ = "MIT Licence 2022-2023, LEIZA, Florian Thiery"
__credits__ = ["Florian Thiery"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Florian Thiery"
__email__ = "florian.thiery@leiza.de"
__status__ = "beta"
__update__ = "2023-03-23"

# import dependencies
import uuid
import requests
import io
import pandas as pd
import os
import codecs
import datetime
import importlib  # py3
import sys

# set UTF8 as default
importlib.reload(sys)  # py3
# reload(sys) #py2

# uncomment the line below when using Python version <3.0
# sys.setdefaultencoding('UTF8')

# set starttime
starttime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

# set input csv
csv = "parent.csv"
csv2 = "items.csv"
dir_path = os.path.dirname(os.path.realpath(__file__))
file_in = dir_path.replace("\\py", "\\csv") + "\\" + csv
file_in2 = dir_path.replace("\\py", "\\csv") + "\\" + csv2

print(file_in)
print(file_in2)

# read csv file
data = pd.read_csv(
    file_in,
    encoding='utf-8',
    sep=',',
    usecols=['id', 'de', 'en', 'dk', 'nl', 'fr',
             'it', 'es', 'pl', 'gr', 'he', 'navisid']
)
print(data.info())

# create triples from dataframe
lineNo = 2
outStr = ""
lines = []

# general metadata

lines.append("nomt:ImportPythonScript" + " " +
             "rdf:type" + " " + "prov:SoftwareAgent .")
lines.append("nomt:ImportPythonScript" + " " + "rdfs:seeAlso" + " " +
             "<https://github.com/archaeolink/navisone-maritime-thesaurus> .")
lines.append("nomt:ImportPythonScript" + " " + "dct:source" + " " +
             "<https://github.com/archaeolink/navisone-maritime-thesaurus> .")
lines.append("nomt:ImportPythonScript" + " " + "rdfs:seeAlso" + " " +
             "<https://github.com/archaeolink/navisone-maritime-thesaurus/blob/main/py/skos.py> .")
lines.append("nomt:ImportPythonScript" + " " + "dct:source" + " " +
             "<https://github.com/archaeolink/navisone-maritime-thesaurus/blob/main/py/skos.py> .")
lines.append("nomt:ImportPythonScript" + " " +
             "dct:creator" + " " + " wd:Q66606154" + " .")
lines.append("wd:Q66606154 rdfs:label 'Florian Thiery M.Sc.'@en .")
lines.append("nomt:ImportPythonScript" + " " +
             "dct:license" + " " + "<https://github.com/archaeolink/navisone-maritime-thesaurus/blob/main/LICENCE>" + " .")
lines.append("nomt:ImportPythonScript" + " " +
             "dct:license" + " " + "'MIT License'@en" + " .")
lines.append("nomt:ImportPythonScript" + " " +
             "dct:bibliographicCitation" + " " + "'10.5281/zenodo.7353771'" + " .")
lines.append("nomt:ImportPythonScript" + " " +
             "dct:bibliographicCitation" + " " + "<https://github.com/archaeolink/navisone-maritime-thesaurus/blob/main/CITATION.cff>" + " .")

# create skos:Concept Scheme

lines.append("nomt:" + "cs01" + " " + "rdf:type" + " skos:ConceptScheme .")
lines.append("nomt:" + "cs01" + " " + "dct:license" + " <" +
             "http://creativecommons.org/licenses/by-sa/4.0/" + "> .")
lines.append(
    "<http://creativecommons.org/licenses/by-sa/4.0/> rdfs:label 'CC BY-SA 4.0'@en .")
lines.append("nomt:" + "cs01" + " " + "cc:license" + " <" +
             "http://creativecommons.org/licenses/by-sa/4.0/" + "> .")
lines.append("nomt:" + "cs01" + " " +
             "cc:attributionURL" + " wd:Q115264627" + " .")
lines.append("nomt:" + "cs01" + " " + "cc:attributionName" + " '" +
             "Arbeitsbereich Wissenschaftliche IT, Digitale Plattformen und Tools des LEIZA" + "' .")
lines.append("nomt:" + "cs01" + " " + "dct:title" +
             " 'NAVISone Maritime Thesaurus' .")
lines.append("nomt:" + "cs01" + " " + "rdfs:label" +
             " 'NAVISone Maritime Thesaurus' .")
lines.append("nomt:" + "cs01" + " " +
             "dct:identifier" + " wd:Q115264680" + " .")
lines.append("wd:Q115264680 rdfs:label 'NAVIS.one Ship Database'@en .")
lines.append("nomt:" + "cs01" + " " +
             "dct:publisher" + " wd:Q115264627" + " .")
lines.append(
    "wd:Q115264627 rdfs:label 'Department of Research Software Engineering at LEIZA '@en .")
lines.append("nomt:" + "cs01" + " " +
             "dct:creator" + " wd:Q66606154" + " .")
lines.append("wd:Q66606154 rdfs:label 'Florian Thiery M.Sc.'@en .")
lines.append("nomt:" + "cs01" + " " +
             "dct:creator" + " wd:Q88865971" + " .")
lines.append("wd:Q88865971 rdfs:label 'Dr. Allard Wijnand Mees FSA'@en .")
lines.append("nomt:" + "cs01" + " " + "dct:date" + " '2022-11-18' .")
lines.append("nomt:" + "cs01" + " " + "dct:created" + " '2022-11-18' .")
lines.append("nomt:" + "cs01" + " " + "dct:modified '" +
             datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "'^^xsd:dateTime .")
lines.append("")

# add parent items
for index, row in data.iterrows():
    # print(lineNo)
    tmpno = lineNo - 2
    if tmpno % 50 == 0:
        print(tmpno)
    lineNo += 1
    thisid = int(str(row['id'])) + 1000
    lines.append("nomt:" + str(thisid) + " " + "rdf:type" + " skos:Concept .")
    lines.append("nomt:" + "cs01" + " " + "skos:hasTopConcept " +
                 "nomt:" + str(thisid) + " .")
    lines.append("nomt:" + str(thisid) + " " +
                 "skos:inScheme" + " nomt:cs01 .")
    lines.append("nomt:" + str(thisid) + " " +
                 "skos:topConceptOf" + " nomt:cs01 .")
    lines.append("nomt:" + str(thisid) + " " + "skos:note" +
                 " 'This is a parent Concept of NAVIS I or NAVIS II and now NAVISone.'@en .")
    # metadata
    lines.append("nomt:" + str(thisid) + " " + "cc:license" + " <" +
                 "http://creativecommons.org/licenses/by-sa/4.0/" + "> .")
    lines.append("nomt:" + str(thisid) + " " +
                 "cc:attributionURL" + " wd:Q115264627" + " .")
    lines.append("nomt:" + str(thisid) + " " + "cc:attributionName" + " '" +
                 "Arbeitsbereich Wissenschaftliche IT, Digitale Plattformen und Tools des LEIZA" + "' .")
    lines.append("nomt:" + str(thisid) + " " +
                 "dct:publisher" + " wd:Q115264627" + " .")
    lines.append("nomt:" + str(thisid) + " " +
                 "dct:identifier" + " nomt:" + str(thisid) + " .")
    lines.append("nomt:" + str(thisid) + " " + "dct:issued '" +
                 datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "'^^xsd:dateTime .")
    lines.append("nomt:" + str(thisid) + " " + "dct:modified '" +
                 datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "'^^xsd:dateTime .")
    lines.append("nomt:" + str(thisid) + " " +
                 "dct:created" + " '2022-11-18' .")
    # item
    if str(row['de']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['de']).replace('\'', '`') + "'@de .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['de']).replace('\'', '`') + "'@de .")
    if str(row['en']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['en']).replace('\'', '`') + "'@en .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['en']).replace('\'', '`') + "'@en .")
    if str(row['dk']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['dk']).replace('\'', '`') + "'@dk .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['dk']).replace('\'', '`') + "'@dk .")
    if str(row['nl']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['nl']).replace('\'', '`') + "'@nl .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['nl']).replace('\'', '`') + "'@nl .")
    if str(row['fr']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['fr']).replace('\'', '`') + "'@fr .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['fr']).replace('\'', '`') + "'@fr .")
    if str(row['it']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['it']).replace('\'', '`') + "'@it .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['it']).replace('\'', '`') + "'@it .")
    if str(row['es']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['es']).replace('\'', '`') + "'@es .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['es']).replace('\'', '`') + "'@es .")
    if str(row['pl']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['pl']).replace('\'', '`') + "'@pl .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['pl']).replace('\'', '`') + "'@pl .")
    if str(row['gr']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['gr']).replace('\'', '`') + "'@gr .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['gr']).replace('\'', '`') + "'@gr .")
    if str(row['he']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['he']).replace('\'', '`') + "'@he .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['he']).replace('\'', '`') + "'@he .")
    # prov-o
    lines.append("nomt:" + str(thisid) + " " +
                 "prov:wasAttributedTo" + " nomt:ImportPythonScript .")
    lines.append("nomt:" + str(thisid) + " " +
                 "prov:wasDerivedFrom" + " wd:Q115264680" + " .")
    lines.append("nomt:" + str(thisid) + " " +
                 "prov:wasGeneratedBy" + " nomt:activity_" + str(thisid) + " .")
    lines.append("nomt:activity_" + str(thisid) +
                 " " + "rdf:type" + " prov:Activity .")
    lines.append("nomt:activity_" + str(thisid) + " " +
                 "prov:startedAtTime '" + starttime + "'^^xsd:dateTime .")
    lines.append("nomt:activity_" + str(thisid) + " " + "prov:endedAtTime '" +
                 datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "'^^xsd:dateTime .")
    lines.append("nomt:activity_" + str(thisid) + " " +
                 "prov:wasAssociatedWith" + " nomt:ImportPythonScript .")
    lines.append("")

# read csv file
data2 = pd.read_csv(
    file_in2,
    encoding='utf-8',
    sep=',',
    usecols=['id', 'navisid', 'de', 'en', 'dk', 'nl', 'fr', 'it', 'es', 'pl', 'gr', 'he', 'desc_en', 'desc_de',
             'origindesc', 'fk_id_parent', 'gettyaat', 'gettyaatrelationtype', 'wikidata', 'wikidatarelationtype']
)
print(data2.info())

# add parent items
for index, row in data2.iterrows():
    # print(lineNo)
    tmpno = lineNo - 2
    if tmpno % 50 == 0:
        print(tmpno)
    lineNo += 1
    thisid = str(row['id'])
    fkid = int(str(row['fk_id_parent'])) + 1000
    lines.append("nomt:" + str(thisid) + " " + "rdf:type" + " skos:Concept .")
    lines.append("nomt:" + str(thisid) + " " + "rdf:type" + " rdfs:Class .")
    lines.append("nomt:" + str(fkid) + " " + "skos:narrower " +
                 "nomt:" + str(thisid) + " .")
    lines.append("nomt:" + str(thisid) + " " +
                 "skos:broader " + "nomt:" + str(fkid) + " .")
    lines.append("nomt:" + str(fkid) + " " +
                 "rdfs:subClassOf " + "nomt:" + str(thisid) + " .")
    lines.append("nomt:" + str(thisid) + " " +
                 "skos:inScheme" + " nomt:cs01 .")
    lines.append("nomt:" + str(thisid) + " " + "skos:note" +
                 " 'This is a Concept of NAVIS I or NAVIS II and now NAVISone.'@en .")
    lines.append("nomt:" + str(thisid) + " " + "lado:identifier_db '" +
                 str(row['navisid']).replace('\'', '`') + "' .")
    lines.append("nomt:" + str(thisid) + " " + "lado:origin_description '" +
                 str(row['origindesc']).replace('\'', '`') + "' .")
    # metadata
    lines.append("nomt:" + str(thisid) + " " + "cc:license" + " <" +
                 "http://creativecommons.org/licenses/by-sa/4.0/" + "> .")
    lines.append("nomt:" + str(thisid) + " " +
                 "cc:attributionURL" + " wd:Q115264627" + " .")
    lines.append("nomt:" + str(thisid) + " " + "cc:attributionName" + " '" +
                 "Arbeitsbereich Wissenschaftliche IT, Digitale Plattformen und Tools des LEIZA" + "' .")
    lines.append("nomt:" + str(thisid) + " " +
                 "dct:publisher" + " wd:Q115264627" + " .")

    lines.append("nomt:" + str(thisid) + " " +
                 "dct:identifier" + " nomt:" + str(thisid) + " .")
    lines.append("nomt:" + str(thisid) + " " + "dct:issued '" +
                 datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "'^^xsd:dateTime .")
    lines.append("nomt:" + str(thisid) + " " + "dct:modified '" +
                 datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "'^^xsd:dateTime .")
    lines.append("nomt:" + str(thisid) + " " +
                 "dct:created" + " '2022-11-18' .")
    # item
    if str(row['de']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['de']).replace('\'', '`') + "'@de .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['de']).replace('\'', '`') + "'@de .")
    if str(row['en']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['en']).replace('\'', '`') + "'@en .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['en']).replace('\'', '`') + "'@en .")
    if str(row['dk']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['dk']).replace('\'', '`') + "'@dk .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['dk']).replace('\'', '`') + "'@dk .")
    if str(row['nl']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['nl']).replace('\'', '`') + "'@nl .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['nl']).replace('\'', '`') + "'@nl .")
    if str(row['fr']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['fr']).replace('\'', '`') + "'@fr .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['fr']).replace('\'', '`') + "'@fr .")
    if str(row['it']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['it']).replace('\'', '`') + "'@it .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['it']).replace('\'', '`') + "'@it .")
    if str(row['es']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['es']).replace('\'', '`') + "'@es .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['es']).replace('\'', '`') + "'@es .")
    if str(row['pl']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['pl']).replace('\'', '`') + "'@pl .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['pl']).replace('\'', '`') + "'@pl .")
    if str(row['gr']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['gr']).replace('\'', '`') + "'@gr .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['gr']).replace('\'', '`') + "'@gr .")
    if str(row['he']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:prefLabel '" +
                     str(row['he']).replace('\'', '`') + "'@he .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:label '" +
                     str(row['he']).replace('\'', '`') + "'@he .")
    # descriptions
    if str(row['desc_en']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:scopeNote" + " '" +
                     str(row['desc_en']).replace('\'', '`') + "'@en .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:comment" + " '" +
                     str(row['desc_en']).replace('\'', '`') + "'@en .")
    if str(row['desc_de']) != 'nan':
        lines.append("nomt:" + str(thisid) + " " + "skos:scopeNote" + " '" +
                     str(row['desc_de']).replace('\'', '`') + "'@de .")
        lines.append("nomt:" + str(thisid) + " " + "rdfs:comment" + " '" +
                     str(row['desc_de']).replace('\'', '`') + "'@de .")
    # matches
    if str(row['gettyaat']) != 'nan':
        if str(row['gettyaatrelationtype']) != 'nan':
            lines.append("nomt:" + str(thisid) + " " + str(row['gettyaatrelationtype']) + " " +
                         "aat:" + str(int(row['gettyaat'])) + " .")
            lines.append("nomt:" + str(thisid) + " " + "lado:gettyaatMatch" + " " +
                         "aat:" + str(int(row['gettyaat'])) + " .")
    if str(row['wikidata']) != 'nan':
        if str(row['wikidatarelationtype']) != 'nan':
            lines.append("nomt:" + str(thisid) + " " + str(row['wikidatarelationtype']) + " " +
                         "wd:" + str(row['wikidata']) + " .")
            lines.append("nomt:" + str(thisid) + " " + "lado:wikidataMatch" + " " +
                         "wd:" + str(row['wikidata']) + " .")
    # prov-o
    lines.append("nomt:" + str(thisid) + " " +
                 "prov:wasAttributedTo" + " nomt:ImportPythonScript .")
    lines.append("nomt:" + str(thisid) + " " +
                 "prov:wasDerivedFrom" + " wd:Q115264680" + " .")
    lines.append("nomt:" + str(thisid) + " " +
                 "prov:wasGeneratedBy" + " nomt:activity_" + str(thisid) + " .")
    lines.append("nomt:activity_" + str(thisid) + " " +
                 "rdf:type" + " <http://www.w3.org/ns/prov#Activity> .")
    lines.append("nomt:activity_" + str(thisid) + " " +
                 "prov:startedAtTime '" + starttime + "'^^xsd:dateTime .")
    lines.append("nomt:activity_" + str(thisid) + " " + "prov:endedAtTime '" +
                 datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "'^^xsd:dateTime .")
    lines.append("nomt:activity_" + str(thisid) + " " +
                 "prov:wasAssociatedWith" + " nomt:ImportPythonScript .")
    lines.append("")

#####################

files = (len(lines) / 100000) + 1
print("lines", len(lines), "files", int(files))

# set output path
dir_path = os.path.dirname(os.path.realpath(__file__))

# write output files
print("start writing turtle files...")

f = 0
step = 100000
filename = "navisone_maritime_thesaurus.ttl"
prefixes = ""
prefixes += "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\r\n"
prefixes += "@prefix owl: <http://www.w3.org/2002/07/owl#> .\r\n"
prefixes += "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\r\n"
prefixes += "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\r\n"
prefixes += "@prefix dc: <http://purl.org/dc/elements/1.1/> .\r\n"
prefixes += "@prefix dct: <http://purl.org/dc/terms/> .\r\n"
prefixes += "@prefix prov: <http://www.w3.org/ns/prov#> .\r\n"
prefixes += "@prefix lado: <http://archaeology.link/ontology#> .\r\n"
prefixes += "@prefix nomt: <http://data.archaeology.link/data/maritimethesaurus/> .\r\n"
prefixes += "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\r\n"
prefixes += "@prefix wd: <http://www.wikidata.org/entity/> .\r\n"
prefixes += "@prefix cc: <http://creativecommons.org/ns#> .\r\n"
prefixes += "@prefix aat: <http://vocab.getty.edu/aat/> .\r\n"
prefixes += "\r\n"

for x in range(1, int(files) + 1):
    strX = str(x)
    filename = dir_path.replace("\\py", "\\data") + "\\" + filename
    file = codecs.open(filename, "w", "utf-8")
    file.write("# create triples from " + csv + " and " + csv2 + " \r\n")
    file.write(
        "# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
    file.write(prefixes)
    i = f
    for i, line in enumerate(lines):
        if (i > f - 1 and i < f + step):
            file.write(line)
            file.write("\r\n")
    f = f + step
    print("Yuhu! > " + filename)
    file.close()

print("*****************************************")
print("SUCCESS")
print("closing script")
print("*****************************************")
