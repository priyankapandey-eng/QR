# Documentation: QR Code Generator with Tkinter GUI
# Overview
This script provides a graphical interface that allows the user to upload a .txt file, generate a QR code from its contents, and save the QR code as a PNG image. The user is prompted to enter a custom name for the output file. The GUI is built using the tkinter library, and QR code generation is handled by the qrcode library.

# Dependencies
The following Python modules are required:

tkinter – For GUI elements (Tk, filedialog, simpledialog, messagebox)

qrcode – For generating QR codes

# Output
A PNG image file containing the QR code is saved in the working directory.

The filename is based on user input (e.g., my_qr.png), or "qr_code.png" if no name is entered.

# User Instructions
Run the script.

When prompted, enter a name for the QR code image.

Click "Upload QR File".

Select a .txt file containing the data you want to encode.

A QR code will be saved as an image in the current directory
