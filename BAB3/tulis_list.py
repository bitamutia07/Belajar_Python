teks = "ini kumpulan warna"
teks_list = ["Biru", "Hujau", "Kuning"]

f = open("file_io/filewarna.txt", "w")

#tulis teks ke file
f.write(teks)
f.writelines(teks_list)
#write akan menulis semua teks
#writelines akan menulis per baris

#tutup file
f.close()