from xml.dom import minidom


#mengurai file xml berdasarkan nama
mydoc = minidom.parse('D:\BELAJAR\Belajar Python\BAB4\file1.xml')

items = mydoc.getElementsByTagName('child')

#one specific item attribute
print ('Item #2 attribute:')
print (items[1].attributes['name'].value)

#all item attribute
print('\nAll attributes: ')
for elem in items :
  print (elem.attributes['name'].value)

#one specific item's data
print('\nItem #2 data:')
print(items[1].firstChild.data)
print(items[1].childNodes[0].data)

#all items data
print('\nAll item data:')
for elem in items:
  print(elem.firstChild.data)
