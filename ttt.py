init=[[1,2,3],[4,5],[6,7]]
flatten=[]
for outer in init:
    for inner in outer:
        flatten.append(inner)
flatten

print [inner for outer in init for inner in outer]
