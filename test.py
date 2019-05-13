import PyPDF2



# Opening the PDF file in binary format and creating a PDF object
pdfFileObj = open('wesley.pdf','rb')

# Creating a PDFReader object and passing the pdffile object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print("Total pages:", pdfReader.numPages)
# Creating a page object

pageObj_0 = pdfReader.getPage(0)

# table of contents page

pageObj_2 = pdfReader.getPage(2)
pageContent_2 = pageObj_2.extractText()

pageContent = pageObj_0.extractText()


#print("Printing first line of the first page")
#companyName = pageContent.splitlines()[0]

companyName = pageContent.partition(".")[0]
print("Company Name:",companyName)

#print("Page index")
#print(pageContent_2)

for line in pageContent_2.splitlines():
    print(line)






pdfFileObj.close()


