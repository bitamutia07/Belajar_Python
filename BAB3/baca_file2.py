# buka file
file_selamat = open("file_io/selamat.txt", "r")

#baca file cara 2
selamat = file_selamat.readlines()

#cetak dalam bentuk perbaris
print("Dalam Bentuk Baris : ")
print (selamat[0])
print (selamat[1])

#tutup file
file_selamat.close()
# fungsi close ini agar dihapus dari memori