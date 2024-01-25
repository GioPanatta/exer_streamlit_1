# Exercício 1 de Streamlit

## Sobre o Projeto
Este projeto é um exercício prático que explora as funcionalidades do Streamlit, utilizando exemplos da documentação oficial. O script é escrito em Python e projetado para ser executado em um ambiente Streamlit.

O link do app pode ser acessado [aqui](https://giopanatta-exer-streamlit-1-streamlit-ex1-b7m0ok.streamlit.app/)

## Funcionalidades Implementadas

### Configuração Inicial
- Importação das bibliotecas `streamlit`, `pandas` e `numpy`.
- Configuração da página com `st.set_page_config`, incluindo título, ícone, layout e estado inicial da barra lateral.

### Apresentação e Visualização de Dados
- Exibição de texto e links usando `st.title`, `st.header`, e `st.write`.
- Criação e visualização de DataFrames simples e com dados aleatórios (`np.random`).

### Widgets Interativos e Layout
- Demonstração de vários widgets do Streamlit como sliders (`st.slider`), caixas de texto (`st.text_input`), e checkboxes (`st.checkbox`).
- Organização de widgets e conteúdo em colunas (`st.columns`) e na barra lateral (`st.sidebar`).
- Uso de blocos `with` para estruturar o layout de forma mais organizada.

### Análise de Dados do Uber
- Carregamento de dados do Uber usando uma função com `@st.cache` para melhorar a performance.
- Criação de um histograma de horários de embarques (`np.histogram`).
- Exibição de dados em um mapa (`st.map`) para visualizar geograficamente os embarques.

## Execução do Script
Para rodar este script:
1. Instale o Streamlit: `pip install streamlit`.
2. Execute o comando: `streamlit run seu_script.py`.

## Nota
Este projeto é apenas para fins educacionais, utilizando dados e exemplos da documentação do Streamlit.
