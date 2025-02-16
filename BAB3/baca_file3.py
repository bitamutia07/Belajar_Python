# buka file
file_selamat = open("file_io/selamat.txt", "r")

#baca file cara 2
selamat = file_selamat.readlines()

#cetak isi file dengan pengeluaran
for teks in selamat :
  print (teks)

#tutup file
file_selamat.close()
# fungsi close ini agar dihapus dari memori