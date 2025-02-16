from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if self.buscar_producto_por_id(producto.get_id()) is None:
            self.productos.append(producto)
            print(f"Producto '{producto.get_nombre()}' agregado al inventario.")
        else:
            print(f"Error: Ya existe un producto con el ID {producto.get_id()}.")

    def eliminar_producto(self, id_producto):
        producto = self.buscar_producto_por_id(id_producto)
        if producto:
            self.productos.remove(producto)
            print(f"Producto '{producto.get_nombre()}' eliminado del inventario.")
        else:
            print(f"Error: No se encontró ningún producto con el ID {id_producto}.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = self.buscar_producto_por_id(id_producto)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print(f"Producto '{producto.get_nombre()}' actualizado.")
        else:
            print(f"Error: No se encontró ningún producto con el ID {id_producto}.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def buscar_producto_por_id(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                return producto
        return None

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for producto in self.productos:
                print(producto)