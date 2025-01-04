from xml.dom import minidom

DOMTree = minidom.parse("dane_xml.xml")
print(DOMTree)  # <xml.dom.minidom.Document object at 0x00000253699B3FB0>
print(DOMTree.toxml())
# <?xml version="1.0" ?><znajomi>
#     <osoba>
#         <imie foo="zzz">Zygmunt</imie>
#         <email>1@1.pl</email>
#     </osoba>
#     <osoba>
#         <imie foo="aaaa">Janina</imie>
#         <email>2@2.pl</email>
#     </osoba>
# </znajomi>

cNodes = DOMTree.childNodes
print(cNodes)  # [<DOM Element: znajomi at 0x28094a5ba40>]
znajomi = cNodes[0]
print("Znajomi: ",znajomi) # Znajomi:  <DOM Element: znajomi at 0x1b5100eba40>

print(znajomi.getElementsByTagName("osoba")) # [<DOM Element: osoba at 0x1c87fedb650>, <DOM Element: osoba at 0x1c87fedbbf0>]
persons = znajomi.getElementsByTagName("osoba")
print(persons[0].toxml())
# <osoba>
#         <imie foo="zzz">Zygmunt</imie>
#         <email>1@1.pl</email>
#     </osoba>
print(persons[1].toxml())
# <osoba>
#         <imie foo="aaaa">Janina</imie>
#         <email>2@2.pl</email>
#     </osoba>

osoba = persons[0]
imie = osoba.getElementsByTagName("imie")[0]
print(imie) # [<DOM Element: imie at 0x1f28aacbb60>]
imie_1 = imie.firstChild.data
print(imie_1) # Zygmunt
atrybut = imie.getAttribute("foo")
print(atrybut) # zzz

#import xml.etree.ElementTree as ET
import pandas as pd

#tree = ET.parse('dane_xml.xml')
#print(tree)
from io import StringIO
xml = DOMTree.toxml()
# print(xml)
df = pd.read_xml(StringIO(xml),parser='lxml')
print(df)
print(5 * '-')
df2 = pd.read_xml('dane_xml.xml',parser='lxml')
print(df2)
print(5 * '-')
df3 = pd.read_xml('dane_xml.xml',parser='etree')
print(df3)

#       imie   email
# 0  Zygmunt  1@1.pl
# 1   Janina  2@2.pl
# -----
#       imie   email
# 0  Zygmunt  1@1.pl
# 1   Janina  2@2.pl
# -----
#       imie   email
# 0  Zygmunt  1@1.pl
# 1   Janina  2@2.pl