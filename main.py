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
            { "codigo": "JO-001", "cantidad": 4 },
            { "codigo": "JO-002", "cantidad": 5 }
        ]
    },
    {
        "nombre": "Ana López",
        "fecha": "2024-10-02",
        "compras": [
            { "codigo": "JO-003", "cantidad": 2 },
            { "codigo": "JO-005", "cantidad": 3 }
        ]
    },
    {
        "nombre": "Juan Pérez",
        "fecha": "2024-10-01",
        "compras": [
            { "codigo": "JO-004", "cantidad": 1 },
            { "codigo": "JO-006", "cantidad": 2 }
        ]
    },
    {
        "nombre": None,
        "fecha": "2024-10-03",
        "compras": [
            { "codigo": "JO-007", "cantidad": 5 },
            { "codigo": "JO-008", "cantidad": 2 }
        ]
    },
    {
        "nombre": "Carlos García",
        "fecha": "2024-10-03",
        "compras": [
            { "codigo": "JO-001", "cantidad": 1 },
            { "codigo": "JO-004", "cantidad": 2 }
        ]
    },
    {
        "nombre": "María Fernández",
        "fecha": "2024-10-04",
        "compras": [
            { "codigo": "JO-002", "cantidad": 3 },
            { "codigo": "JO-006", "cantidad": 1 }
        ]
    },
    {
        "nombre": None,
        "fecha": "2024-10-05",
        "compras": [
            { "codigo": "JO-003", "cantidad": 4 },
            { "codigo": "JO-005", "cantidad": 1 }
        ]
    },
    {
        "nombre": "Luis Martínez",
        "fecha": "2024-10-05",
        "compras": [
            { "codigo": "JO-007", "cantidad": 5 },
            { "codigo": "JO-008", "cantidad": 2 }
        ]
    },
    {
        "nombre": "Sofía Ramírez",
        "fecha": "2024-10-06",
        "compras": [
            { "codigo": "JO-003", "cantidad": 4 },
            { "codigo": "JO-005", "cantidad": 1 }
        ]
    },
    {
        "nombre": "David Torres",
        "fecha": "2024-10-07",
        "compras": [
            { "codigo": "JO-001", "cantidad": 2 },
            { "codigo": "JO-007", "cantidad": 3 }
        ]
    },
    {
        "nombre": "Lucía González",
        "fecha": "2024-10-08",
        "compras": [
            { "codigo": "JO-002", "cantidad": 1 },
            { "codigo": "JO-006", "cantidad": 4 }
        ]
    },
    {
        "nombre": "Fernando Díaz",
        "fecha": "2024-10-09",
        "compras": [
            { "codigo": "JO-004", "cantidad": 2 },
            { "codigo": "JO-008", "cantidad": 3 }
        ]
    },
    {
        "nombre": None,
        "fecha": "2024-10-10",
        "compras": [
            { "codigo": "JO-005", "cantidad": 1 },
            { "codigo": "JO-003", "cantidad": 2 }
        ]
    },
    {
        "nombre": "Claudia Herrera",
        "fecha": "2024-10-10",
        "compras": [
            { "codigo": "JO-002", "cantidad": 3 },
            { "codigo": "JO-006", "cantidad": 1 }
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
semanas = []
for i in range(0, 4):
    dic = {"semana": i+1,  "compra": []}
    for j in range(i*7 - 1, (i+1)*7): #iterar por toda la semana
        for compra in compras:
            if compra["fecha"] == f"2024-10-{f"0{j}" if j< 10 else j}": #Revisar que este en esa semana
                dic["compra"].append({"nombre": compra["nombre"], "compras": compra["compras"]})

    semanas.append(dic)
#Combinar las compras de una misma semana con mismo nombre:
for  semana in semanas:
    for i in range(len(semana["compra"])-1):
        for j in range(i +1, len(semana["compra"])-1):
            if semana["compra"][i]["nombre"] == semana["compra"][j]["nombre"]:
                semana["compra"][i] = combineCompras(semana["compra"][i], semana["compra"][j])
                semana["compra"].pop(j)

#
for semana in semanas:
    dic = {"Semana": semana["semana"]}
    mejoresCompradores= []
    mejoresArtitculos= []

    #Obtener los tres mejores compradores
    for register in semana["compra"]:
        if register["nombre"] == None:#Se debe tener registro del nombre
            continue
        price = getPrice(register)
        if len(mejoresCompradores) == 3 and  price > mejoresCompradores[2]["total"]:
            mejoresCompradores[2] = {"nombre": register["nombre"], "total": price}
        elif len(mejoresCompradores) < 3:
            mejoresCompradores.append({"nombre": register["nombre"], "total": price})
    
    dic["compradores"] = mejoresCompradores


    for art in articulos:
        count = 0
        for register in semana["compra"]:
            for compra in register["compras"]:
                if compra["codigo"] == art ["codigo"]:
                    count += compra["cantidad"]
        if len(mejoresArtitculos) == 3 and count > mejoresArtitculos[2]["total"]:
            mejoresArtitculos[2] = {"codigo": art["codigo"], "total": count}
        elif len(mejoresCompradores) < 3:
            mejoresArtitculos.append({"codigo": art["codigo"], "total": count})
    #Convertir el total de cantidad a precio
    for art in mejoresArtitculos:
        for arti in articulos:
            if arti["codigo"] == art["codigo"]:
                art["total"] = arti["valor"] * art["total"]
    
    dic["articulos"] = mejoresArtitculos
    if  len(mejoresCompradores) > 0: #No dar info vacia
         continue

    output[1]["porSemana"].append(dic)

print(output)