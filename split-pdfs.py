import PyPDF2
import sys
import os

def split_pdf(input_pdf):
    # Read the PDF
    pdf_reader = PyPDF2.PdfReader(input_pdf)

    # Create output folder
    base_name = os.path.splitext(os.path.basename(input_pdf))[0]
    output_folder = f"{base_name}_split_pages"
    os.makedirs(output_folder, exist_ok=True)

    # Split each page into separate PDF
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])

        output_path = os.path.join(output_folder, f"{base_name}_page_{page_num + 1}.pdf")
        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

    print(f"✅ Split {len(pdf_reader.pages)} pages into folder '{output_folder}'.")

if __name__ == '__main__':
    input_pdf = sys.argv[1]
    split_pdf(input_pdf)

