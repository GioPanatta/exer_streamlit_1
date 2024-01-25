#Importando as bibliotecas
#Obs: Para imagens (histograma) utilizaremos apenas o Numpy
import streamlit as st
import pandas as pd
import numpy as np

# 1 ALterando o nome e imagem do app 
st.set_page_config(
   page_title="Exercício 1 Streamlit",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)

# 2 Introdução
st.title("Olá!") 
st.title("Este é o exercício 1 de Streamlit!")
st.header("Neste exercício iremos apenas copiar e colar alguns códigos da própria documentação do Streamlit.")
st.write("Ao clicar em [Streamlit](https://docs.streamlit.io/) você pode verificar a fonte dos nossos códigos.")

"""
## Our first app
## Here's our first attempt at using data to create a table:
"""

# 3 Criando um DF 
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

"""
## Creating a DataFrame with the numpy random function
"""
# 4 Criando um DF com a função random do Numpy
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)


st.write(" ## Let's expand on the first example using the Pandas Styler object to highlight some elements in the interactive table.")

# 5 Utilizando marcadores no DF
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

st.write("## Plot a map: With st.map you can display data points on a map. Let's use Numpy to generate some sample data and plot it on a map of San Francisco.")

# 6 Criando um mapa
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

st.write("## When you've got the data or model into the state that you want to explore, you can add in widgets like st.slider(), st.button() or st.selectbox(). It's really straightforward — treat widgets as variables:")

# 7 Criando um slider
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# 8 Criando um widget 
st.write("## Widgets can also be accessed by key, if you choose to specify a string to use as the unique key for the widget:")

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

# 9 Criando um checkbox
st.write("# Use checkboxes to show/hide data")
st.write("## One use case for checkboxes is to hide or show a specific chart or section in an app. st.checkbox() takes a single argument, which is the widget label. In this sample, the checkbox is used to toggle a conditional statement.")

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

st.write("# Use a selectbox for options")
st.write("## Use st.selectbox to choose from a series. You can write in the options you want, or pass through an array or data frame column.")
st.write("## Let's use the df data frame we created earlier.")


# 10 Criando um DF com a opção de seleção
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

st.write("# Layout")
st.write("## Streamlit makes it easy to organize your widgets in a left panel sidebar with st.sidebar. Each element that's passed to st.sidebar is pinned to the left, allowing users to focus on the content in your app while still having access to UI controls.")

st.write("### For example, if you want to add a selectbox and a slider to a sidebar, use st.sidebar.slider and st.sidebar.selectbox instead of st.slider and st.selectbox:")

# 11 criando um sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# 12 Adicionando slider ao sidebar
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.write("### Beyond the sidebar, Streamlit offers several other ways to control the layout of your app. st.columns lets you place widgets side-by-side, and st.expander lets you conserve space by hiding away large content.")

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# 13 widget de seleção com bloco (block)
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

#Titulo para dados Uber

st.header("Agora usaremos os principais recursos do Streamlit para criar um aplicativo interativo; explorando um conjunto de dados público do Uber para embarques e desembarques na cidade de Nova York. Quando terminarmos, saberemos como buscar e armazenar dados em cache, desenhar gráficos, plotar informações em um mapa e usar widgets interativos, como um controle deslizante, para filtrar resultados.")

st.title('Uber pickups in NYC')

st.write("## Let's start by writing a function to load the data:")

# 14 Selecionando os dados através do URL
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# 15 Função com @st.cache 
@st.cache_data #Essa função permite salvar os dados carregados em cache, evitando assim que sejam carregados novamente
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# 16 Elemento de texto para informar ao usuário sobre o início e fim da leitura dos dados
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

st.write("## It's always a good idea to take a look at the raw data you're working with before you start working with it. Let's add a subheader and a printout of the raw data to the app:")

# 17 verificação dos dados brutos
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')

# 18 histograma de 24 horas de embarques dataset Uber
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

st.write("## Using a histogram with Uber's dataset helped us determine what the busiest times are for pickups, but what if we wanted to figure out where pickups were concentrated throughout the city. While you could use a bar chart to show this data, it wouldn't be easy to interpret unless you were intimately familiar with latitudinal and longitudinal coordinates in the city. To show pickup concentration, let's use Streamlit st.map() function to overlay the data on a map of New York City.")


# 19 Mapa com todos os embarques
st.subheader('Map of all pickups')

st.map(data)

# 20 Filtro com apenas o horário de mario pico de embarques (17:00 rs)
hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
