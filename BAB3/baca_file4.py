# buka file
file_selamat = open("file_io/selamat.txt", "r")

#baca file cara 2
selamat = file_selamat.read()

#cetak isi file 
print (selamat)

#tutup file
file_selamat.close()
# fungsi close ini agar dihapus dari memori