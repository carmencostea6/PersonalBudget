import tkinter as tk
from tkinter import ttk, messagebox
from model import Tranzactie, ManagerBuget
from utils import curs_valutar

class InterfataGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("💰 Buget Personal")
        self.root.configure(bg="#f0f4f7")
        self.buget = ManagerBuget()

        self.font = ("Calibri", 11)
        self.init_ui()

    def init_ui(self):
        # === Frame de sus: Form ===
        frame_form = tk.Frame(self.root, bg="#f0f4f7")
        frame_form.pack(padx=20, pady=10)

        tk.Label(frame_form, text="Tip:", bg="#f0f4f7", font=self.font).grid(row=0, column=0, sticky="w")
        self.tip_var = tk.StringVar()
        self.tip_box = ttk.Combobox(frame_form, textvariable=self.tip_var, values=["venit", "cheltuiala"])
        self.tip_box.grid(row=0, column=1)
        self.tip_box.bind("<<ComboboxSelected>>", self.actualizeaza_categorii)

        tk.Label(frame_form, text="Sumă:", bg="#f0f4f7", font=self.font).grid(row=1, column=0, sticky="w")
        self.suma_entry = tk.Entry(frame_form, font=self.font)
        self.suma_entry.grid(row=1, column=1)

        tk.Label(frame_form, text="Monedă:", bg="#f0f4f7", font=self.font).grid(row=2, column=0, sticky="w")
        self.moneda_var = tk.StringVar()
        self.moneda_box = ttk.Combobox(frame_form, textvariable=self.moneda_var, values=["RON", "EUR", "USD"])
        self.moneda_box.grid(row=2, column=1)

        tk.Label(frame_form, text="Categorie:", bg="#f0f4f7", font=self.font).grid(row=3, column=0, sticky="w")
        self.categorii_cheltuieli = ["Mâncare", "Utilități", "Vacanță", "Haine", "Medicamente", "Iesiri în oraș", "Altele"]
        self.categorii_venituri = ["Salariu", "Bursă", "Cadou", "Altele"]
        self.cat_var = tk.StringVar()
        self.cat_box = ttk.Combobox(frame_form, textvariable=self.cat_var, values=[])

        self.cat_box.grid(row=3, column=1)

        tk.Label(frame_form, text="Descriere:", bg="#f0f4f7", font=self.font).grid(row=4, column=0, sticky="w")
        self.desc_entry = tk.Entry(frame_form, font=self.font)
        self.desc_entry.grid(row=4, column=1)

        self.btn_adauga = tk.Button(frame_form, text="➕ Adaugă", bg="#4CAF50", fg="white", font=self.font, command=self.adauga)
        self.btn_adauga.grid(row=5, column=0, columnspan=2, pady=10)
        self.btn_adauga.bind("<Enter>", lambda e: self.btn_adauga.config(bg="#388e3c"))
        self.btn_adauga.bind("<Leave>", lambda e: self.btn_adauga.config(bg="#4CAF50"))

        # === Tabel tranzacții ===
        self.tree = ttk.Treeview(self.root, columns=("data", "tip", "categorie", "suma", "moneda", "suma in lei", "descriere"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=100)
        self.tree.pack(padx=20, pady=10, fill="x")

        # === Buton ștergere ===
        self.btn_sterge = tk.Button(self.root, text="🗑️ Șterge tranzacție", bg="#e53935", fg="white", font=self.font, command=self.sterge)
        self.btn_sterge.pack(pady=5)
        self.btn_sterge.bind("<Enter>", lambda e: self.btn_sterge.config(bg="#c62828"))
        self.btn_sterge.bind("<Leave>", lambda e: self.btn_sterge.config(bg="#e53935"))

        # === Label buget ===
        self.buget_var = tk.StringVar()
        tk.Label(self.root, textvariable=self.buget_var, font=("Calibri", 14, "bold"), bg="#f0f4f7").pack(pady=10)

        self.actualizeaza()

    def adauga(self):
        try:
            tranzactie = Tranzactie(
                tip=self.tip_var.get(),
                suma=self.suma_entry.get(),
                moneda=self.moneda_var.get(),
                categorie=self.cat_var.get(),
                descriere=self.desc_entry.get()
            )
            self.buget.adauga(tranzactie)
            self.clear_inputs()
            self.actualizeaza()
        except Exception as e:
            messagebox.showerror("Eroare", f"Tranzacție invalidă: {e}")

    def sterge(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Info", "Selectează o tranzacție.")
            return
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete?")
        if confirm:
            idx = int(sel[0])
            self.buget.sterge(idx)
            self.actualizeaza()

    def clear_inputs(self):
        self.tip_var.set("")
        self.suma_entry.delete(0, tk.END)
        self.moneda_var.set("")
        self.cat_var.set("")
        self.desc_entry.delete(0, tk.END)

    def actualizeaza(self):
        self.tree.delete(*self.tree.get_children())
        for i, t in enumerate(self.buget):
            self.tree.insert('', tk.END, iid=i, values=(t.data, t.tip, t.categorie, t.suma, t.moneda, t.suma_lei, t.descriere))
        self.buget_var.set(f"💸 Buget total: {self.buget.buget_total():.2f} lei")
    def actualizeaza_categorii(self, event=None):
        tip_selectat = self.tip_var.get()
        if tip_selectat == "venit":
         self.cat_box['values'] = self.categorii_venituri
        else:
             self.cat_box['values'] = self.categorii_cheltuieli
        self.cat_var.set("")  # Resetează selecția curentă
