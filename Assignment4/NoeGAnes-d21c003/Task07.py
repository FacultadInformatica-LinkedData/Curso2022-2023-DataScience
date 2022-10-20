#Task 07: Querying RDF(s)
#!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

#TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL
#RDFLib
ns= Namespace("http://somewhere#")
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s)
  
#SPARQL
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
from rdflib.plugins.sparql import prepareQuery
q1 = prepareQuery('''
  SELECT 
    ?Subject
  WHERE { 
    ?Subject rdfs:subClassOf ns:Person. 
  }
  ''',
  initNs = { "rdfs":RDFS , "ns":ns}
)
for r in g.query(q1):
  print(r)


#TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)
#RDFLib
for s, p, o in g.triples((None, RDF.type, ns.Person)):
  print(s)
  
#SPARQL
q2 = prepareQuery('''
  SELECT 
    ?Subject
  WHERE { 
    ?Subject rdf:type ns:Person. 
  }
  ''',
  initNs = { "rdfs":RDFS , "ns":ns}
)
for r in g.query(q2):
  print(r)
  

#TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL
#RDFLib
for s1, p1, o1 in g.triples((None, RDF.type, ns.Person)):
  for s1,p2,o2 in g.triples((s1, None, None)):
    print(p2,o2)
    
#SPARQL
q3 = prepareQuery('''
  SELECT 
    ?Property ?Object 
  WHERE { 
    ?Subject rdf:type ?Person. 
    ?Subject ?Property ?Object.
  }
  ''',
  initNs = { "rdfs":RDFS, "ns":ns}
)
for r in g.query(q3):
  print(r)
