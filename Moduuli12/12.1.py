import requests

def hae_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        vitsi = data["value"]
        return vitsi
    else:
        return "Vitsin hakeminen epäonnistui."

def main():
    print("Tässä on satunnainen Chuck Norris -vitsi:")
    vitsi = hae_chuck_norris_vitsi()
    print(vitsi)

if __name__ == "__main__":
    main()
