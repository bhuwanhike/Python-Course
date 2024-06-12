import PyPDF2
import os

pdfs = ["file3.pdf", "file2.pdf", "file3.pdf"]
merger = PyPDF2.PdfMerger()

for i in pdfs:
    pdFile = open(i, 'rb')
    pdfread = PyPDF2.PdfReader(pdFile)
    merger.append(pdfread)

pdFile.close()
merger.write('merged pdf') 
os.startfile('merged pdf')