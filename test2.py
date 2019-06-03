import PyPDF3
import re



# Opening the PDF file in binary format and creating a PDF object
pdfFileObj = open('orange.pdf', 'rb')

# Creating a PDFReader object and passing the pdffile object
pdfReader = PyPDF3.PdfFileReader(pdfFileObj)

def splchrtr(chrtr):
    pgnum_chrt = chrtr
    spl_chrtr = re.search("-", pgnum_chrt)
    if spl_chrtr:
        print("this is in ***-*** format")
        pgnum_list = pgnum_chrt.split("-")
        pgnum = int(pgnum_list[0])
        print("Page number of Questioned costs is :", pgnum)
        return pgnum
    else:
        print("This is in normal format")
        pgnum = int(chrtr)
        return pgnum


for i in range(15):
    pageObj_temp = pdfReader.getPage(i)
    pageContent_temp = pageObj_temp.extractText()
    pageContent_list_temp = pageContent_temp.split()

    # Searching for the string "finding" while traversing thru pages
    if "Questioned" in pageContent_list_temp:
        pos = pageContent_list_temp.index("Questioned")
        print("findings Page number is in table of contents is:", i)
        print("findings word is at position:", pos)
        print(pageContent_list_temp[pos + 2])
        #print(pageContent_list_temp[pos + 6].isalnum())
        #print(pageContent_list_temp[95])
        dot_str = re.findall(".", pageContent_list_temp[pos + 2])
        if dot_str[0] == '.':
            print("This is dotted string")
            dot_pos = pos + 2
            while pageContent_list_temp[dot_pos].isalnum() == False:
                print("I am in while loop")
                dot_pos += 1
                print("new dotpos", dot_pos)
            pgnum_list_format = pageContent_list_temp[dot_pos]
            print("Dot-- Pgnum of finding is:", pgnum_list_format)
            page = splchrtr(pgnum_list_format)
            print("page number is:", page)
        else:
            page = splchrtr(pageContent_list_temp[pos + 2])
            print("Page number is:", page)

        break

