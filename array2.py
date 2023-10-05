heros=['spider man','thor','hulk','iron man','captain america']

#que1
print(len(heros))

#que2
heros.append("black panther")
print(heros)

#que3
heros.remove("black panther")
print(heros)
heros.insert(3, 'black panther')
print(heros)

#ques4
heros[1:3] = ['Dr strange']
print(heros)

#que5
heros.sort()
print(heros)
