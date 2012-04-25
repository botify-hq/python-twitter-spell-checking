import re, collections
import ConfigParser
import os 

# Lambda function which tranforms a ConfigParser items
# list of tuples object into a dictionnary
items_to_dict = lambda items : {k:v for k,v in items}

def words(text): return re.findall('[a-z]+', text.lower()) 

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

class CorrectWord(object):
    def __init__(self, correct_inst):
        self.correct_inst = correct_inst

    def known_edits2(self, word):
        return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in Correct.NWORDS[self.correct_inst.key])

    def known(self, words): return set(w for w in words if w in Correct.NWORDS[self.correct_inst.key])

    def correct(self, word):
        candidates = self.known([word]) or self.known(edits1(word)) or self.known_edits2(word) or [word]
        return max(candidates, key=Correct.NWORDS[self.correct_inst.key].get)

class Correct(object):

    NWORDS = dict()

    def __init__(self, settings_file, namespace):
        self.settings_file = settings_file
        self.namespace = namespace
        CONFIG = ConfigParser.ConfigParser()
        CONFIG.read(settings_file)

        config = items_to_dict(CONFIG.items('namespace:%s' % namespace))
        self.key = '%s:%s' % (settings_file, namespace)
        if self.key not in Correct.NWORDS:
            Correct.NWORDS[self.key] = train(words(open(os.path.join(config['files'], 'tweets_%s.txt' % namespace)).read()))

    def correct(self,word):
        cw = CorrectWord(self)
        return ' '.join([cw.correct(w) for w in word.split(' ')])
