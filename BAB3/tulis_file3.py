print("Selamat Datang di Program Biodata")
print("=====================================")

#Ambil input dari user
nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")

#format teks
teks = "\nNama: {}\nUmur: {}\nAlamat: {}\n".format(nama, umur, alamat)

#buku file untuk ditulis
file_bio = open("file_io/biodata.txt", "a")
# a -> digunakan untuk menambah (append) data ke file, menambahkan isi file tanpa mengantinya

#tulis teks ke file
file_bio.write(teks)

#tutup file
file_bio.close()