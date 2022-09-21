nombre = input("Nombre masculino: ")
nombre1 = input("Nombre femenino: ")
verbo1 = input("Verbo: ")
verbo1_plural = input("El mismo verbo pero en plural: ")
verbo2 = input("Verbo: ")
animal = input("Animal: ")
adj = input("Adjetivo: ")
adj2 = input("Adjetivo: ")


madlib = f"""
En una casa había un niño llamado {nombre}, era muy {adj} y le gustaba
 mucho {verbo1},
lo hacía todos los días. Cuando viene su {adj2} amiga, {nombre1}. {nombre} 
y
 {nombre1} {verbo1_plural}
todo el día, cuando {nombre1} se iba a su casa, {nombre}
 se quedaba solo a {verbo2},
después se iba a dormir y soñaba con tener un {animal}."""

print(madlib)
