"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""
from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery

with open('example6.rdf', 'r') as file:
    # Create a Graph
    g = Graph()
    g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
    g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
    g.parse(file, format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

print("TASK 7.1: List all subclasses of 'Person' with RDFLib and SPARQL")
# WITH RDFLib
print("With RDFLib:")
ns = Namespace("http://somewhere#")
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    print(s)

# WITH SPARQL
print()
print("With SPARQL:")
q1 = """
PREFIX ns: <http://somewhere#>
PREFIX vcard: <http://www.w3.org/2001/vcard-rdf/3.0/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?subclasses
WHERE {
    ?subclasses rdfs:subClassOf ns:Person
}"""

# Visualize the results
for r in g.query(q1):
    print(r)
print()

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**"""

print("TASK 7.2: List all individuals of 'Person' with RDFLib and SPARQL (remember the subClasses)")
# WITH RDFLib
print("With RDFLib:")
# Search for individuals
for s, p, o in g.triples((None, RDF.type, ns.Person)):
    print(s)
# Search for subclasses of Person
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    # Individuals of the subclasses found
    for s2, p2, o2, in g.triples((None, RDF.type, s)):
        print(s2)

# WITH SPARQL
print()
print("With SPARQL:")
q2 = prepareQuery(
    """SELECT DISTINCT ?name
    WHERE {
      ?name rdf:type ?subclass .
      ?subclass rdfs:subClassOf* ns:Person
    }""",
    initNs={"ns": ns, "rdf": RDF, "rdfs": RDFS})

# Visualize the results
for r in g.query(q2):
    print(r)
print()

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
"""

print("TASK 7.3: List all individuals of 'Person' and all their properties including their class with RDFLib and "
      "SPARQL")
# WITH RDFLib
print("With RDFLib:")
# Search for individuals
for s, p, o in g.triples((None, RDF.type, ns.Person)):
    # Properties and its values of the individuals
    for s2, p2, o2 in g.triples((s, None, None)):
        print(s2, p2, o2)
# Search for subclasses of Person
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    # Individuals of the subclasses found
    for s2, p2, o2 in g.triples((None, RDF.type, s)):
        # Properties and its values of the individuals
        for s3, p3, o3 in g.triples((s2, None, None)):
            print(s3, p3, o3)

# WITH SPARQL
print()
print("With SPARQL:")
q3 = prepareQuery(
    """SELECT DISTINCT ?name ?property ?value
    WHERE {
      ?name rdf:type ?subclass .
      ?subclass rdfs:subClassOf* ns:Person .
      ?name ?property ?value
    }""",
    initNs={"ns": ns, "rdf": RDF, "rdfs": RDFS})

# Visualize the results
for r in g.query(q3):
    print(r)
