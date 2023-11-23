import streamlit as st
import requests
import matplotlib.pyplot as plt



def exibir_grafico_desfechos_quebra_linha():
    url_desfechos_quebra_linha = 'http://127.0.0.1:5000/desfechos'

    response = requests.get(url_desfechos_quebra_linha)
    if response.status_code == 200:
        data = response.json()
    else:
        st.error("Erro ao obter informações. Verifique se o servidor Flask está em execução.")

    labels = data.keys()

    total = 0
    for valor in data.values():
        total += valor

    porcentagens = []
    for valor in data.values():
        porcentagem = valor / total
        porcentagens.append(porcentagem)

    sizes = porcentagens

    fig1, ax1 = plt.subplots()  
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax1.axis('equal')

    st.markdown('Geral:')
    st.pyplot(fig1)

def exibir_grafico_desfechos_quebra_linha_por_time():
    url_desfechos_quebra_linha_por_time = 'http://127.0.0.1:5000/desfechos_por_time'

    response = requests.get(url_desfechos_quebra_linha_por_time)
    if response.status_code == 200:
        data = response.json()
    else:
        st.error("Erro ao obter informações. Verifique se o servidor Flask está em execução.")
    
    for time in data.keys():
        
        labels = data[time].keys()

        total = 0
        for valor in data[time].values():
            total += valor

        porcentagens = []
        for valor in data[time].values():
            porcentagem = valor / total
            porcentagens.append(porcentagem)

        sizes = porcentagens

        fig1, ax1 = plt.subplots()  
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax1.axis('equal')

        st.markdown(f'{time}:')
        st.pyplot(fig1)