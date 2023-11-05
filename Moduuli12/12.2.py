import requests

def hae_saatiedot(api_avain, paikkakunta):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_avain}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        sateen_kuvaus = data["weather"][0]["description"]
        lampotila_kelvin = data["main"]["temp"]
        lampotila_celsius = lampotila_kelvin - 273.15  # Kelvin -> Celsius
        return sateen_kuvaus, lampotila_celsius
    else:
        return None, None

def main():
    api_avain = "TÄHÄN_SYÖTÄ_API_AVAIN"
    paikkakunta = input("Anna paikkakunnan nimi: ")

    sateen_kuvaus, lampotila_celsius = hae_saatiedot(api_avain, paikkakunta)

    if sateen_kuvaus is not None and lampotila_celsius is not None:
        print(f"Sää paikkakunnalla {paikkakunta}:")
        print(f"Kuvaus: {sateen_kuvaus}")
        print(f"Lämpötila: {lampotila_celsius:.2f} °C")
    else:
        print("Säätietojen hakeminen epäonnistui.")

if __name__ == "__main__":
    main()
