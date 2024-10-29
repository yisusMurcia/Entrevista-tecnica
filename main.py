# Lista de artículos
articulos = [
    {"codigo": "JO-001", "nombre": "Chocolate Amargo", "tipo": "dulce", "valor": 500},
    {"codigo": "JO-002", "nombre": "Gomitas", "tipo": "dulce", "valor": 300},
    {"codigo": "JO-003", "nombre": "Caramelo", "tipo": "dulce", "valor": 200},
    {"codigo": "JO-004", "nombre": "Chicle Menta", "tipo": "dulce", "valor": 100},
    {"codigo": "JO-005", "nombre": "Agua Mineral", "tipo": "bebida", "valor": 1600},
    {"codigo": "JO-006", "nombre": "Papas Fritas", "tipo": "snack", "valor": 1200},
    {"codigo": "JO-007", "nombre": "Gaseosa", "tipo": "bebida", "valor": 2500},
    {"codigo": "JO-008", "nombre": "Maní Salado", "tipo": "snack", "valor": 500}
]

compras = [
    {
        "nombre": "Juan Pérez",
        "fecha": "2024-10-01",
        "compras": [
            {"codigo": "JO-001", "cantidad": 4},
            {"codigo": "JO-002", "cantidad": 5}
        ]
    },
    {
        "nombre": "Juan Pérez",
        "fecha": "2024-10-02",
        "compras": [
            {"codigo": "JO-006", "cantidad": 6},
            {"codigo": "JO-002", "cantidad": 5}
        ]
    },
    {
        "nombre": "Ana López",
        "fecha": "2024-10-02",
        "compras": [
            {"codigo": "JO-003", "cantidad": 2},
            {"codigo": "JO-005", "cantidad": 3}
        ]
    }
]

def getNameByCode(code):
    for articulo in articulos:
        if articulo["codigo"] == code:
            return articulo["nombre"]


def getPrice(obj):
    price = 0
    for art in obj["compras"]:
        value = 0
        for arti in articulos:
            if arti["codigo"] == art["codigo"]:
                value = arti["valor"]
                break
        price += value * art["cantidad"]
    return price

def getMostBuyedArt(obj):
    articule = ""
    amount = 0
    for art in obj["compras"]:
        if art["cantidad"] > amount:
            articule = getNameByCode(art["codigo"])
            amount = art["cantidad"]

    return [articule, amount]

def combineCompras(compras, register):
    for compra in compras["compras"]:
        mismaCompra = False
        for compraInRegister in register["compras"]:
            if compra["codigo"] == compraInRegister["codigo"]:
                compraInRegister["cantidad"] += compra["cantidad"]
                mismaCompra = True
        if not mismaCompra:
            register["compras"].append(compra)
    
    return register


#Agrupar compras por día
comprasPorDia=[
    #{"fecha": ----, "compras": []}"
]
for compra in compras:
    #Revisar si el día esta en al array
    added = False
    for  fecha in comprasPorDia:
        if fecha["fecha"] == compra["fecha"]:
            #Revisar que el nombre no este en esa fecha
            for register in fecha["compras"]:
                if register["nombre"] == compra["nombre"]:
                    register = combineCompras(compra, register)
            #Si esta, agregar la compra
            fecha["compras"].append({"nombre":compra["nombre"], "compras": compra["compras"]})

            added = True
            break
    if not added:
        comprasPorDia.append({"fecha": compra["fecha"], "compras": [{"nombre":compra["nombre"], "compras": compra["compras"]}]})

output= [
    {"porDia":[
    ]},
    {"porSemana":[

    ]}
]
for dia in comprasPorDia:
    bestBuyer = ""
    priceBestBuy = 0

    article = ["", 0]
    for compra in dia["compras"]:
        if compra["nombre"] != None:
            price = getPrice(compra)
            if price > priceBestBuy:
                priceBestBuy = price
                bestBuyer = compra["nombre"]
        if getMostBuyedArt(compra)[1] > article[1]:
            article = getMostBuyedArt(compra)

    output[0]["porDia"].append({
        "fecha": dia["fecha"],
        "comprador":  bestBuyer,
        "dulce": article[0]
    })

#Por semana
semana = 1
for i in range(6, 31,  7):
    semana += 1 #Pasar a la siguiente semana


print(output)