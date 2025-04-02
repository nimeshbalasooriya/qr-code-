import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter text to generate QR code")
        return
    
    global qr
    qr = qrcode.make(data)
    qr = qr.resize((200, 200))
    qr_img = ImageTk.PhotoImage(qr)
    
    qr_label.config(image=qr_img)
    qr_label.image = qr_img

def save_qr():
    if 'qr' not in globals():
        messagebox.showerror("Error", "No QR code generated to save")
        return
    
    filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
    if filepath:
        qr.save(filepath)
        messagebox.showinfo("Success", "QR Code saved successfully")

# Tkinter window setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("350x500")
root.configure(bg="#2C3E50")

# Title Label
title_label = tk.Label(root, text="QR Code Generator", font=("Arial", 16, "bold"), bg="#2C3E50", fg="#ECF0F1")
title_label.pack(pady=10)

# Entry field
entry_frame = tk.Frame(root, bg="#2C3E50")
entry_frame.pack(pady=10)
entry = tk.Entry(entry_frame, width=30, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=5)

# Generate Button
button = tk.Button(root, text="Generate QR Code", font=("Arial", 12, "bold"), bg="#3498DB", fg="white", padx=10, pady=5, command=generate_qr)
button.pack(pady=10)

# Label to display QR Code
qr_label = tk.Label(root, bg="#2C3E50")
qr_label.pack(pady=10)

# Save Button
save_button = tk.Button(root, text="Save QR Code", font=("Arial", 12, "bold"), bg="#27AE60", fg="white", padx=10, pady=5, command=save_qr)
save_button.pack(pady=10)

# Footer Label
footer_label = tk.Label(root, text="Developed by NHB LK", font=("Arial", 10, "italic"), bg="#2C3E50", fg="#ECF0F1")
footer_label.pack(pady=10)

root.mainloop()
