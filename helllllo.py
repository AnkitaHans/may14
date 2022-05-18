import numpy
rno=[1,2,3,4,5]
names=['joe','luci','jack','doe','flora']
marks=[11,100,33,88,9]
z=list(zip(rno,names,marks))
print(z)
zip1=zip(rno,names)
print(list(zip1))
print(list(zip(*z)))

