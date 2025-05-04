aprobados = 0
noAprobados = 0 

for i in range(6):
    nota = int(input("Ingrese su nota: "))
    
    if nota > 1:
        aprobados += 1
    else: 
        noAprobados += 1
    
print(f"Los alumnos que aprobaron son: {aprobados}")
print(f"Los alumnos que no aprobaron son: {noAprobados}")
