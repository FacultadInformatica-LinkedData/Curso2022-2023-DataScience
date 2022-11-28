# LIMPIEZA DE DATOS

Empezamos este proyecto con la extracción de datos de diferentes fuentes; con un total de **7 csv**.
Para la limpieza de datos hemos ido atravesando distintas fases hasta llegar a los 3 CSVs finales.

* Primero limpiamos **individualmente** cada csv de los 6 relacionados con instancias de contenedores de
forma que podamos unificar todos en uno que llamaremos *Contenedores.csv*.
Los Json usados para modificar cada csv tienen el nombre en forma de **history+Nombrecsvoriginal**.

* Aplicamos desde OpenRefine las modificaciones pertinentes a las columnas del nuevo archivo en el que
hemos juntado todos los anteriores; **localizando duplicados** y **unificando los nombres**. 

* A continuación, nos pareció interesante agregar la opción de filtrar en función del **código postal** por 
lo que agregamos una nueva columna. No encontramos ninguna API capaz de facilitarnos la información
deseada en función de las coordenadas UTM (que son las que tenemos) por lo que recurrimos a **python**, 
dónde desarrollaríamos un script capaz de llevar a cabo esta tarea y modificaríamos nuestro csv.

* Una vez unificados todos los datos de los contenedores en uno solo, decidimos crear un nuevo csv (*Ubicacion.csv*)
con las propiedades de la ubicación para un mejor tratamiento de los datos. Limpiaremos este nuevo csv y cada
elemento tendrá su propio ID que corresponde al objeto de la columna ubicación en el csv principal.

* Por último, trataríamos el csv referente al **tipo de residuos** donde tras una serie de transformaciones en
OpenRefine conseguiríamos estructurar los datos de forma útil para nuestros intereses.

Tras todo este proceso hemos generado todos los json documentando cada modificación en openrefine además de dos
scripts de python y los 3 CSVs resultantes de todo el proceso: Contenedores.csv, Ubicacion.csv y Residuos.csv