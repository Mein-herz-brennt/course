import xml.etree.ElementTree as ET

etree = ET.ElementTree(file="XML_For_parse.xml")
root = etree.getroot()
for child in root:
    title = child.find("title").text
    code = child.find("code").text
    category = child.find("Category").text
    sub_Category = child.find("Sub_Category").text
    price = child.find("Price").text
    description = child.find("description")
    picture = child.find("picture")
    attrs = child.find("attrs")
    print(title)
    print(code)
    print(category)
    print(sub_Category)
    print(price)
    # if description is not None:
    #     print(description.text)
    print(f"https://protachka.com.ua/wp-content/uploads/{code}.jpg")

    if attrs is not None:
        attr = attrs.find("attr")
        for at in attr:
            print(at.tag, at.text)
    print("----------------------")

# products = et.findall("Product")
# a = []
# for product in products:
#     a.append(product.attrib)
#
# print(a)
