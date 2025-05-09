import requests

class APIClient:
    def Obtener_Animal(self, nombre_vernaculo):
        url = "https://www.datos.gov.co/resource/wizt-zh64.json"
        parametros = { "$where": f"upper(nombre_vernaculo) like upper('%{nombre_vernaculo}%')" }
        response = requests.get(url, params=parametros)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener datos: {response.status_code}")

if __name__ == "__main__":
    while True:
        nombre_vernaculo = input("Ingrese el nombre del animal que desea buscar: ")
        if not nombre_vernaculo.strip():
            print("Por favor se necesita un nombre para la busqueda")
            continue
        if nombre_vernaculo == " ":
            print("No se permiten espacios en blanco ")
        
            


        api = APIClient()
        resultados = api.Obtener_Animal(nombre_vernaculo)
    

        if resultados:
            for i, item in enumerate(resultados, start=1):
                print(f"{i}. Nombre común: {item.get('nombre_vernaculo', 'nombre_vernaculo')}")
                print(f"   Nombre científico: {item.get('nombre_cientifico', 'nombre_cientifico')}")
                print(f"   Reino: {item.get('reino', 'reino')}")
                print(f"   Familia: {item.get('familia', 'familia')}")
                print(f"   Estado de conservación: {item.get('estado_de_amenaza', 'estado_de_amenaza')}")
                print(" ")
        else:
            print("No se encontraron resultados para ese animal.")

        opcion = input("¿Desea buscar otro animal? (1 = Sí, 0 = No): ").strip()
        if opcion != "1":
                print(" Gracias por usar el programa.")
                break


