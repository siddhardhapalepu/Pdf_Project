import PyPDF3



# Opening the PDF file in binary format and creating a PDF object
pdfFileObj = open('nottoway.pdf','rb')

# Creating a PDFReader object and passing the pdffile object
pdfReader = PyPDF3.PdfFileReader(pdfFileObj)
if pdfReader.isEncrypted:
    print("File is encrypted")
    pdfReader.decrypt("")

print("Total pages:", pdfReader.numPages)
# Creating a page object

pageObj_0 = pdfReader.getPage(0)

# table of contents page

pageObj_2 = pdfReader.getPage(2)
pageContent_2 = pageObj_2.extractText()

pageContent = pageObj_0.extractText()

########

'''
pageObj_12 = pdfReader.getPage(11)
pageContent_12 = pageObj_12.extractText()
pageContent_12_list = pageContent_12.split()
len = len(pageContent_12_list)
print("list length:", len)
if "Questioned" in pageContent_12_list:
    x = pageContent_12_list.index("Questioned")
    print("Questioned is at:", x)
    
'''

for i in range(15):
    pageObj_temp = pdfReader.getPage(i)
    pageContent_temp = pageObj_temp.extractText()
    pageContent_list_temp = pageContent_temp.split()
    if "Questioned" in pageContent_list_temp:
        pos = pageContent_list_temp.index("Questioned")
        print("Questioned Page number is :", i)
        print("Questioned is at:", pos)
        print("page number is:", pageContent_list_temp[pos+2])
        break


#print("Printing first line of the first page")
#companyName = pageContent.splitlines()[0]

companyName = pageContent.partition(".")[0]
#print("Company Name:",companyName)
'''
print("printing list")
pageContent_2_list = pageContent_2.split()
len = len(pageContent_2_list)
print("list lenth:", len)

if "Questioned" in pageContent_2_list:
    x = pageContent_2_list.index("Questioned")
    print("Questioned is at:", x)

print("Page number of Questioned costs:",pageContent_2_list[x+2])

# This is the page number of SCHEDULED FINDINGS AND QUESTIONED COSTS
pgnum = x+2
'''



'''
x = pageContent_2.find("Questioned")
pagenumber = pageContent_2[x+17:x+19]
print("X is at:",x)
print(pageContent_2[571])
print(pageContent_2[589])
print("page number is :", pagenumber)
'''

#print("Page index")
#print(pageContent_2)


#for line in pageContent_2.splitlines():
#    print(line)
#    linecount=linecount + 1







pdfFileObj.close()

