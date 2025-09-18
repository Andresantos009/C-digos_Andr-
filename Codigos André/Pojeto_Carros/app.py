import streamlit as st
### COLOCA UM TITULO
st.title("VELOZ LOCADORA")
st.sidebar.title("VELOZ LOCADORA")
st.sidebar.image("logo.png")
### ESCREVE
st.sidebar.write("Boa Tarde. Escolha o seu carro para alugar com a melhor empresa do país")
### CRIA UMA BARRA LATERAL
st.sidebar.title("Carros Disponivel Para ALugar")
### CRIANDO UMA LISTA
nomes = ["Civic", "BMW", "Ford Focus", "Audi A8", "Volkswagen", "Ford Fiesta 2012" ]
## CRIA A CAIXINHA NA BARRA LATERAL
carro_escolhido = st.sidebar.selectbox("Escolha um Carro para alugar :" , nomes)
### Selecionar a imagem de acordo com o carro
st.markdown('---')


carros = ["Civic", "BMW", "Ford Focus", "Audi A8", "Volkswagen", "Ford Fiesta 2012"]


precos = {
    "Civic": 245,
    "BMW": 670,
    "Ford Focus": 220,
    "Audi A8": 1420,
    "Volkswagen": 180,
    "Ford Fiesta 2012": 120
}

if "indice_carro" not in st.session_state:
    st.session_state.indice_carro = 0

# Layout com setas
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⬅️"):
        st.session_state.indice_carro = (st.session_state.indice_carro - 1) % len(carros)
with col3:
    if st.button("➡️"):
        st.session_state.indice_carro = (st.session_state.indice_carro + 1) % len(carros)
carro_escolhido = carros[st.session_state.indice_carro]
diaria = precos[carro_escolhido]


st.image(f"{carro_escolhido}.png", caption=carro_escolhido)
st.markdown(f"## Você escolheu alugar: {carro_escolhido}")

gps = st.checkbox("Adicionar GPS (R$ 15 por dia)")
preco_gps = 15

if carro_escolhido == "Civic":
    diaria = 245

elif carro_escolhido == "BMW":
    diaria = 670

elif carro_escolhido == "Ford Focus":
    diaria = 220

elif carro_escolhido == "Audi A8":
    diaria = 1420

elif carro_escolhido == "Volkswagen":
    diaria = 180

elif carro_escolhido == "Ford Fiesta 2012":
    diaria = 120


dias = st.text_input(F"Por quantos dias você alugou o {carro_escolhido} ?")
km = st.number_input(f"Quantos km você rodou?")


if st.button("Calcular"):
    dias = int(dias)
    km = float(km)
    
    custo_gps = preco_gps * dias if gps else 0 

    total_dias = dias * diaria
    tolal_km = km * 0.15
    aluguel = total_dias + tolal_km + custo_gps 

    msg_gps = f" incluindo GPS por {dias} dias" if gps else "" 
    
    st.warning(f"Você alugou o {carro_escolhido} por {dias} dias{msg_gps}, rodou {km} km. O valor total do aluguel foi de R$ {aluguel:.2f}") 




