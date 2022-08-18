from modelos import Modelo

def main():
    producto = Modelo(9, 'Sandwich de cordero', 30)
    print(producto.json())


if __name__ == '__main__':
    main()