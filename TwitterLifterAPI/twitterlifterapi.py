import nltk
from EntityLinker import entitylinker
import json

def lift(tweet):
    tokens = nltk.word_tokenize(tweet.text)
    tagged = nltk.pos_tag(tokens)
    
    subject = None
    verb = None
    direct_object = None

    for tag in tagged:
        if subject is None and (tag[1] == 'NNS' or tag[1] == 'NNP' or tag[1] == 'PRP'):
            subject = twitter_linker(tag[0], tweet)
        elif verb is None and (tag[1] == 'VB' or tag[1] == 'VBP' or tag[1] == 'VBZ'):
            verb = third_person(tag[0])
        elif direct_object is None and (tag[1] == 'NNS' or tag[1] == 'NNP' or tag[1] == 'PRP'):
            direct_object = twitter_linker(tag[0], tweet)
    
    return '{"' + subject + '":{"aop:' + verb + '":[{"value":"' + direct_object + '","type":"uri"}]}}' 

def twitter_linker(word, tweet):
    if word.lower() == 'i' or word.lower() == 'me':
        return "https://twitter.com/intent/user?user_id=" + str(tweet.author.id)
    elif tweet.text[tweet.text.index(word)-1] == '@':
        return "https://twitter.com/users/" + word
    else:
        return entitylinker.link(word)

def third_person(verb):
    if not verb.endswith('s'):
        return verb + 's'
    else:
        return verb
