"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

with open('example5.rdf', 'r') as file:
    # Create a Graph
    g = Graph()
    g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
    g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
    g.parse(file, format="xml")

"""Create a new class named Researcher"""

print("Creating a class named 'Researcher'")
ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
    print(s, p, o)
print()

"""**TASK 6.1: Create a new class named "University"**"""
print("Creating a class named 'University'")
g.add((ns.University, RDF.type, RDFS.Class))

# Visualize the results
for s, p, o in g:
    print(s, p, o)
print()

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

print("Adding class 'Researcher' as a subclass of 'Person'")
# A researcher is a person
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))

# Visualize the results
for s, p, o in g:
    print(s, p, o)
print()

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

print("Creating an individual of the class 'Researcher' named 'Jane Smith'")
# Jane Smith is a researcher
g.add((ns.JaneSmith, RDF.type, ns.Researcher))

# Visualize the results
for s, p, o in g:
    print(s, p, o)
print()

"""**TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**"""

print("Adding properties to the individual 'Jane Smith'")
# TO DO
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")
# Jane's fullname is Jane Smith
g.add((ns.JaneSmith, vcard.FN, Literal("Jane Smith")))
# Jane Smith's given name is Jane
g.add((ns.JaneSmith, vcard.Given, Literal("Jane")))
# Jane's family name is Smith
g.add((ns.JaneSmith, vcard.Family, Literal("Smith")))

# Visualize the results
for s, p, o in g:
    print(s, p, o)
print()

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

print("Adding 'UPM' as the university where John Smith works")
# UPM is a university
g.add((ns.UPM, RDF.type, ns.University))

# John Smith works for UPM
g.add((ns.JohnSmith, ns.worksAt, ns.UPM))

# Visualize the results
for s, p, o in g:
    print(s, p, o)
