import tkinter as Tk
from tkinter import filedialog, simpledialog, messagebox
import qrcode

# Ask user for file name
file_name = simpledialog.askstring("Input", "Enter name of your file:")
# Create the main Tkinter window
root = Tk.Tk()
root.attributes('-fullscreen', True)


# If no name is given, set a default name
if not file_name:
    file_name = "qr_code"

def input_image():
    file_path = filedialog.askopenfilename(
        title="Select a QR File",
        filetypes=[("Text Files", "*.txt")]
    )

    if not file_path:  # If user cancels, return
        return
    
    with open(file_path, "r", encoding="utf-8") as file:
        qr_data = file.read().strip()  # Read entire file and remove extra spaces

    print(f"QR loaded from {file_path}")

    # Generate the QR code
    qr_img = qrcode.make(qr_data)
    qr_img.save(f"{file_name}.png")  # Save using the entered file name
    print(f"QR Code saved as {file_name}.png")

    messagebox.showinfo("Dialog Box", f"QR code saved successfully as {file_name}.png")
    root.destroy()

# Create the upload button
btn_qr = Tk.Button(root, text="Upload QR File", command=input_image, width=15, height=2)
btn_qr.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
