import csv
import PyPDF2
import re

data = open('C:\\Users\\Pranav Pagote\\Downloads\\exercise.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)

url = ''
for lines in range(len(data_lines)):
    url = url + data_lines[lines][lines]
print(url)

f = open('C:\\Users\\Pranav Pagote\\Downloads\\Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
for pdf_page in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pdf_page)
    phonePattern = re.compile(r'(\d{3}).(\d{3}).(\d{4})')
    phone = re.search(phonePattern, page.extractText())
    print(phone)
    if (phone != None):
        print(phone.group())
""" 
file_write = open('C:\\Users\\Pranav Pagote\\Downloads\\writer.csv', mode='w', newline='')
csv_writer = csv.writer(file_write, delimiter=',')
csv_writer.writerow(['1','2', '3'])

csv_writer.writerows([['4', '5', '6'], ['7', '8', '9']])
file_write.close()

f = open('C:\\Users\\Pranav Pagote\\Downloads\\Some_BrandNew_Doc.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)
first_page = pdf_reader.getPage(0)
print(first_page.extractText())

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)

pdf_output = open('C:\\Users\\Pranav Pagote\\Downloads\\newPdf.pdf', 'wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()

 """