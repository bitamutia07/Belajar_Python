import csv
siswa = {
  ('Yuniar Spardi', 'A', 90),
  ('Nia Yusnia', 'B', 85),
  ('Tania Noor', 'A', 80),
  ('Ganesha Noor', 'B', 90),
  ('Zumastina Noor', 'C', 70)
}

#tentukan lokasi file, nama file, dan inisiasi csv
f = open("file_io/siswa.csv", "w")
w = csv.writer(f)
w.writerow(('Nama', 'Kelas', 'Nilai'))

#menulis file csv
for s in siswa :
  w.writerow(s)

#menutup file csv
f.close()