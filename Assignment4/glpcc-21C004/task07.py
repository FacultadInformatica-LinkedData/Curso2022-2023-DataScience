
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

ns = Namespace("http://somewhere#")
for s, p, o in g.triples((None,RDFS.subClassOf,ns.Person)):
  print(s)

q1 = 'SELECT ?x WHERE {?x RDFS:subClassOf ns:Person}'
for r in g.query(q1,initNs={'ns':ns,'RDFS':RDFS}):
 print(r.x)

for person,p,o in g.triples((None,RDF.type,ns.Person)):
  print(person)
for subclass, p, o in g.triples((None,RDFS.subClassOf,ns.Person)):
  for person,t,s in g.triples((None,RDF.type,subclass)):
    print(person)

q1 = 'SELECT ?x WHERE {?class RDFS:subClassOf* ns:Person. ?x RDF:type ?class}'
for r in g.query(q1,initNs={'ns':ns,'RDFS':RDFS,'RDF':RDF}):
 print(r.x)

individuals = []
for person,p,o in g.triples((None,RDF.type,ns.Person)):
    individuals.append(person)
for subclass, p, o in g.triples((None,RDFS.subClassOf,ns.Person)):
  for person,t,s in g.triples((None,RDF.type,subclass)):
    individuals.append(person)

for person in individuals:
    print(f'Individual:{person}\n Properties:')
    for s,p,o in g.triples((person,None,None)):
        print(p,o)
        
q1 = 'SELECT ?x ?prop ?y WHERE {?x RDF:type ns:Person. ?x ?prop ?y}'
individuals = set()
for r in g.query(q1,initNs={'ns':ns,'RDF':RDF}):
    if r.x not in individuals:
        print(f'Individual:{r.x}')
        individuals.add(r.x)
        print('Properties:')
    print(f'{r.prop}:{r.y}')


