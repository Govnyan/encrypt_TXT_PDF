###---Encrypt PDF file---###
from PyPDF2 import PdfReader, PdfWriter
from getpass import getpass

pdfwriter = PdfWriter()
pdf = PdfReader("test.pdf")

for page in range(pdf.numPages):
    pdfwriter.add_page(pdf.pages[page])

password = getpass(prompt="Enter password: ")
pdfwriter.encrypt(password)

with open("test_encrypted.pdf", "wb") as f:
    pdfwriter.write(f)