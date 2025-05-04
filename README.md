# PersonalBudge# 💰 Buget Personal - Aplicație Python cu GUI

Aceasta este o aplicație simplă de gestionare a bugetului personal, dezvoltată în Python.  
Poți adăuga venituri și cheltuieli în RON, EUR sau USD, iar sumele în valută sunt convertite automat în lei folosind cursul valutar BNR actual.

## Funcționalități

- Adăugare de tranzacții (venituri și cheltuieli)
- Conversie automată EUR/USD -> RON pe baza cursului oficial BNR
- Salvarea datelor într-un fișier .json
- Interfață grafică intuitivă (Tkinter)
- Tabel cu tranzacțiile introduse
- Calculul bugetului total
- Categorii dinamice în funcție de tipul tranzacției

## Categorii disponibile

- *Venit*: Salariu, Bursă, Cadou, Altele  
- *Cheltuială*: Mâncare, Utilități, Vacanță, Haine, Medicamente, Ieșiri în oraș, Altele

## Tehnologii folosite

- Python 3
- Tkinter (pentru GUI)
- BeautifulSoup + Requests (pentru web scraping curs valutar BNR)
- JSON (pentru salvarea datelor)

## Instalare

1. Clonează acest repo:
   ```bash
   git clone https://github.com/utilizator/buget-personal.git
   cd buget-personal
