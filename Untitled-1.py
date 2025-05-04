import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
import json

FISIER = "buget_gui.json"

# Încarcă datele
try:
    with open(FISIER, "r") as f:
        tranzactii = json.load(f)
except FileNotFoundError:
    tranzactii = []

# Salvează datele
def salveaza():
    with open(FISIER, "w") as f:
        json.dump(tranzactii, f, indent=2)

# Adaugă o tranzacție
def adauga_tranzactie():
    tip = tip_var.get()
    suma = suma_entry.get()
    categorie = categorie_entry.get()
    descriere = descriere_entry.get()

    if not suma or not categorie or not tip:
        messagebox.showerror("Eroare", "Completează toate câmpurile.")
        return

    try:
        suma = float(suma)
    except:
        messagebox.showerror("Eroare", "Sumă invalidă.")
        return

    tranzactie = {
        "data": str(date.today()),
        "tip": tip,
        "categorie": categorie,
        "suma": suma,
        "descriere": descriere
    }

    tranzactii.append(tranzactie)
    salveaza()
    actualizeaza_lista()
    actualizeaza_buget()

    # Clear inputs
    suma_entry.delete(0, tk.END)
    categorie_entry.delete(0, tk.END)
    descriere_entry.delete(0, tk.END)

# Actualizează lista de tranzacții
def actualizeaza_lista():
    lista_tranzactii.delete(*lista_tranzactii.get_children())
    for t in tranzactii:
        lista_tranzactii.insert('', tk.END, values=(t["data"], t["tip"], t["categorie"], t["suma"], t["descriere"]))

# Calculează și afișează bugetul
def actualizeaza_buget():
    total = 0
    for t in tranzactii:
        if t["tip"] == "venit":
            total += t["suma"]
        else:
            total -= t["suma"]
    buget_var.set(f"Buget total: {total:.2f} lei")

# === Interfață ===
root = tk.Tk()
root.title("Aplicație Buget Personal")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Tip:").grid(row=0, column=0)
tip_var = tk.StringVar()
ttk.Combobox(frame, textvariable=tip_var, values=["venit", "cheltuiala"], width=15).grid(row=0, column=1)

tk.Label(frame, text="Sumă:").grid(row=1, column=0)
suma_entry = tk.Entry(frame)
suma_entry.grid(row=1, column=1)

tk.Label(frame, text="Categorie:").grid(row=2, column=0)
categorie_entry = tk.Entry(frame)
categorie_entry.grid(row=2, column=1)

tk.Label(frame, text="Descriere:").grid(row=3, column=0)
descriere_entry = tk.Entry(frame)
descriere_entry.grid(row=3, column=1)

tk.Button(frame, text="Adaugă", command=adauga_tranzactie).grid(row=4, column=0, columnspan=2, pady=5)

# Tabel tranzacții
lista_tranzactii = ttk.Treeview(root, columns=("data", "tip", "categorie", "suma", "descriere"), show="headings")
for col in lista_tranzactii["columns"]:
    lista_tranzactii.heading(col, text=col.capitalize())
lista_tranzactii.pack(pady=10)

# Buget total
buget_var = tk.StringVar()
tk.Label(root, textvariable=buget_var, font=("Arial", 14)).pack()

# Inițializare
actualizeaza_lista()
actualizeaza_buget()

root.mainloop()
