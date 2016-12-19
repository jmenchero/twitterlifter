# Twitter Lifter API
## What is it?
It is both a collaborative project and a service for developers.
This API is based on the RDF triples concept (Subject Predicate
Object), translating the same grammatical syntax from the natural
language into URIs and RDF tags readable by the machine.
## How to use it
You just have to make a HTTP request to the next IP with the id
from the tweet you want to analyze, and process the RDF in JSON
format it returns:
>>> http://193.70.1.232:5000/<TWEET-ID>

You can test it with the demo tweets we have posted in the project's
Twitter account:
>>> https://twitter.com/SemanticAPI/with_replies

I.E: Open the following link with your browser:
>>> http://193.70.1.232:5000/810733932740308994

## TO-DOs
- Nouns with multiple words.
- Biography + previous tweets consideration for a better word
linking.
- Use a bigger lexicon with a CCG (Combinatory Categorial Grammar)
parser, to be able to process more complex sentences.

# Actions Ontology Project
## What is it?
It is a collaborative project of a verbs categorization ontology,
the goal of the project is to achieve an english semantical tree
with a huge range of verbs, from more global ones to more precise
ones, related with each others through their meanings.
For example, an small tree would be:
Verbs
-Positive
--Pleasant
---Like
So you are able to know that the like word is both a pleasant and
a positive verb (this way you can code in base of the general meaning
of the verb, so if you don't care about the precise meaning
differences, you just need to code until some level).

## How to use it
As any other ontology online. You can use any library you want,
although we highly recommend using RDFLib for Python.
## TO-DOs
- Add more verbs and categories.
- Improve hierarchy based on meaning relations.

# Our Project
## Our Contribution
Our contribution with this project can be sumarized as follows:
- Two open projects to the community with guidelines for future
improves, so the project can continue and get bigger and more 
precise.
- The concept of translating Natural Language directly into RDF.
- Enhacing the lifted data with the Twitter context.
- An ontology project of categorized words based on meaning.
## Utilities
Some examples of possible projects using both contributions
together might be:
- Automatic Participatory Sensing (tweets will provide
parsed information for the data processors).
- Transalte tweets into image sequences (I.E: I like chimichangas
will result into a picture of the user, a 'like' icon, and the
chimichangas picture hosted in dbpedia).
