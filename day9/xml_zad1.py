# dane w tagach, pliki xml

#  1 <rozklad>
#  2   <miejscowosc>Poznań</miejscowosc>
#  3   <linia>
#  4       <numer>5</numer>
#  5       <poczatek>Górczyn</poczatek>
#  6       <koniec>Miłostowo</koniec>
#  7   </linia>
#  8   <linia>
#  9       <numer>105</numer>
# 10       <poczatek>Rondo Rataje</poczatek>
# 11       <koniec>Piątkowo</koniec>
# 12   </linia>
# 13 </rozklad>

from xml.dom import minidom

from pydantic.v1 import root_validator

root = minidom.Document()

xml = root.createElement("root")

root.appendChild(xml)

productChild = root.createElement('product')
productChild.setAttribute('name', "Python-to-Python")
xml.appendChild(productChild)
print(root)  # <xml.dom.minidom.Document object at 0x00000141FC64E210>
xmlStr = root.toprettyxml()
print(xmlStr)
# <?xml version="1.0" ?>
# <root>
# 	<product name="Python-to-Python"/>
# </root>

print(type(xmlStr))  # <class 'str'>
save_path = "ptp.xml"
with open(save_path,'w') as f:
    f.write(xmlStr)
