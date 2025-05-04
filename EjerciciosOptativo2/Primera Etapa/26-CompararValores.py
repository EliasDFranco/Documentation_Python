producto1Name = input("Ingrese el nombre del producto 1: ")
producto1Precio = float(input("Ingrese elprecio del producto uno: "))

producto2Name = input("Ingrese el nombre del producto 2: ")
producto2Precio = float(input("Ingrese elprecio del producto dos: "))
                        
producto3Name = input("Ingrese el nombre del producto 3: ")
producto3Precio = float(input("Ingrese elprecio del producto tres: "))

if producto1Precio > producto2Precio and producto1Precio > producto3Precio:
    productoMasCaro = producto1Name
    mayorPrecio = producto1Precio
    
elif producto2Precio > producto1Precio and producto2Precio > producto3Precio:
    productoMasCaro = producto2Name
    mayorPrecio = producto2Precio
    
else: 
    productoMasCaro = producto3Name 
    mayorPrecio = producto3Precio 


print(f"El producto más caro es: {productoMasCaro} y su precio es: {mayorPrecio}")
