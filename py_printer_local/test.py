import escpos
from escpos.printer import Usb

p = Usb(0x04b8,0x0202, profile="TM-T88IV")
p.text("Hello, ESC/POS!\n")
p.set(align='center', bold=True, size='2x2')
p.text("Centered and Bold Text\n")
p.set(align='left', bold=False, size='normal') # Reset formatting
p.cut()
