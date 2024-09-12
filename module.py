estudantes = [{"nome": "Alice", "notas": [8.5, 9.0, 7.5], "curso": "Matemática"},
		{"nome": "Bob", "notas": [6.0, 5.5, 7.0], "curso": "Física"},
		{"nome": "Charlie", "notas": [9.5, 8.0, 9.0], "curso": "Computação"}]

def filtrar_aprovados(estudante):
    nota_soma = 0
    for nota in estudante["notas"]:
        nota_soma += nota    
    return nota_soma/  len(estudante["notas"]) >= 7


def add_media(estudante):
    nota_soma = 0
    for nota in estudante["notas"]:
        nota_soma += nota    
    estudante["media"] = round(nota_soma/  len(estudante["notas"]), 2)
    return estudante
        

def estudantes_aprovados(estudantes: list):
    aprovados = filter(filtrar_aprovados, estudantes)
    aprovados = map(add_media, aprovados)
    return 

    
    

estudantes_aprovados(estudantes)

print(estudantes_aprovados)