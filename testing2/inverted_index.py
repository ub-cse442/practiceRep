from myMRjob import myMRjob
##
##
class inverted_index(myMRjob):

    def mapper(self,k,v):
        for w in v.split():
            yield w,k

    def reducer(self,k,l):
        yield k,sorted(list(set(l)))

data = {1:'See Spot Run', 2:'Run Spot Run'}


results = inverted_index().run(data)

for result in results:
    print result

quit()

data = {k:v for k,v in enumerate(open('pynchon.txt').read().split('\n\n'))}
results = inverted_index().run(data)

for word,paranums in results:
    print word,paranums
