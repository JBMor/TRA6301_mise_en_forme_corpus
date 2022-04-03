import PyPDF2
from os import listdir

# Gets all PDF files from a directory
input_path = r"C:\Users\jbmor\Desktop\TRA3601_corpus\Manual_FR\\"
output_path = input_path
PDF_files = listdir(input_path)
print(PDF_files)

# Opens all PDF files from input
for file in PDF_files:
    with open(input_path + file, "rb") as pdfObject:

        # Creates a python object from PDF file
        pdf_reader = PyPDF2.PdfFileReader(pdfObject)

        # Parameters needed for the while loop
        x = 0
        y = True
        text = ""

        # Gets the number of pages from PDF file
        page_amount = pdf_reader.numPages

        while y:

            page_obj = pdf_reader.getPage(page_amount - page_amount + x)
            if x < page_amount - 1:

                # Appends text from each PDF file pages
                page_text = page_obj.extractText()
                text = text + page_text
                x = x + 1

                # Prints info
                print(file)
                print(f"Page {x}")
                print(page_text)

            else:
                y = False

        # Writes text variable to new file
        with open(output_path + file + ".txt", "w", encoding="UTF-8") as output_file:
            output_file.writelines(text)
