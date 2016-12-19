from SPARQLWrapper import SPARQLWrapper, JSON

def link(word):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?uri
        WHERE {
          ?uri rdfs:label ?label .
          ?label bif:contains '""" + word + """' .
        }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    return results["results"]["bindings"][0]["uri"]["value"]
