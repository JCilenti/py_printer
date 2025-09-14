from escpos.printer import Usb
from pypdf import PdfReader
"""Seiko Epson Corp. Interface Card UB-U05 for Thermal Receipt Printers"""
p = Usb(0x04b8,0x0202, profile="TM-T88IV")
#print(type(p))

#task_name = input("Please Enter the Task to Complete: ")
'''
due_date = input("When is the task due? (Ex. TTTT, MMDDYYY: ")
task_notes = ("Please Enter Any Notes for the Task: ")
# print the entire task and details to the screen and press enter to submit
# consider generating a QR code here for the task or notes related to it
p.text("Task: " + task_name + "\n")
p.text("Due: " + due_date + "\n")
p.text("Notes: " + task_notes + "\n")
p.barcode('4006381333931', 'EAN13', 64, 2, '', '')
'''

#p.text("Task: " + task_name + "\n")
p.text("mixed veggies\n")
p.text("pie crust\n")
p.text("cream of chicken soup\n")
p.text("aluminum foil\n")
p.text("chicken\n")
p.text("olive oil spray\n\n\n")
p.image("rickroll.png")

p.cut()

