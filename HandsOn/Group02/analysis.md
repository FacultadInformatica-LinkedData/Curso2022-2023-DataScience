Analysis of the datasets
=======

First of all, we did an initial survey of the data in Excel, looking again at the structure of the different datasets and the information we wanted to extract from them. Along with this, we review the information about the content of the dataset provided on the web page from which we extracted the data. This gave us a general notion of the main classes that would define the ontology and encompass the other classes and instances. We have three datasets:

* Dataset about parks and gardens in Madrid. We intend to extract those parks and gardens that have sports facilities or that, due to their characteristics, are ideal for practicing a sport. For example, a botanical garden can be ideal for jogging while enjoying the views, a large park can be used for running, etc. The types of parks and gardens that are defined within the dataset are:
  
  * Parques y jardines
  
  * Colecciones botánicas
  
  * Parques forestales
  
  * Parques históricos

* Dataset about sports centers in Madrid. Includes information about:
  
  * Agrupaciones deportivas
  
  * Campos de golf
  
  * Clubs deportivos
  
  * Centros Deportivos Municipales
  
  * Centros de tecnificación

* Dataset about sports facilities in Madrid. Although it may seem similar to the previous one, this includes those sports spaces that are made up of a sports unit or units and are not covered by any sports center. That is, they are basic facilities that are usually free to use.

* Dataset about quiet streets of Madrid. Streets that can be traveled by bicycle due to its low traffic and other characteristics that make it safer and ideal for cycling. The user can get an idea of ​​the appropriate street network if he plans to take a route or has to take a bike trip.

Central to our project and something that the first three datasets have in common are sports facilities. Both parks and gardens, sports facilities and sports centers have in common that they include or are sports facilities. It seemed ideal to us to first define an entity called Sports Space, which would encompass the possible classes of spaces where sports can be performed. Thus, a sports space can be:

* A basic sports facility (not included within a sports center). Within it there may be one or more sports units (for example, several soccer fields and a skating rink, or simply a basketball court).

* A sports center, within which there are sports facilities.

* The parks and gardens, within which there are sports facilities.

For a more detailed analysis of the information and to be able to delve deeper into the ontology, we have used OpenRefine as support to detect the entities. Selecting facet >> text facet in the column that interested us, we browsed the main classes or types of the dataset. In all the datasets that we have selected, there is a column called "Type", which categorizes the type of park, garden, facility, etc. For example, in the Parks and Gardens dataset, doing facet >> text facet in the "Type" column we see the following information:

/contenido/entidadesYorganismos/ParquesJardines

/contenido/entidadesYorganismos/ParquesJardines/ColeccionesBotanicas

/contenido/entidadesYorganismos/ParquesJardines/ParquesForestales

/contenido/entidadesYorganismos/ParquesJardines/ParquesHistoricos

In this particular case, it has been very useful to us because this information was not in the description of the data on the web page.

Thus, we had EspaciosDeporte as a superclass, within which there are basic sports facilities, sports centers and parks. These with their corresponding subclasses.

Another very positive aspect of the data is that they all have information about their location, which is why we have also included them in the graph as entities.

License
=======

Righstholder: The rightsholder is the Madrid City Council.

Publisher: The publisher of the data is the Open Data Portal of the Madrid City Council.

License: According to the [Portal de Datos abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/portal/site/egob/menuitem.3efdb29b813ad8241e830cc2a8a409a0/?vgnextoid=8742d660ccb62610VgnVCM1000001d4a900aRCRD&vgnextchannel=b4c412b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default), "...these conditions allow the reuse of open documents and data from the catalog and library loans submitted to them for commercial and non-commercial purposes." There are a series of conditions for its use:

1.- It is forbidden to distort the meaning of the information.

2.- The source of the documents subject to reuse must be cited. This appointment may be made as follows: "Data source: Community of Madrid and Madrid City Council

3.- The date of the last update of the documents subject to reuse must be mentioned, as long as it was included in the original document.

4.- It may not be indicated, insinuated or suggested that the Community of Madrid and the Madrid City Council participate, sponsor or support the reuse that is carried out with the information.

5.- The metadata on the update date and the applicable reuse conditions included, where appropriate, in the document made available for reuse must be kept, not altered or deleted.

6.- In the case of anonymized information for the protection of personal data or other reasons, it is expressly prohibited to carry out work to re-identify people based on these data and other possible, past, current or future sources of data and information.

We will use the same class of license in all the datasets that we generate.

Resource Naming Strategy
===============

To name the elements we have decided to follow the following structure.

* The domain chosen for the URIs is the following http://DeportesMadridGroup2.es, which we have verified is not in use

* Instances of any class in the ontology have the URI in the form http://DeportesMadridGroup2.es/Espacios/instances/{instance_id}

* The ontology classes will have the URI in the form http://DeportesMadridGroup2.es/Espacios/ontology/{class_name}

* In the case of street instances, the name of the street will appear in camelCase in its URI.

* For instances of sports space subclasses, their URI is that of any instance followed by a unique ID that appears in the data obtained, named PK which we ensured is unique for all the instances in the csv files.

* Finally, for instances of other classes such as Localizacion,Direccion,Barrio,etc... a Location/XX style naming will be followed, where XX is the unique ID of the instance it will be reference to, i.e, its PK.