# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E55W-V-zPge7Bj-wF55tmypQXLeOlU1w

**Task 07: Querying RDF(s)**
"""

#!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

#OPTION1: RDFLib
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s, p, o)


#OPTION2: SPARQL
q1 = prepareQuery('''
  SELECT DISTINCT ?subclasses
  WHERE 
  { 
    ?subclasses  rdfs:subClassOf/rdfs:subClassOf*  ns:Person. 
  }
  ''', initNs = { "ns": ns,"rdfs":RDFS}
)

for i in g.query(q1):
  print(i)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

#OPTION1: RDFLib
for s,p,o in g.triples((None, RDF.type, ns.Person)):
  print(s)

for subClasses,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s,p,o in g.triples((None, RDF.type, subClasses)):
    print(s)

#OPTION2: SPARQL

q2 = prepareQuery('''
SELECT DISTINCT ?individuals 
WHERE 
{
  ?individuals rdf:type/rdfs:subClassOf* ns:Person
}
''',
initNs = {"ns": ns}
)

for i in g.query(q2):
  print(i)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

#OPTION1: RDFLib
for s,p,o in g.triples((None, RDF.type, ns.Person)):
  for s2,p2,o2 in g.triples((s,None,None)):
    print(s2,p2,o2)

for subClasses,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s,p,o in g.triples((None, RDF.type, subClasses)):
    for s2,p2,o2 in g.triples((s,None,None)):
      print(s2,p2,o2)

#OPTION2: SPARQL

q3 = prepareQuery('''
  SELECT DISTINCT ?s ?p ?o
  WHERE 
  {
      ?subclasses rdfs:subClassOf* ns:Person.
      ?s rdf:type ?subclasses.
      ?s ?p ?o
  }
  ''',
  initNs = {"ns":ns}
)

for i in g.query(q3):
  print(i)
