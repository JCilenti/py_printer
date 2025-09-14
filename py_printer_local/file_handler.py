from pypdf import PdfReader
from escpos.printer import Usb
from pypdf import PdfReader
"""Seiko Epson Corp. Interface Card UB-U05 for Thermal Receipt Printers"""
p = Usb(0x04b8,0x0202, profile="TM-T88IV")

reader = PdfReader("doc.pdf")
number_of_pages = len(reader.pages)
print(f"Number of pages: {number_of_pages}")

page = reader.pages[0] # first page
text = page.extract_text()
#p.text(text)
print(f"Text from first page:\n{text}")
p.image("weather.png")
p.cut()
