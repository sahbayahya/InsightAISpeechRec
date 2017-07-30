
# this is an old ntlk version, download this way:
#pip install https://github.com/nltk/nltk/tarball/model

from nltk.corpus import brown
from nltk.probability import LidstoneProbDist, WittenBellProbDist
import sys




def simple_ngram(inputfile):

    estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
    counts = {}
    for line in open('persuasion.txt','r'):
        for word in line.strip().lower().split():
            counts[word] = counts.get(word, 0) + 1
    total = sum(counts.values()) + len(counts)
    #print total
    for sent in open(inputfile, 'r'):
        prob =  1.0
        for w in sent.strip().lower().split():
            prob = prob * (float(counts.get(w, 0))/total)
        print prob

    # tutorial link: https://pythonhosted.org/ngram/tutorial.html
    #search
    #Use search() to return similar items in a set, and find() to only return the most similar item:
    #
    # import ngram
    # G = ngram.NGram(['joe','joseph','jon','john','sally'])
    # print G.search('jon')
    # print "--"*30
    # print  "only with probability higher than 0.3:" , G.search('jon', threshold=0.3)
    # print "only the most similar:" , G.find('jose')
    #

if __name__=='__main__':
    inputfile = sys.argv[1]
    ngram(inputfile)
