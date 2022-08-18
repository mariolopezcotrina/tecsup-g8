from modelos import Modelo
from data import productos


def main():
    print("Aplicacion de inventarios")
    print("=========================")
    print("COMANDOS:")
    print(" filtrar: muestra los productos en formato json")
    print(" cerrar: cierra la aplicacion")
    while True:
        comando = input("Ingrese el comando: ")
        if comando == "filtrar":
            resultados = []
            for producto in productos:
                producto_json = Modelo(
                    producto["id"], producto["nombre"], producto["precio"]
                )
                resultados.append(producto_json.json())

            print(
                {
                    "success": True,
                    "message": "La data se ha cargado correctamente",
                    "content": resultados,
                }
            )
        elif comando == "cerrar":
            break
        else:
            print("Comando incorrecto, pruebe otra vez")


if __name__ == "__main__":
    main()