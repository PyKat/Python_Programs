import PyPDF2 #install PyPDF2 (pip install PyPDF2)
import docx #install python-docx (pip install python-docx)
from docx.shared import Inches

pdfFileObj = open('C:/Users/krane/Desktop/New folder New/Ketan Ranebennur_Resume.pdf', 'rb') #path of your PDF file
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
pageObj.extractText()
f= open("C:/Users/krane/Desktop/New folder New/new_file.doc","w+") #Path of your DOC file to be saved
f.write(pageObj.extractText()) #Write into the doc file