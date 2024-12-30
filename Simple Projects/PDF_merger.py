import PyPDF2
import os

# Function to validate file paths
def get_valid_pdf_paths():
    pdf_files = []
    print("Enter the paths of PDFs to merge (type 'done' when finished):")
    while True:
        file = input("Enter file path: ").strip('" ')  # Strip extra quotes or spaces
        if file.lower() == 'done':
            break
        if os.path.isfile(file) and file.endswith(".pdf"):
            pdf_files.append(file)
        else:
            print(f"Invalid file path or not a PDF: {file}")
    return pdf_files

# Main script
pdf_files = get_valid_pdf_paths()

if not pdf_files:
    print("No valid PDFs provided. Exiting.")
else:
    try:
        # Merge PDFs
        merger = PyPDF2.PdfMerger()
        for pdf in pdf_files:
            print(f"Adding file: {pdf}")
            merger.append(pdf)

        # Ask for output file name
        output_file = input("Enter the output file name (with .pdf extension): ").strip('" ')
        if not output_file.endswith(".pdf"):
            output_file += ".pdf"

        merger.write(output_file)
        merger.close()
        print(f"Merged PDF saved as {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
