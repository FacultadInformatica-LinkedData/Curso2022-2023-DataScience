## Análisis de los datos

Primeramente hicimos un sondeo inicial de los datos en Excel, viendo de nuevo un poco la estructura de los diferentes datasets y la información que queríamos extraer de estos. Junto con esto, revisamos la información acerca del contenido del dataset provista en la página web de donde extaímos los datos. Esto nos dio una noción general de las principales clases que definirian la ontología y englobarían a las otras clases e instancias.
Disponemos de tres datasets:

* Dataset acerca de parques y jardines de Madrid. Pretendemos extraer aquellos parques y jardines que dispongan de instalaciones deportivas o que por sus características sean ideales para practicar algún deporte. Por ejemplo, un jardín botánico puede ser ideal para hacer footing mientras disfrutas de las vistas, un parque amplio puede servir para correr, etc. Los tipos de parques y jardines que se definen dentro del dataset son:
  
  * Parques y jardines
  
  * Colecciones botánicas
  
  * Parques forestales
  
  * Parques históricos

* Dataset acerca de centros deportivos de Madrid. Incluye información acerca de:
  
  * Agrupaciones deportivas
  
  * Campos de golf
  
  * Clubs deportivos
  
  * Centros Deportivos Municipales
  
  * Centros de tecnificación

* Dataset acerca de instalaciones deportivas de Madrid. Aunque puede parecer similar al anterior, este recoge aquellos espacios deportivos que están constituidos por una unidad o unidades deportivas y no están recogidos por ningún centro deportivo. Es decir, son instalaciones básicas que suelen ser de uso libre.

* Dataset acerca de calles tranquilas de Madrid. Calles por las que se puede transitar en bicicleta por su bajo tráfico y otras características que lo hacen más seguro e ideal para practicar ciclismo. El usuario puede tener una idea de la red de calles adecuadas si planea hacer una ruta o tiene que hacer un trayecto en bici.

Lo central para nuestro proyecto y algo que tienen en común los tres primeros datasets son las instalaciones deportivas. Tanto los parques y jardines, como las instalaciones deportivas y los centros deportivos tienen en común que incluyen o son instalaciones deportivas. Nos pareció ideal definir primeramente una entidad llamada Espacio Deportivo, que englobaría las posibles clases de espacios donde realizar deporte, así, un espacio deportivo puede ser:

* Una instalación deportiva básica (no incluida dentro de un centro deportivo). Dentro de la misma puede haber una o varias unidades deportivas (por ejemplo, varias pistas de fútbol y un patinódromo, o simplemente constar de una pista de baloncesto).

* Un centro deportivo, dentro de los cuales hay instalaciones deportivas.

* Los parques y jardines, dentro de los cuales hay instalaciones deportivas.

Para un análisis más detallado de la información y para poder profundizar más en la ontología, hemos usado OpenRefine como apoyo para detectar las entidades. Seleccionando facet >> text facet en la columna que nos interesaba ojeabamos las clases o tipos principales que del dataset. 

En todos los datasets que hemos seleccionado, hay una columna llamada "Tipo", la cual categoriza el tipo de parque, jardin, instalación, etc. Por ejemplo, en el dataset Parques y Jardines, haciendo facet >> text facet en la columna "Tipo" vemos las siguiente información:

/contenido/entidadesYorganismos/ParquesJardines

/contenido/entidadesYorganismos/ParquesJardines/ColeccionesBotanicas

/contenido/entidadesYorganismos/ParquesJardines/ParquesForestales

/contenido/entidadesYorganismos/ParquesJardines/ParquesHistoricos

En este caso particular, nos ha sido muy útil porque está información no estaba en la descripción de los datos de la página web. 

Así teníamos como superclase el Espacio deportivo, dentro del cual hay instalaciones deportivas básicas, centros deportivos y parques. Estos con sus correspondientes subclases. 

Otro aspecto muy positivo de los datos es que todos ellos tienen información acerca de su localización, por lo que también lo hemos incluido en el grafo como entidades.

## Licencia

La Comunidad de Madrid publicó estos datos Bajo una [licencia abierta](https://datos.madrid.es/portal/site/egob/menuitem.3efdb29b813ad8241e830cc2a8a409a0/?vgnextoid=8742d660ccb62610VgnVCM1000001d4a900aRCRD&vgnextchannel=b4c412b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default), que permite el uso de los datos libremente siempre que se cite a la comunidad y se cumplan algunas normas explicadas más en detalle en el link a la licencia.

## Estrategia para el nombramiento de los recursos.

Para nombrar los elementos hemos decidido seguir la siguiente estructura.

* El dominio elegido para las URIs es el siguiente http://DeportesMadridGroup2.es, que hemos comprobado que no esta en uso

* Las instancias de cualquier clase en la ontologia tienen el URI con la forma http://DeportesMadridGroup2.es/Espacios/ontology/#

* Las clases de la ontologia tendran el URI de la forma http://DeportesMadridGroup2.es/Espacios/ontology/#

* En el caso de las instancias de calle en su URI aparecera el nombre de la calle en camelCase.

* Para las instancias de subclases de espacio deportivo, su URI es la de cualquier instancia seguida de un ID unico que aparece en los datos obtenidos.

* Finalmente para instancias de otras clases como Localización o Dirección se seguira un nombramiento del estilo LocalizaciónXX siendo XX un ID unico que se asignará incrementalmente




