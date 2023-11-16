import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfFileReader
import re

class PlagiarismChecker:
    def __init__(self, master):
        self.master = master
        master.title("Plagiarism Checker")

        self.file1_path = None
        self.file2_path = None

        self.browse_button1 = tk.Button(master, text="Asosiy faylni tanlang", command=self.browse_pdf_file1)
        self.browse_button1.pack(pady=10)

        self.browse_button2 = tk.Button(master, text="Tekshiriladigon fayl!", command=self.browse_pdf_file2)
        self.browse_button2.pack(pady=10)

        self.check_button = tk.Button(master, text="O'xshashlikni tekshirish", command=self.check_plagiarism)
        self.check_button.pack(pady=20)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=20)

    def extract_text(self, file_path):
        text = ""
        with open(file_path, "rb") as file:
            pdf_reader = PdfFileReader(file)
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extract_text()
        return text

    def calculate_plagiarism_percentage(self, text1, text2):
        words1 = re.findall(r'\b\w+\b', text1.lower())
        words2 = re.findall(r'\b\w+\b', text2.lower())
        p = 0
        for t1 in words1:
            for t2 in words2:
                if t1 == t2:
                    p = p + 1
        # common_words = set(words1) & set(words2)
        # plagiarism_percentage = (len(common_words) / len(set(words1))) * 100
        # plagiarism_percentage = (p / (len(words1) + len(words2) - p * 2)) * 100
        plagiarism_percentage = (p / (len(words1))) * 100

        return plagiarism_percentage

    def browse_pdf_file1(self):
        self.file1_path = filedialog.askopenfilename(
            title="Select PDF File 1",
            filetypes=[("PDF files", "*.pdf")]
        )

    def browse_pdf_file2(self):
        self.file2_path = filedialog.askopenfilename(
            title="Select PDF File 2",
            filetypes=[("PDF files", "*.pdf")]
        )

    def check_plagiarism(self):
        if self.file1_path and self.file2_path:
            text1 = self.extract_text(self.file1_path)
            text2 = self.extract_text(self.file2_path)

            plagiarism_percentage = self.calculate_plagiarism_percentage(text1, text2)
            self.result_label.config(text=f"O'xshashlik: {plagiarism_percentage:.2f}%")
        else:
            self.result_label.config(text="Iltimos barcha maydonlarni to'ldiring, 2 ta pdf fayl tanlaganingizga ishonch hosil qiling !")

if __name__ == "__main__":
    root = tk.Tk()
    plagiarism_checker = PlagiarismChecker(root)
    root.mainloop()
