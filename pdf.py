import PyPDF2
import sys
import os

names = []
directory = './PDFs/'
for filename in os.listdir(directory):
    new_name = directory + filename
    names.append(new_name)

# with open('./PDFs/dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)
#     page = reader.getPage(0)
#     page.rotateClockwise(90)
#
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)

def pdf_combiner(li):
    merger = PyPDF2.PdfFileMerger()
    for pdf in li:
        print(pdf)
        merger.append(pdf)
    merger.write('./PDFs/super.pdf')

template = PyPDF2.PdfFileReader(open('PDFs/super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('PDFs/wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('PDFs/watermarked_output.pdf', 'wb') as file:
        output.write(file)
