# -*- coding: utf-8 -*-
"""Task08.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lmKehNWcRnyn4BkC__0xl--55iIpWSjD

**Task 08: Completing missing data**
"""

#!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"/rdf/data01.rdf", format="xml")
g2.parse(github_storage+"/rdf/data02.rdf", format="xml")

"""Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas."""

for s, p, o in g1:
  print(s, p, o)

for s, p, o in g2:
  print(s, p, o)

from rdflib.plugins.sparql import prepareQuery

syntax = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
data = Namespace('http://data.org#')
vcar = Namespace(' http://www.w3.org/2001/vcard-rdf/3.0#')

q1 = prepareQuery('''
  SELECT ?person WHERE{
    ?person syntax:type data:Person
  }
  ''',
    initNs = { 'syntax': syntax, 'data': data, 'vcar':vcar}
)
for r in g1.query(q1):
  print(r.person)

#Añadimos los nombres y apellidos

vcar = Namespace('http://www.w3.org/2001/vcard-rdf/3.0#')
Sara = Literal('Sara')
Jones = Literal('Jones')
John = Literal('John')
Smith = Literal('Smith')

g1.add((data.SaraJones, vcar.Given, Sara))
g1.add((data.SaraJones, vcar.Family, Jones))
g1.add((data.JohnSmith, vcar.Given, John))
g1.add((data.JonesSmith, vcar.Family, Smith))

#Vemos los resultados
for s, p , o in g1:
  print(s, p, o)

#Vemos quienes tienen correo

q2 = prepareQuery('''
  SELECT ?person ?email WHERE{
    ?person syntax:type data:Person.
    ?person vcar:EMAIL ?email
  }
  ''',
    initNs = { 'syntax': syntax, 'data': data, 'vcar':vcar}
)
for r in g1.query(q2):
  print(r.person, r.email)

#Añadimos un correo a aquellos que no tienen

correo_SaraJones = URIRef('s.jones@data.org')
correo_HarryPotter = URIRef('h.potter@data.org')
g1.add((data.SaraJones, vcar.EMAIL, correo_SaraJones))
g1.add((data.HarryPotter, vcar.EMAIL, correo_HarryPotter))

#Vamos los resultados

for s, p , o in g1:
  print(s, p, o)