def calculadoraPromedio(nota1, nota2, nota3, nota4):
    return (nota1 +  nota2 + nota3 + nota4 ) / 4 

materia1 = input("Ingrese el nombre de la materia uno: ")
nota1 = float(input(f"Ingrese la nota de la {materia1}: "))

materia2 = input("Ingrese el nombre de la materia dos: ")
nota2 = float(input(f"Ingrese la nota de la {materia2}: "))

materia3 = input("Ingrese el nombre de la materia tres: ")
nota3 = float(input(f"Ingrese la nota de la {materia3}: "))

materia4 = input("Ingrese el nombre de la materia cuatro: ")
nota4 = float(input(f"Ingrese la nota de la {materia4}: "))


respuestaPromedio = calculadoraPromedio(nota1, nota2, nota3, nota4)

materias = [materia1, materia2, materia3, materia4]
notas = [nota1,nota2,nota3, nota4]

menor = notas.index(min(notas))
materiaMenor = materias[menor]
notaMenor = notas[menor]

print("El promedio de estas cuatro notas es: ", respuestaPromedio)
print(f"La materia con menor nota es: {materiaMenor}, y su nota es: {notaMenor}")
