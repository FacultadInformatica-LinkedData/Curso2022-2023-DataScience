1
    Analysis
    Ontology
        - No hace falta que defináis namespaces distintos para las entidades de cada fichero en la ontología.
        - Es más, esto os está dando problemas, pues tenéis términos definidos en ambos namespaces.
        -No hay ontología en:  http://www.contextus.net/ontology/ontomedia/misc/date#. Podéis usar la OWL Time ontology para describir información temporal.
        - Corregir "Adress" -> "Address"
        - Los códigos (ej. de distrito) no son números.
        - Los números de calle no son números.
        - Los nombres de las clases deberían empezar por mayúsculas.
        - En OWL, múltiples dominios (o rangos) implican la intersección de todo lo que aparece, no la unión. Con lo que cuando lo estáis usando es incorrecto.
    RDF data
        - Hay valores que no tienen el tipo de datos.
        - Las URIs no son strings.
        - Revisad la codificación del texto (ej. "Arg&amp;uuml;elles").
