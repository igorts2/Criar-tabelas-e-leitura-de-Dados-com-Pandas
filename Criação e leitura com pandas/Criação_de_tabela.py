import pandas as pd

#criar uma tabela exel atravez das informações
clientes = [
    {"Data": "2025-05-24", "ID": "CL001", "País": "Argentina", "Cidade": "La Plata", "Nome": "Rafael", "Sobrenome": "Ramírez"},
    {"Data": "2025-05-30", "ID": "CL002", "País": "Colômbia", "Cidade": "Barranquilla", "Nome": "Valentina", "Sobrenome": "Almeida"},
    {"Data": "2025-05-26", "ID": "CL003", "País": "Brasil", "Cidade": "Curitiba", "Nome": "Mariana", "Sobrenome": "Vargas"},
    {"Data": "2025-05-30", "ID": "CL004", "País": "Argentina", "Cidade": "Mendoza", "Nome": "Agustina", "Sobrenome": "Castillo"},
    {"Data": "2025-05-23", "ID": "CL005", "País": "Brasil", "Cidade": "Curitiba", "Nome": "Lucas", "Sobrenome": "Torres"},
    {"Data": "2025-05-30", "ID": "CL006", "País": "Brasil", "Cidade": "Salvador", "Nome": "Camila", "Sobrenome": "Correa"},
    {"Data": "2025-05-29", "ID": "CL007", "País": "Argentina", "Cidade": "Rosário", "Nome": "Bruno", "Sobrenome": "Lima"},
    {"Data": "2025-05-26", "ID": "CL008", "País": "Brasil", "Cidade": "Curitiba", "Nome": "Agustina", "Sobrenome": "Correa"},
    {"Data": "2025-05-20", "ID": "CL009", "País": "Chile", "Cidade": "Iquique", "Nome": "Andrés", "Sobrenome": "Herrera"},
    {"Data": "2025-05-25", "ID": "CL010", "País": "Colômbia", "Cidade": "Cali", "Nome": "Sofía", "Sobrenome": "López"},
    {"Data": "2025-05-21", "ID": "CL011", "País": "Brasil", "Cidade": "Recife", "Nome": "Rafael", "Sobrenome": "Vargas"},
    {"Data": "2025-05-21", "ID": "CL012", "País": "Brasil", "Cidade": "Porto Alegre", "Nome": "Valentina", "Sobrenome": "Castillo"},
    {"Data": "2025-05-24", "ID": "CL013", "País": "Argentina", "Cidade": "Mendoza", "Nome": "Pedro", "Sobrenome": "Vargas"},
    {"Data": "2025-05-24", "ID": "CL014", "País": "Brasil", "Cidade": "Porto Alegre", "Nome": "Martín", "Sobrenome": "González"},
    {"Data": "2025-05-21", "ID": "CL015", "País": "Colômbia", "Cidade": "Cali", "Nome": "Diego", "Sobrenome": "Fernández"},
    {"Data": "2025-05-27", "ID": "CL016", "País": "Argentina", "Cidade": "Córdoba", "Nome": "Mariana", "Sobrenome": "Ríos"},
    {"Data": "2025-05-27", "ID": "CL017", "País": "Argentina", "Cidade": "La Plata", "Nome": "Camila", "Sobrenome": "Ramírez"},
    {"Data": "2025-05-29", "ID": "CL018", "País": "Argentina", "Cidade": "Rosário", "Nome": "Diego", "Sobrenome": "Pérez"},
    {"Data": "2025-05-26", "ID": "CL019", "País": "Chile", "Cidade": "Antofagasta", "Nome": "Lucas", "Sobrenome": "Martínez"},
    {"Data": "2025-05-20", "ID": "CL020", "País": "Brasil", "Cidade": "Curitiba", "Nome": "Lucas", "Sobrenome": "Palacios"},
    {"Data": "2025-05-24", "ID": "CL021", "País": "Argentina", "Cidade": "La Plata", "Nome": "Andrés", "Sobrenome": "Castillo"},
    {"Data": "2025-05-28", "ID": "CL022", "País": "Brasil", "Cidade": "Manaus", "Nome": "Diego", "Sobrenome": "Navarro"},
    {"Data": "2025-05-20", "ID": "CL023", "País": "Chile", "Cidade": "Concepción", "Nome": "Lorena", "Sobrenome": "Pérez"},
    {"Data": "2025-05-22", "ID": "CL024", "País": "Colômbia", "Cidade": "Cali", "Nome": "Juliana", "Sobrenome": "Palacios"},
    {"Data": "2025-05-24", "ID": "CL025", "País": "Brasil", "Cidade": "Salvador", "Nome": "Joaquín", "Sobrenome": "Herrera"},
    {"Data": "2025-05-27", "ID": "CL026", "País": "Colômbia", "Cidade": "Cali", "Nome": "Paula", "Sobrenome": "Fernández"},
    {"Data": "2025-05-25", "ID": "CL027", "País": "Argentina", "Cidade": "La Plata", "Nome": "Camila", "Sobrenome": "Pérez"},
    {"Data": "2025-05-24", "ID": "CL028", "País": "Colômbia", "Cidade": "Cartagena", "Nome": "Paula", "Sobrenome": "Pérez"},
    {"Data": "2025-05-30", "ID": "CL029", "País": "Brasil", "Cidade": "Manaus", "Nome": "Diego", "Sobrenome": "González"},
    {"Data": "2025-05-30", "ID": "CL030", "País": "Colômbia", "Cidade": "Cali", "Nome": "Rafael", "Sobrenome": "Morales"},
    {"Data": "2025-05-29", "ID": "CL031", "País": "Chile", "Cidade": "Iquique", "Nome": "Bruno", "Sobrenome": "López"},
    {"Data": "2025-05-27", "ID": "CL032", "País": "Colômbia", "Cidade": "Cartagena", "Nome": "Isabela", "Sobrenome": "Navarro"},
    {"Data": "2025-05-21", "ID": "CL033", "País": "Argentina", "Cidade": "La Plata", "Nome": "Rafael", "Sobrenome": "Castillo"},
    {"Data": "2025-05-24", "ID": "CL034", "País": "Colômbia", "Cidade": "Cartagena", "Nome": "Agustina", "Sobrenome": "Ríos"},
    {"Data": "2025-05-25", "ID": "CL035", "País": "Brasil", "Cidade": "Manaus", "Nome": "Andrés", "Sobrenome": "Almeida"},
    {"Data": "2025-05-26", "ID": "CL036", "País": "Brasil", "Cidade": "Manaus", "Nome": "Mateo", "Sobrenome": "Ríos"},
    {"Data": "2025-05-26", "ID": "CL037", "País": "Colômbia", "Cidade": "Cali", "Nome": "Lucas", "Sobrenome": "Navarro"},
    {"Data": "2025-05-20", "ID": "CL038", "País": "Chile", "Cidade": "Temuco", "Nome": "Carlos", "Sobrenome": "Acuña"},
    {"Data": "2025-05-24", "ID": "CL039", "País": "Argentina", "Cidade": "Rosário", "Nome": "Rafael", "Sobrenome": "Vargas"},
    {"Data": "2025-05-22", "ID": "CL040", "País": "Chile", "Cidade": "Iquique", "Nome": "Sofía", "Sobrenome": "González"},
    {"Data": "2025-05-21", "ID": "CL041", "País": "Chile", "Cidade": "Temuco", "Nome": "Lucas", "Sobrenome": "Torres"},
    {"Data": "2025-05-24", "ID": "CL042", "País": "Colômbia", "Cidade": "Barranquilla", "Nome": "Isabela", "Sobrenome": "González"},
    {"Data": "2025-05-23", "ID": "CL043", "País": "Argentina", "Cidade": "Rosário", "Nome": "Camila", "Sobrenome": "Ramírez"},
    {"Data": "2025-05-23", "ID": "CL044", "País": "Argentina", "Cidade": "La Plata", "Nome": "Juliana", "Sobrenome": "Martínez"},
    {"Data": "2025-05-24", "ID": "CL045", "País": "Brasil", "Cidade": "Curitiba", "Nome": "Andrés", "Sobrenome": "López"},
    {"Data": "2025-05-26", "ID": "CL046", "País": "Argentina", "Cidade": "La Plata", "Nome": "Diego", "Sobrenome": "Acuña"},
    {"Data": "2025-05-25", "ID": "CL047", "País": "Colômbia", "Cidade": "Medellín", "Nome": "Andrés", "Sobrenome": "González"},
    {"Data": "2025-05-20", "ID": "CL048", "País": "Chile", "Cidade": "Concepción", "Nome": "Andrés", "Sobrenome": "Almeida"},
    {"Data": "2025-05-30", "ID": "CL049", "País": "Brasil", "Cidade": "Recife", "Nome": "Fernanda", "Sobrenome": "Mendoza"},
    {"Data": "2025-05-28", "ID": "CL050", "País": "Chile", "Cidade": "Iquique", "Nome": "Agustina", "Sobrenome": "Lima"},
    {"Data": "2025-05-29", "ID": "CL051", "País": "Chile", "Cidade": "Valparaíso", "Nome": "Isabela", "Sobrenome": "Correa"},
    {"Data": "2025-05-26", "ID": "CL052", "País": "Brasil", "Cidade": "Porto Alegre", "Nome": "Pedro", "Sobrenome": "Vargas"},
    {"Data": "2025-05-27", "ID": "CL053", "País": "Chile", "Cidade": "Temuco", "Nome": "Lucas", "Sobrenome": "Mendoza"},
    {"Data": "2025-05-26", "ID": "CL054", "País": "Chile", "Cidade": "Iquique", "Nome": "Martín", "Sobrenome": "Morales"},
    {"Data": "2025-05-23", "ID": "CL055", "País": "Colômbia", "Cidade": "Medellín", "Nome": "Lucas", "Sobrenome": "Castillo"},
    {"Data": "2025-05-27", "ID": "CL056", "País": "Argentina", "Cidade": "Córdoba", "Nome": "Pedro", "Sobrenome": "Correa"},
    {"Data": "2025-05-27", "ID": "CL057", "País": "Brasil", "Cidade": "Porto Alegre", "Nome": "Lucas", "Sobrenome": "Castillo"},
    {"Data": "2025-05-25", "ID": "CL058", "País": "Argentina", "Cidade": "La Plata", "Nome": "Lorena", "Sobrenome": "Morales"},
    {"Data": "2025-05-23", "ID": "CL059", "País": "Argentina", "Cidade": "La Plata", "Nome": "Joaquín", "Sobrenome": "Torres"},
    {"Data": "2025-05-25", "ID": "CL060", "País": "Colômbia", "Cidade": "Cali", "Nome": "Sofía", "Sobrenome": "Martínez"},
    {"Data": "2025-05-21", "ID": "CL061", "País": "Brasil", "Cidade": "Manaus", "Nome": "Bruno", "Sobrenome": "Mendoza"},
    {"Data": "2025-05-30", "ID": "CL062", "País": "Chile", "Cidade": "Iquique", "Nome": "Pedro", "Sobrenome": "Herrera"},
    {"Data": "2025-05-21", "ID": "CL063", "País": "Colômbia", "Cidade": "Pereira", "Nome": "Fernanda", "Sobrenome": "Lima"},
    {"Data": "2025-05-28", "ID": "CL064", "País": "Brasil", "Cidade": "Manaus", "Nome": "Agustina", "Sobrenome": "Mendoza"},
    {"Data": "2025-05-29", "ID": "CL065", "País": "Brasil", "Cidade": "Recife", "Nome": "Lorena", "Sobrenome": "Fernández"},
    {"Data": "2025-05-21", "ID": "CL066", "País": "Argentina", "Cidade": "San Juan", "Nome": "Martín", "Sobrenome": "Correa"},
    {"Data": "2025-05-22", "ID": "CL067", "País": "Brasil", "Cidade": "Recife", "Nome": "Mateo", "Sobrenome": "Castillo"},
    {"Data": "2025-05-25", "ID": "CL068", "País": "Chile", "Cidade": "Valparaíso", "Nome": "Rafael", "Sobrenome": "Acuña"},
    {"Data": "2025-05-21", "ID": "CL069", "País": "Colômbia", "Cidade": "Cartagena", "Nome": "Joaquín", "Sobrenome": "Morales"},
    {"Data": "2025-05-22", "ID": "CL070", "País": "Brasil", "Cidade": "Salvador", "Nome": "Diego", "Sobrenome": "Martínez"},
    {"Data": "2025-05-21", "ID": "CL071", "País": "Colômbia", "Cidade": "Barranquilla", "Nome": "Lorena", "Sobrenome": "López"},
    {"Data": "2025-05-21", "ID": "CL072", "País": "Colômbia", "Cidade": "Pereira", "Nome": "Mateo", "Sobrenome": "Martínez"},
    {"Data": "2025-05-22", "ID": "CL073", "País": "Argentina", "Cidade": "Rosário", "Nome": "Bruno", "Sobrenome": "López"},
    {"Data": "2025-05-21", "ID": "CL074", "País": "Brasil", "Cidade": "Manaus", "Nome": "Bruno", "Sobrenome": "Vargas"},
    {"Data": "2025-05-23", "ID": "CL075", "País": "Colômbia", "Cidade": "Barranquilla", "Nome": "Mateo", "Sobrenome": "Mendoza"},
    {"Data": "2025-05-23", "ID": "CL076", "País": "Colômbia", "Cidade": "Pereira", "Nome": "Diego", "Sobrenome": "Navarro"},
    {"Data": "2025-05-22", "ID": "CL077", "País": "Colômbia", "Cidade": "Cartagena", "Nome": "Lucas", "Sobrenome": "Correa"},
    {"Data": "2025-05-27", "ID": "CL078", "País": "Colômbia", "Cidade": "Pereira", "Nome": "Fernanda", "Sobrenome": "Herrera"},
    {"Data": "2025-05-23", "ID": "CL079", "País": "Colômbia", "Cidade": "Pereira", "Nome": "Carlos", "Sobrenome": "Acuña"},
    {"Data": "2025-05-30", "ID": "CL080", "País": "Chile", "Cidade": "Antofagasta", "Nome": "Camila", "Sobrenome": "Almeida"},
    {"Data": "2025-05-28", "ID": "CL081", "País": "Argentina", "Cidade": "La Plata", "Nome": "Carlos", "Sobrenome": "Vargas"},
    {"Data": "2025-05-27", "ID": "CL082", "País": "Chile", "Cidade": "Concepción", "Nome": "Pedro", "Sobrenome": "Morales"},
    {"Data": "2025-05-24", "ID": "CL083", "País": "Colômbia", "Cidade": "Pereira", "Nome": "Paula", "Sobrenome": "Fernández"},
    {"Data": "2025-05-29", "ID": "CL084", "País": "Argentina", "Cidade": "Rosário", "Nome": "Valentina", "Sobrenome": "Lima"},
    {"Data": "2025-05-27", "ID": "CL085", "País": "Argentina", "Cidade": "Rosário", "Nome": "Andrés", "Sobrenome": "Ramírez"},
    {"Data": "2025-05-20", "ID": "CL086", "País": "Brasil", "Cidade": "Salvador", "Nome": "Fernanda", "Sobrenome": "Almeida"},
    {"Data": "2025-05-26", "ID": "CL087", "País": "Brasil", "Cidade": "Porto Alegre", "Nome": "Lorena", "Sobrenome": "Mendoza"},
    {"Data": "2025-05-22", "ID": "CL088", "País": "Colômbia", "Cidade": "Medellín", "Nome": "Valentina", "Sobrenome": "Almeida"},
    {"Data": "2025-05-20", "ID": "CL089", "País": "Colômbia", "Cidade": "Pereira", "Nome": "Lucas", "Sobrenome": "López"},
    {"Data": "2025-05-22", "ID": "CL090", "País": "Chile", "Cidade": "Valparaíso", "Nome": "Fernanda", "Sobrenome": "Palacios"},
    {"Data": "2025-05-20", "ID": "CL091", "País": "Brasil", "Cidade": "Porto Alegre", "Nome": "Lorena", "Sobrenome": "Ríos"},
    {"Data": "2025-05-28", "ID": "CL092", "País": "Colômbia", "Cidade": "Cali", "Nome": "Paula", "Sobrenome": "Correa"},
    {"Data": "2025-05-20", "ID": "CL093", "País": "Brasil", "Cidade": "Porto Alegre", "Nome": "Sofía", "Sobrenome": "Correa"},
    {"Data": "2025-05-30", "ID": "CL094", "País": "Chile", "Cidade": "Valparaíso", "Nome": "Mateo", "Sobrenome": "Herrera"},
    {"Data": "2025-05-22", "ID": "CL095", "País": "Chile", "Cidade": "Antofagasta", "Nome": "Martín", "Sobrenome": "Acuña"},
    {"Data": "2025-05-28", "ID": "CL096", "País": "Argentina", "Cidade": "San Juan", "Nome": "Pedro", "Sobrenome": "Correa"},
    {"Data": "2025-05-26", "ID": "CL097", "País": "Argentina", "Cidade": "Mendoza", "Nome": "Mateo", "Sobrenome": "Herrera"},
    {"Data": "2025-05-21", "ID": "CL098", "País": "Argentina", "Cidade": "La Plata", "Nome": "Joaquín", "Sobrenome": "Correa"},
    {"Data": "2025-05-26", "ID": "CL099", "País": "Argentina", "Cidade": "Mendoza", "Nome": "Diego", "Sobrenome": "Fernández"},
    {"Data": "2025-05-22", "ID": "CL100", "País": "Colômbia", "Cidade": "Medellín", "Nome": "Diego", "Sobrenome": "Castillo"},
]

#criar dataframe
df = pd.DataFrame(clientes)

#salvar em exel
df.to_excel("clientes_novaconecta.xlsx", index=False)

arquivo = "clientes_novaconecta.xlsx"

df = pd.read_excel(arquivo)

pd.set_option('display.max_rows', None)

print(df.head(150))