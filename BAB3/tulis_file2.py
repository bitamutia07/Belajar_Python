print("Program membaca dan menulis file teks")
print("=====================================")

#Ambil input dari user
nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")

#format teks
teks = "Nama: {}\nUmur: {}\nAlamat: {}".format(nama, umur, alamat)

#buku file untuk ditulis
file_bio = open("file_io/biodata.txt", "r+")
# r+ -> digunakan untuk membaca sekaliguss menulis data ke file

#tulis teks ke file
file_bio.write(teks)

#tutup file
file_bio.close()

