import sys
from PyPDF2 import PdfMerger

def merge_pdfs(paths, output):
    merger = PdfMerger()
    for path in paths:
        merger.append(path)
    merger.write(output)
    merger.close()

if __name__ == '__main__':
    if len(sys.argv) > 3:
        paths = sys.argv[1:-1]
        output = sys.argv[-1]
        merge_pdfs(paths, output)
        print(f"Merged files {paths} into {output}")
    else:
        print("Usage: python pdf_merger.py [input_files] output_file")
