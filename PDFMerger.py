from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
files=["Profile.pdf","StackingOrder.pdf"]

writer=PdfFileWriter()
for i in files:
    pdf=PdfFileReader(i,'rb')
    for Pno in range(pdf.getNumPages()):
        writer.addPage(pdf.getPage(Pno))
f=open("Merged.pdf",'wb')
writer.write(f)
f.close()