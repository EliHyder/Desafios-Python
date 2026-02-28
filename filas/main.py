import os
import pandas as pd

filas_csv =  [f for f in os.listdir("dados_filiais") if f.endswith(".csv")]

df_filiais = [pd.read_csv(f"dados_filiais/{f}") for f in filas_csv]
for df in df_filiais:
    df.rename(columns=lambda x: "valor" if df[x].dtype == 'int64' else "produto", inplace=True)
    df["valor"] = df["valor"].fillna(0)  # Substituindo valores nulos por 0

df_concatenado = pd.concat(df_filiais, ignore_index=True)
print(df_concatenado)

relatorio = df_concatenado.groupby("produto")["valor"].sum().reset_index()
print(relatorio)
relatorio.to_csv("relatorio_final.csv", index=False)
