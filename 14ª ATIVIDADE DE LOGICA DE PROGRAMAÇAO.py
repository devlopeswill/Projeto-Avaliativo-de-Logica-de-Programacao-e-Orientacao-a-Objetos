import pandas as pd

df = pd.read_csv("notas_alunos.csv")

media = (df["nota_1"] + df["nota_2"]) / 2

df.loc[((df["média das notas"] >=7) and (df["faltas"] <= 5)), "situação"] = "APROVADO"
df.loc[((df["média das notas"] <7) or (df["faltas"] > 5)), "situação"] = "REPROVADO"


maior_faltas = df["faltas"].max()
media_turma = df["média das notas"].median()
maior_media = df["média das notas"].max()

df.writer("notas_alunos.csv")

print("Maior número de faltas: " , maior_faltas)
print("Média da turma: " , media_turma)
print("Maior média de aluno: " , maior_media)
