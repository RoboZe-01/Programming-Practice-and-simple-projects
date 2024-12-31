

# Project Done by RoboZe ( Prem )

# This Project is the Part of making 5 unique project in 2 days     
# To end the year with the feeling of accomplishment
 

         ###  PDF Merger    ### 

# In this project user can merge two or more pdf by entering the path of the pdfs to be merged

# Main features of this project are : 

#  1. Take Input from user as a path address
#  2. User can add as many pdfs as they want . 
#  3. If they want to to stop they can enter "done"
#  4. User can specify the name of the pdf 
#  5. Only pdf type file format is acceptable other will be shown as " NOt valid pdf "

# Lets start coding 






# install Pypdf2 using pip install 
# import pypdf2 and os 

# Documentation of PyPdf2 :  https://www.geeksforgeeks.org/introduction-to-python-pypdf2-library/
# Documentation of Os      : https://www.geeksforgeeks.org/os-module-python-examples/
# Learn more about Pypdf2  and Os from above link 






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
    try:                            # try and except are used for error handeling for smoother excecution

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
