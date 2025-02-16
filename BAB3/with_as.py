with open ("file_io/selamat.txt", "r") as dok :
  print (dok.read())
#pake with as biar gak perlu nulis close lagi, otomatis te apus dari memori

try :
  f = open ("file_io/selamat.txt", "r")
except IOError as err:
  print ("Terjadi Kesalahan: {}".format(err))