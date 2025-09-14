import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("Análise de Visualizações por Tipo com Tendência")

# Carregar dados
df = pd.read_csv("netflix_tratado.csv")
df["Data"] = pd.to_datetime(df["Data"])
df["Mes"] = df["Data"].dt.to_period("M")

# Agrupar por mês e tipo
vis_por_mes_tipo = df.groupby(["Mes", "Tipo"]).size().unstack(fill_value=0)

# Transformar meses em números
meses_numericos = np.arange(len(vis_por_mes_tipo)).reshape(-1, 1)

# Plotar gráfico com regressão
fig, ax = plt.subplots(figsize=(12, 5))

for tipo, cor in zip(vis_por_mes_tipo.columns, ["blue", "green", "purple"]):
    y = vis_por_mes_tipo[tipo].values
    modelo = LinearRegression().fit(meses_numericos, y)
    tendencia = modelo.predict(meses_numericos)

    ax.plot(vis_por_mes_tipo.index.astype(str), y, marker='o', label=tipo, color=cor)
    ax.plot(vis_por_mes_tipo.index.astype(str), tendencia, linestyle='--', color=cor, alpha=0.5)

ax.set_title("Tendência de Visualizações por Tipo", fontsize=14)
ax.set_xlabel("Mês")
ax.set_ylabel("Visualizações")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)

st.pyplot(fig)

