from sqlite3 import Row


matrik1 = [
  [5, 0],
  [2, 6]
]

matrik2 = [
  [1, 0],
  [4, 2]
]

matrik3 = []

print (matrik1)
print (matrik2)

for x in range (0, len(matrik1)) :
  Row = []
  for y in range(0, len(matrik1[0])) :
    total = 0
    for z in range(0, len(matrik1)) :
      total = total + (matrik1[x][z] * matrik2[z][y])
    Row.append(total)
  matrik3.append(Row)

for x in range(0, len(matrik3)) :
  for y in range(0, len(matrik3[0])):
    print (matrik3[x][y], end=' ')