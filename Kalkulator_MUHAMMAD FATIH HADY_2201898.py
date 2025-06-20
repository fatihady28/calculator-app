import tkinter as tk
from tkinter import ttk

# membuat window
window = tk.Tk()
window.title("Kalkulator by Fatih")
window.geometry("220x230")
window.resizable(False,False)

# fungsi untuk melakukan penjumlahan
def tambah():
    hasil = int(angka1.get()) + int(angka2.get())
    label_hasil.config(text="Hasil: " + str(hasil))

# fungsi untuk melakukan pengurangan
def kurang():
    hasil = int(angka1.get()) - int(angka2.get())
    label_hasil.config(text="Hasil: " + str(hasil))

# fungsi untuk melakukan penambahan
def kali():
    hasil = int(angka1.get()) * int(angka2.get())
    label_hasil.config(text="Hasil: " + str(hasil))

# fungsi untuk melakukan pembagian
def bagi():
    hasil = int(angka1.get()) / int(angka2.get())
    label_hasil.config(text="Hasil: " + str(hasil))

# menambahkan label untuk input angka pertama
label_angka1 = ttk.Label(text="Angka pertama:")
label_angka1.pack()

# menambahkan input untuk angka pertama
angka1 = ttk.Entry()
angka1.pack()

# menambahkan label untuk input angka kedua
label_angka2 = ttk.Label(text="Angka kedua:")
label_angka2.pack()

# menambahkan input untuk angka kedua
angka2 = ttk.Entry()
angka2.pack()

# menambahkan tombol untuk penjumlahan
tombol_tambah = ttk.Button(text="+", command=tambah)
tombol_tambah.pack()

# menambahkan tombol untuk pengurangan
tombol_kurang = ttk.Button(text="-", command=kurang)
tombol_kurang.pack()

# menambahkan tombol untuk penambahan
tombol_kali = ttk.Button(text="*", command=kali)
tombol_kali.pack()

# menambahkan tombol untuk pembagian
tombol_bagi = ttk.Button(text="/", command=bagi)
tombol_bagi.pack()

# menambahkan label untuk hasil
label_hasil = ttk.Label(text="Hasil: ")
label_hasil.pack()

# menjalankan loop untuk window
window.mainloop()
