from CartonDB import Carton
import time

k=Carton("db")
start=time.time()
for i in range(1000000):
    k.add(i,i)
k.save()
end=time.time()
print(end-start)