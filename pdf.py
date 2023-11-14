import fitz  # PyMuPDF
import difflib
import tkinter as tk
from tkinter import filedialog

def load_pdf(file_path):
    doc = fitz.open(file_path)
    text = ''
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text

def compare_pdfs(pdf1, pdf2):
    sequence_matcher = difflib.SequenceMatcher(None, pdf1, pdf2)
    similarity_ratio = sequence_matcher.ratio()
    return similarity_ratio

def select_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def compare_files():
    file_path1 = entry_file1.get()
    file_path2 = entry_file2.get()

    if not file_path1 or not file_path2:
        result_label.config(text="Please select both PDF files.")
        return

    pdf1 = load_pdf(file_path1)
    pdf2 = load_pdf(file_path2)

    similarity_ratio = compare_pdfs(pdf1, pdf2)
    result_label.config(text=f"Similarity Ratio: {similarity_ratio:.2%}")

# Create GUI
root = tk.Tk()
root.title("PDF Similarity Detector")

# File 1
label_file1 = tk.Label(root, text="Select PDF file 1:")
label_file1.grid(row=0, column=0, padx=10, pady=10)
entry_file1 = tk.Entry(root, width=50)
entry_file1.grid(row=0, column=1, padx=10, pady=10)
button_file1 = tk.Button(root, text="Browse", command=lambda: select_file(entry_file1))
button_file1.grid(row=0, column=2, padx=10, pady=10)

# File 2
label_file2 = tk.Label(root, text="Select PDF file 2:")
label_file2.grid(row=1, column=0, padx=10, pady=10)
entry_file2 = tk.Entry(root, width=50)
entry_file2.grid(row=1, column=1, padx=10, pady=10)
button_file2 = tk.Button(root, text="Browse", command=lambda: select_file(entry_file2))
button_file2.grid(row=1, column=2, padx=10, pady=10)

# Compare Button
button_compare = tk.Button(root, text="Compare PDFs", command=compare_files)
button_compare.grid(row=2, column=1, pady=20)

# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=1)

root.mainloop()
