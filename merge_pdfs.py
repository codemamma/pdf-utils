import PyPDF2
import sys
import os

def merge_pdfs(paths, output):
    pdf_writer = PyPDF2.PdfWriter()

    for path in paths:
        pdf_reader = PyPDF2.PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    inputs = sys.argv[1:-1]
    output = sys.argv[-1]
    merge_pdfs(inputs, output)

