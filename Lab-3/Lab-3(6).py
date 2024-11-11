ll=[]
for i in range(25):
    ll.append(random.randint(0,25))
meanll=numpy.mean(ll)
medianll=numpy.median(ll)
modell=stats.mode(ll)
print(ll)
print("mean is", meanll)
print("median is",medianll)
print("mode is",modell)
