class Modelo:
    def __init__(self, id_producto, nombre_producto, precio_producto):
        self.id = id_producto
        self.nombre = nombre_producto
        self.precio = precio_producto

    def json(self):
        return {
            "productId": self.id,
            "productName": self.nombre
        }