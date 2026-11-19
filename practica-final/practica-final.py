tipo_cambio_euro_peso = 23.70
tipo_cambio_dolar_peso = 20.75
tipo_conversion_euro_dolar = input("Ingrese el tipo de conversión (euro/dolar): ")
if tipo_conversion_euro_dolar.lower() == "euro":
    monto_euro = float(input("Ingrese el monto a convertir en euros: "))
    conversion = monto_euro * tipo_cambio_euro_peso
    print(f"{monto_euro} euros equivalen a {conversion} pesos.")
elif tipo_conversion_euro_dolar.lower() == "dolar":
    monto_dolar = float(input("Ingrese el monto a convertir en dólares: "))
    conversion = monto_dolar * tipo_cambio_dolar_peso
    print(f"{monto_dolar} dólares equivalen a {conversion} pesos.")
else:
    print("Tipo de conversión no válido.")
