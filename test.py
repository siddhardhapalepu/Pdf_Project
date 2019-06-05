import PyPDF3
import re

# Opening the PDF file in binary format and creating a PDF object
pdfFileObj = open('Elderly_housing.pdf', 'rb')

# Creating a PDFReader object and passing the pdffile object
pdfReader = PyPDF3.PdfFileReader(pdfFileObj)
if pdfReader.isEncrypted:
    print("File is encrypted")
    pdfReader.decrypt("")

print("Total pages:", pdfReader.numPages)

########

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

def nextpgnum(curr_pos, curr_page, list_len):
    current_pos = int(curr_pos)
    current_page = int(curr_page)
    list_length_2 = list_len
    pgnum_pattern = '[0-9]'
    while curr_pos < list_length:
        #print("inside second while")
        curr_pos += 1
        temp_str = pageContent_list_temp[curr_pos]
        #print(temp_str)
        result = re.match(pgnum_pattern, temp_str)
        if result:
            print("Found next pagenumber:", pageContent_list_temp[curr_pos])
            next_pg_num = pageContent_list_temp[curr_pos]
            return int(next_pg_num)
            break
        else:
            #print("next page number not found")
            continue


flag_pos = int(0)
flag_dot_pos = int(0)

for i in range(15):
    pageObj_temp = pdfReader.getPage(i)
    pageContent_temp = pageObj_temp.extractText()
    pageContent_list_temp = pageContent_temp.split()
    list_length = len(pageContent_list_temp)


    # Searching for the string "finding" while traversing thru pages
    if "Questioned" in pageContent_list_temp:
        pos = pageContent_list_temp.index("Questioned")
        #print("findings Page number is in table of contents is:", i)
        #print("Questioned word is at position:", pos)
        #print(pageContent_list_temp[pos + 2])
        #print(pageContent_list_temp[pos + 6].isalnum())
        #print(pageContent_list_temp[95])
        dot_str = re.findall(".", pageContent_list_temp[pos + 2])
        if dot_str[0] == '.':
            print("This is dotted string")
            dot_pos = pos + 2
            while pageContent_list_temp[dot_pos].isalnum() == False:
                #print("I am in while loop")
                dot_pos += 1
                #print("new dotpos", dot_pos)
            pgnum_list_format = pageContent_list_temp[dot_pos]
            #print("Dot-- Pgnum of finding is:", pgnum_list_format)
            page = splchrtr(pgnum_list_format)
            flag_dot_pos = 1
            print("page number is:", page)
            print("current page is (dot)", i)
            next_pg = nextpgnum(dot_pos, i, list_length)
            print("Next pg num:", next_pg)
        else:
            flag_pos = 1
            page = splchrtr(pageContent_list_temp[pos + 2])
            print("Page number is:", page)
            print("current page is (else):", i)
            next_pg = nextpgnum(pos+2, i, list_length)
            print("Next pf num:", next_pg)

        break

pattern = '(\d{4})-(\d{3})'

print("########################################################")
print("Questioned costs page:", page)
print("Next page number:", next_pg)





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

