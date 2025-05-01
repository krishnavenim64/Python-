Import PyPDF2



Pdf_file = “document.pdf”

With open(pdf_file, “rb”) as file:

    Reader = PyPDF2.PdfReader(file)

    For page in reader.pages:

        Print(page.extract_text())

