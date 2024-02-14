import sys
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(path, output_base):
    reader = PdfReader(path)
    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)
        output_filename = f'{output_base}_page_{i}.pdf'
        with open(output_filename, 'wb') as output_pdf:
            writer.write(output_pdf)
        print(f"Created: {output_filename}")

if __name__ == '__main__':
    if len(sys.argv) == 3:
        path = sys.argv[1]
        output_base = sys.argv[2]
        split_pdf(path, output_base)
    else:
        print("Usage: python pdf_splitter.py input_file output_base")
