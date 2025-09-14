
# 📌 Análise de Comportamento de Visualização na Netflix

## 🧠 Resumo
****Este projeto tem como objetivo analisar padrões de consumo de conteúdo na Netflix com base em uma base de dados pessoal de visualizações. Foram realizadas etapas de tratamento, análise exploratória e geração de insights sobre tipos de conteúdo, dias da semana mais assistidos, gêneros preferidos, séries mais vistas por mês, entre outros. A análise foi feita utilizando Python e bibliotecas como Pandas e Matplotlib.****


## 🎯 Objetivo
Investigar os hábitos de consumo de conteúdo na Netflix, identificando:
- Preferência entre filmes e séries.
- Dias da semana com maior e menor atividade.
- Gêneros mais assistidos.
- Séries mais populares por mês.
- Média de títulos assistidos por mês.
- Padrões temporais de visualização.
---
## 🧹 Tratamento de Dados
- Leitura e inspeção inicial dos dados.
- Verificação de tipos de dados e conversão quando necessário.
- Identificação e tratamento de valores nulos.
- Remoção de duplicatas.
- Padronização de formatos de texto (ex.: nomes de séries e gêneros).
- Período coberto: 05/12/2020 a 23/08/2022 (datas de visualização).
- Conversão de datas para formato datetime .
- Agrupamentos por série, gênero, tipo e data.
- Integração com dados externos de clima e feriados.
- Normalização de nomes de séries e gêneros.
- Análise de outliers e tratamento de dados extremos.
- Geração de estatísticas descritivas.
- Visualizações iniciais para entender distribuições e tendências.
- Documentação do processo de tratamento e análise.
---
## 📂 Fonte e Descrição dos Dados
- **Fonte:** Base pessoal exportada da Netflix.
- **Formato:** CSV
- **Colunas principais:**
  - `Date`: Data da visualização
  - `Serie`, `Temporada`, `Episodio`, `Titulo`: Informações do conteúdo
  - `Tipo`: Filme ou Série
  - `Ano`: Ano da visualização
  - `Dia Semana`: Dia da semana
  - `Genero`: Gênero do conteúdo
  - `Cidade`: Cidade de visualização
  - `Feriado`: Quantidade de feriados no mês

---
## 🔍 Metodologia

- **Linguagem**: Python
- **Bibliotecas principais**: `pandas`, `matplotlib`, `scikit-learn`, `holidays`, `meteostat`
- **Análise Exploratória**: Estatísticas descritivas, visualizações gráficas (barras, linhas).
- **Agrupamentos**: Por série, gênero, tipo, data.
- **Integração de dados externos**: Clima e feriados.
- **Integrações externas**:
 
  - API de geocodificação via [Open-Meteo](https://open-meteo.com)
  - Feriados nacionais e estaduais via `holidays`

---
## 🧠 Insights Estratégicos
- Investir em **séries** pode exigir reposicionamento ou curadoria mais atrativa.
- **Filmes** mantêm estabilidade e podem ser reforçados em campanhas sazonais.
- **Gêneros populares**: Drama e Documentários são os mais assistidos.
- **Séries de sucesso**: "Stranger Things", "La Casa de Papel", "The Witcher" e "Bridgerton".
- **Dias de maior consumo**: Sábado e Domingo.
- **Dias de menor consumo**: Segunda-feira e Terça-feira.
- **Picos de visualização** ocorrem em meses específicos.
- **Tendência de queda**: Diminuição gradual no número de visualizações ao longo do tempo.
- **Impacto do clima**: Dias chuvosos tendem a aumentar o consumo de conteúdo.
- **O clima e feriados** são variáveis relevantes para prever comportamento de consumo.

---
## 🚀 Próximos Passos
- Aplicar modelos preditivos para estimar visualizações futuras.
- Explorar regressão múltipla com variáveis combinadas (clima + feriado + tipo).
- Testar modelos de séries temporais (ARIMA, Prophet).
- Analisar impacto de lançamentos e campanhas de marketing.
- Realizar segmentação de usuários para personalização de recomendações.
- Criar dashboards interativos com `Plotly` ou `Streamlit`.
- Expandir a base com novos dados, dispositivo e horário de visualização.
---
## 📬 Contato

- **Autor**: Marco
- **Local**: Florianópolis–SC  
- **Data do projeto**: Setembro de 2025

---
## 🛠️ Como Executar o Projeto
- **Execução:** Basta abrir o notebook e executar as células sequencialmente.
