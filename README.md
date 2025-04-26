# 📄 PDF Utils

Simple Python command-line tools to manage PDFs:
- Merge multiple PDFs into one
- Split a PDF into individual single-page PDFs

---

## 🚀 Features

- 🗂️ Merge multiple PDFs into a single file
- ✂️ Split a multi-page PDF into separate single-page PDFs
- 📦 Lightweight and easy to use
- 🛠️ Written in pure Python using PyPDF2

---

## ⚠️ Error Handling

- If the input PDF file doesn't exist, a friendly error will be shown.
- If no file or invalid page range is provided, helpful usage instructions are printed.
- Page range validation ensures correct splitting.

---

## 📚 Requirements

- Python 3.7+
- PyPDF2 library

Install dependencies:

```bash
pip install PyPDF2

---

## Runtime commands:

- Merges `file1.pdf` and `file2.pdf` into a new file called `merged_output.pdf`

```bash
python3 merge_pdfs.py file1.pdf file2.pdf merged_output.pdf
```

- Splits the entire input.pdf into separate pages.
- Output saved into a folder: input_split_pages/

```bash
python3 split_pdfs.py input.pdf
```

- Split Specific Page Range

```bash
python3 split_pdfs.py input.pdf <start-page> <end-page>
```
