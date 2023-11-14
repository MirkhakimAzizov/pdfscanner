import PyPDF2
from tkinter import *

def calculate_similarity():
    # Get the file paths from the text boxes
    file1_path = file1_entry.get()
    file2_path = file2_entry.get()

    try:
        # Open the PDF files
        file1 = open(file1_path, 'rb')
        file2 = open(file2_path, 'rb')

        # Create PDF reader objects
        pdf1 = PyPDF2.PdfFileReader(file1)
        pdf2 = PyPDF2.PdfFileReader(file2)

        # Extract text from the PDF files
        text1 = ""
        for page in range(pdf1.getNumPages()):
            text1 += pdf1.getPage(page).extractText()

        text2 = ""
        for page in range(pdf2.getNumPages()):
            text2 += pdf2.getPage(page).extractText()

        # Calculate similarity percentage (dummy calculation)
        similarity_percentage = 75.0

        # Update the GUI with the similarity percentage
        similarity_label.config(text=f"Similarity: {similarity_percentage}%")

        # Close the PDF files
        file1.close()
        file2.close()

    except FileNotFoundError:
        similarity_label.config(text="File not found!")

root = Tk()
root.title("PDF Similarity Checker")

# Add labels, buttons, and text boxes
file1_label = Label(root, text="PDF File 1:")
file1_label.pack()

file1_entry = Entry(root, width=50)
file1_entry.pack()

file2_label = Label(root, text="PDF File 2:")
file2_label.pack()

file2_entry = Entry(root, width=50)
file2_entry.pack()

similarity_button = Button(root, text="Calculate Similarity", command=calculate_similarity)
similarity_button.pack()

similarity_label = Label(root, text="")
similarity_label.pack()

root.mainloop()
