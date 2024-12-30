


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





# Step 1 
# Import alll the important libraries and modules 

import PyPDF2 
import os 

# We will make a function for users to input  their pdf 

def pdf_input ():
   pdf_files = []    # Empty list to add all the proper pdf in it( path )
   print(" Enter the paths of pdf to be merged ( write (Done) when want to stop )")    # Simple instructions for users
   

   while True :                                                      # for iterating until user enters "Done "
    user_input = input(" Enter the path of pdf :  ").strip('"')                                    # user input 
    if user_input.lower() == "done":
     break
     
      # we will check whether the Given Path input is valid or not and pdf extension

    if os.path.isfile(user_input) and user_input.endswith(".pdf"):   # Condition to check Path and format to be PDF
      pdf_files.append(user_input)
    else :
      print(f'Invalid path or file : {user_input}') 
    return pdf_files    

pdf_files = pdf_input 



                       ### Step 3 : Process ###

if not  pdf_files :
  print(" No valid Pdf ( path)")

else :
      try :

        # Merging the PDF


        merger = PyPDF2.PdfMerger()

        for pdf in pdf_files :               # Pdf will run over each paths in the pdf_files variable 
          print(" Adding files {pdf}")

          merger.append(pdf)                 # merger function will be appended with pdf ( paths in the pdf_files)                   
        
        ### Step 4 : Output ###

        # Asking users for the name of the merged pdf 

        output_pdf = input( " Enter the name of pdf ( With .Pdf extenstion  )").strip('"')

        if not output_pdf.endswith(".pdf"):         # if user accidently did not add (.pdf ) extension the program will automatically add it
          output_pdf+= ".pdf"

        merger.write(output_pdf)           # Merged pdf will get the name defined by user 
        merger.close()

        print(f'Merged PDF is saved as : {output_pdf}')


      except Exception as e :  
        print(f" An error occured as {e}")  
 

          
        




        



          












      




      
   





   










