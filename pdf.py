import PyPDF2

with open('dummy.pdf','rb') as my_file:
    reader=PyPDF2.PdfFileReader(my_file)
    print(reader.numPages)
    page=reader.getPage(0)
    print(page)
    print(page.rotateCounterClockwise(90))

    writer=PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open('tilt.pdf','wb') as file:
        writer.write(file)
