import streamlit as st 
from api_utils import cadastra_jogo
import os


def save_uploaded_file(uploadedfile):
  with open(os.path.join("./photos",uploadedfile.name),"wb") as f:
     f.write(uploadedfile.getbuffer())
  return True

st.title('Carregue Novos jogos para o sistema aqui')
st.subheader('Leia as instruções antes de preencher o formulário')

with st.expander('Instruções para o correto preenchimento do formulário'):
    st.divider()
    instructions='''
    <style>
    [data-testid="stAppViewContainer"]{
        background-image: linear-gradient(145deg, #FCEA10, #E6007E, #009FE3);
    }

    [data-testid="stExpander"]{
        color: white
    }
    .titulo{
    font-size:16px;
    text-align:center;
    color:white
    }

    .subtitulo{
    font-size:14px;
    color:white
    }

    .texto{
    font-size:12px;
    color:white
    }
    </style>

    <h1 class='titulo'> Instruções para o link do vídeo </h1>
    <h3 class='texto'> Para que possamos processar o vídeo, é preciso que seja enviado o link do video do youtube</h3>
    <h2 class='subtitulo'> Como posso colocar meu video no youtube? </h2>
    <p>
    <li> Faça uma conta no youtube e um canal </li>
    <li> Poste o seu vídeo como não listado no seu canal mas ainda PÚBLICO. Esse processo pode demorar alguns minutos</li>
    </p>
    <h3 class='texto'> depois de seguir esses passos, basta colocar o link do video no formulário </h3>
    <h1 class='titulo' > Instruções para o link do arquivo csv </h1>
    <h3 class='texto'> Para que possamos processar o arquivo com os dados brutos, é preciso que seja enviado o link do arquivo do google drive</h3>
    <h2 class='subtitulo'>Como posso colocar meu arquivo no google drive? </h2>
    <p>
    <li> Faça uma conta no gmail e abra o drive</li>
    <li> coloque seu vídeo no seu drive e deixe esse vídeo PÚBLICO. Esse processo pode demorar alguns minutos</li>
    </p>
    <h3 class='texto'> depois de seguir esses passos, basta colocar o link para o arquivo csv no formulário </h3>
    
    '''
    
    st.markdown(instructions,unsafe_allow_html=True)


with st.container():
    with st.form(key='form_jogo',clear_on_submit=True):
        time1 = st.text_input('Digite o nome do primeiro time')
        logo1 = st.file_uploader('Coloque aqui a logo do time acima em formato PNG',key='time1')
        time2 = st.text_input('Digite o nome do segundo time')
        logo2 = st.file_uploader('Coloque aqui a logo do time acima em formato PNG',key='time2')
        link_video = st.text_input("insira o link para o video do jogo")
        link_csv = st.text_input("insira o link para arquivo csv dos dados bruto")
        lista_dados = [time1,logo1,logo2,time2,link_video,link_csv]


        if st.form_submit_button():
            if (not(None in lista_dados)):
                save_uploaded_file(logo1)
                save_uploaded_file(logo2)
                data = {'link_video': link_video ,'link_csv': link_csv, 'time1':time1, 'time2': time2}
                files= {'logo1':open(f'./photos/{logo1.name}','rb'),
                        'logo2':open(f'./photos/{logo2.name}','rb')}
                salvou, mensagem = cadastra_jogo(data,files)
                st.write('Seus dados foram enviados com sucesso e estão sendo processados. Esse processo pode demorar alguns horas')
            else: 
                st.error('todos os dados devem ser preenchidos')