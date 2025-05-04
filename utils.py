import requests

def curs_valutar(moneda):
    try:
        moneda = moneda.upper()
        if moneda == "RON":
            return 1.0

        url = f"http://www.floatrates.com/daily/{moneda.lower()}.json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "ron" in data:
            return float(data["ron"]["rate"])
        else:
            print(f"Moneda necunoscută: {moneda}. Folosesc suma originală.")
            return None
    except Exception as e:
        print(f"Eroare la obținerea cursului: {e}")
    return None