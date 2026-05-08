"""
"""

import requests
from config import API_KEY, URL

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def uso_api_ollama(frase):
    prompt = f"""
Clasifica la siguiente frase en una sola categoría.

Categorías permitidas:
deportes, crónica roja, política, economía, salud, educación, tecnología.
Cuando no tengas claro que categoría, usar: sin categoria
Responde únicamente con el nombre de la categoría.

Frase:
"{frase}"
"""

    data = {
            "model": "mistral-small-latest",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0,
            "max_tokens": 20
        }

    response = requests.post(URL, headers=HEADERS, json=data)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"].strip().lower()


def clasificar():
    archivo = open("data/noticias_cortas_500.csv", "r")
    lineas = archivo.readlines()
    lineas = [s.replace("\n", "") for s in lineas]
    lineas = [s.split("|") for s in lineas]
    lineas = lineas[0:]
    for l in lineas[1:20]:
        print(l[2])
        print(l[3])
        print(uso_api_ollama(l[2]))
        print("--------------------")

if __name__ == "__main__":
    clasificar()
