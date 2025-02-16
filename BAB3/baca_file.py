# buka file
file_selamat = open("file_io/selamat.txt", "r")

# baca isi file
print("Dalam Bentuk List : ")
print (file_selamat.readlines())
#readlines bakal ngehasilin output berupa list

#tutup file
file_selamat.close()
# fungsi close ini agar dihapus dari memori

