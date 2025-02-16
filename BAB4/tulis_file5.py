import csv
from operator import delitem

#membaca baris per baris
with open ("file_io/siswa.csv") as csvfile :
  readCSV = csv.reader(csvfile, delimiter=',')
  for row in readCSV :
    print (row)