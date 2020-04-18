import xml.etree.ElementTree as et
drzewo=et.parse('dane.xml')
print(type(drzewo))
imie = drzewo.find("imie")

print(imie.text)

adres=drzewo.find('adres')
miasto=adres.find('miasto')

print(miasto.text)

write("<head></head><body>")
write("<a href='")
write("pobieranie  z jsona")
write("'>link do obrazka</a>")
write("</body>")