import requests
# Tu clave de API
api_key = "7cb78ea8fa27033ae2e9cdee8ee0f267"
# Ciudad de interés{}[]
city = "La Paz"
# URL base de la API
base_url = f"http:/
/api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Hacer la solicitud
response = requests.get(base_url)
if response.status_code == 200:
    data = response.json()
    # Extraer datos útiles
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"En {city}, el clima es '{weather}' con una temperatura de {temperature}°C.")
else:
    print("Error al obtener datos de la API.")
