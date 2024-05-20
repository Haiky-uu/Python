# build small application to query xml file

import xml.etree.ElementTree as ET


def xlaP(tree):
    root = tree.getroot()  # getting root of tree
    print(ET.tostring(root))   # getting all details of the xml with respect to root
    root.set('Details','Companies')   # setting attrib to root node with a value
    print(root.attrib)  # Printing all attributes of the root
    tree.write('./cat.xml')  # Writing changes to the file

    print("-----------------")
    for child in root:
        for ch in child:
            if ch.tag not in ['ARTIST',"COMPANY"]:
                print(ch.text)

            if ch.tag == 'TITLE':
                print("Name of companies: ",ch.text)

            if ch.tag == 'COUNTRY':
                print("Country is :",ch.text)

            if ch.tag == 'YEAR':
                print("---------------")



def main():
    path = './cat.xml'
    tree = ET.parse(path)
    xlaP(tree)



if __name__ == '__main__':
    main()



