import PyPDF3
import re

# Opening the PDF file in binary format and creating a PDF object
pdfFileObj = open('Virginia_union.pdf', 'rb')

# Creating a PDFReader object and passing the pdffile object
pdfReader = PyPDF3.PdfFileReader(pdfFileObj)
if pdfReader.isEncrypted:
    print("File is encrypted")
    pdfReader.decrypt("")

print("Total pages:", pdfReader.numPages)

########

for i in range(15):
    print("I am in for loop, page number:", i)
    pageObj_temp = pdfReader.getPage(i)
    pageContent_temp = pageObj_temp.extractText()
    pageContent_list_temp = pageContent_temp.split()

    if "Questioned" in pageContent_list_temp:
        pos = pageContent_list_temp.index("Questioned")
        print("Questioned page number in table of contents is:", i)
        print("Questioned word is at position:", pos)
        dot_str = re.findall(".", pageContent_list_temp[pos + 2])
        if dot_str[0] == ".":
            print("This is dotted string")
            dot_pos = pos + 2
            while pageContent_list_temp[dot_pos].isalnum() == False:
                dot_pos += 1
            pgnum_list_format = pageContent_list_temp[dot_pos]
            print("Pos is:", pos)
            print("page number is:", pgnum_list_format)
            spl_chrtr = re.search("-", pgnum_list_format)
            if (spl_chrtr):
            print("this is in ***-*** format")
            pgnum_list = pgnum_list_format.split("-")
            pgnum = int(pgnum_list[0])
            print("Page number of Questioned costs is :", pgnum)
            break
        else:
            print("This is normal format")
            pgnum_list_format = pageContent_list_temp[pos + 2]
            pgnum = int(pgnum_list_format)
            print("Page number of Questioned costs is :", pgnum)
            break

def splchrtr(chrtr):
    pgnum_chrt = chrtr
    spl_chrtr = re.search("-", pgnum_chrt)
    if (spl_chrtr):
        print("this is in ***-*** format")
        pgnum_list = pgnum_list_format.split("-")
        pgnum = int(pgnum_list[0])
        print("Page number of Questioned costs is :", pgnum)
        return pgnum
    else:
        pgnum = int(chrtr)
        return pgnum


'''
# Searching for the string "finding" while traversing thru pages
    if "Findings" in pageContent_list_temp:
        print("I am first IF loop")
        pos = pageContent_list_temp.index("Findings")
        print("findings Page number is in table of contents is:", i)
        print("findings word is at position:", pos)
        if pageContent_list_temp[pos + 2] == 'Questioned':
            print("Found questioned")
            dot_str = re.findall(".", pageContent_list_temp[pos + 4])
            if dot_str[0] == '.':
                print("This is dotted string")
                dot_pos = pos + 4
                while pageContent_list_temp[dot_pos].isalnum() == False:
                    dot_pos += 1
                pgnum_list_format = pageContent_list_temp[dot_pos]

            pgnum_list_format = pageContent_list_temp[pos + 4]
            print("Pos is:", pos)
            print(pageContent_list_temp[pos + 4])
            print("page number is:", pgnum_list_format)
            spl_chrtr = re.search("-", pgnum_list_format)
            if (spl_chrtr):
                print("this is in ***-*** format")
                pgnum_list = pgnum_list_format.split("-")
                pgnum = int(pgnum_list[0])
                print("Page number of Questioned costs is :", pgnum)
            else:
                print("This is normal format")
                pgnum = int(pgnum_list_format)
                print("Page number of Questioned costs is :", pgnum)
                break
                elif pageContent_list_temp[pos - 1] == 'of' and pageContent_list_temp[pos - 2] == 'Schedule':
            print("Schedule of Findings found")
        else:
            print("Not found")
'''










pdfFileObj.close()

