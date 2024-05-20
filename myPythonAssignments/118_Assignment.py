# 118 read xml file and print all lines, search specific tags

import xml.etree.ElementTree as et

trace = et.parse("./countryTest.xml")
print(trace)

root = trace.getroot()
print("Root tag:- ",root.tag)
# print(root.tag)
dic = {}

for child in root:
    attrib = child.attrib
    tag = child.tag

    if 'name' not in attrib:
        print(child.text)
        print("This is not country")
        if 'color' in attrib:
            print("Color", attrib['color'])
        if 'fruit' in attrib:
            print("Fruit", attrib['fruit'])
    else:
        print("Country Name:- ",attrib['name'])
    if 'area' in attrib:
        print("Country Area:- ",attrib['area'])

    for details in child:
        #print(details.attrib)
        if details.text != None:
            print(details.tag,':-',details.text)
        else:
            print("Neighbour:- ",details.attrib['name']," in direction ", details.attrib['direction'])

    print("-----------------------------------")



