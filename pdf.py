import tkinter as tk
from tkinter import filedialog
import PyPDF2

def hisobla_foiz(pdf1, pdf2):
    # Birinchi PDF faylni ochamiz
    with open(pdf1, 'rb') as file1:
        pdf_reader1 = PyPDF2.PdfFileReader(file1)
        page_count1 = pdf_reader1.numPages

    # Ikkinchi PDF faylni ochamiz
    with open(pdf2, 'rb') as file2:
        pdf_reader2 = PyPDF2.PdfFileReader(file2)
        page_count2 = pdf_reader2.numPages

    # Foizni hisoblaymiz
    if page_count1 > 0 and page_count2 > 0:
        foiz = (min(page_count1, page_count2) / max(page_count1, page_count2)) * 100
        return foiz
    else:
        return 0

def fayl_tanlash():
    # Fayl menejer oynasini ochamiz
    root = tk.Tk()
    root.withdraw()

    # Birinchi PDF faylni tanlash
    file_path1 = filedialog.askopenfilename(title="Birinchi PDF faylni tanlang", filetypes=[("PDF fayllari", "*.pdf")])

    # Ikkinchi PDF faylni tanlash
    file_path2 = filedialog.askopenfilename(title="Ikkinchi PDF faylni tanlang", filetypes=[("PDF fayllari", "*.pdf")])

    # Foizni hisoblash va natijani korsatish
    if file_path1 and file_path2:
        foiz = hisobla_foiz(file_path1, file_path2)

        # Yangi oyna yaratish
        result_window = tk.Tk()
        result_window.title("Natija")

        # Natijani korsatish
        result_label = tk.Label(result_window, text=f"Foiz: {foiz}%", font=("Helvetica", 12))
        result_label.pack(pady=20)

        # Oynani ishga tushirish
        result_window.mainloop()

if __name__ == "__main__":
    fayl_tanlash()
