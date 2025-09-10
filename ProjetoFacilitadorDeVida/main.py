# @SavioCartaxo - GitHub

import cv2 as cv
import os
import pandas as pd

#Lendo o arquivo
planilha_df = pd.read_csv("/home/saviocartaxo/Documents/repositorios/GT_RECEITA(Sheet1).csv", sep=';', encoding='utf-8') ##### caminho para o csv
lista_das_imagens = planilha_df['NOME_IMAGEM']

# Isso serve para que, no final, vc saiba quais os arquivos nao lidos pelo programa
lista_de_imagens_nao_encontradas = []

# aqui coloca o caminho da pasta que esta o arquivo
pasta = "/home/saviocartaxo/Downloads/pasta_5/IMGS" ##### AQUI COLOCA O CAMINHO PARA A PASTA DE IMAGENS
arquivo_acessado_atualmente = int(input("Numero do primeiro arquivo que vc ira trabalhar: "))
arquivo_acessado_atualmente -= 2 

while True:
    # Aqui selecionamos digitamos o nome do documento em si
    print(arquivo_acessado_atualmente + 2)
    nome_do_arquivo = lista_das_imagens[arquivo_acessado_atualmente]

    caminho_para_o_arquivo = os.path.join(pasta, nome_do_arquivo)
    
    imagem = cv.imread(caminho_para_o_arquivo)
    
    if imagem is None:
        lista_de_imagens_nao_encontradas.append(nome_do_arquivo)
        continue

    while (True):

        # Trabalhando com a janela
        cv.namedWindow(nome_do_arquivo, cv.WINDOW_NORMAL)
        cv.resizeWindow(nome_do_arquivo,800, 1200)
        cv.moveWindow("Imagem Esquerda", 0, 0)

        cv.imshow(nome_do_arquivo, imagem)
        tecla = cv.waitKey(0) & 0xFF
        
        # tecla espaço ou enter fecha a imagem # 13
        if tecla == 13 or tecla == 120:
            break

        # tecla direita >> rotaciona a imagem 90° #83
        if tecla == 83:
            imagem = cv.rotate(imagem, cv.ROTATE_90_CLOCKWISE)

        # tecla esquerda >> rotaciona a imagem 270° #81
        if tecla == 81:
            imagem = cv.rotate(imagem, cv.ROTATE_90_COUNTERCLOCKWISE)

        # tecla para cima ou para baixo >> rotaciona 180° #82 # 84
        if tecla == 82 or tecla == 84:
            imagem = cv.rotate(imagem, cv.ROTATE_180)
        
        if tecla == 8:
            arquivo_acessado_atualmente -= 2
            break

        cv.imwrite(caminho_para_o_arquivo, imagem)
    
    if (tecla == 120) : break
    cv.destroyAllWindows()
    arquivo_acessado_atualmente += 1

# Printa o nome dos arquivos nao encontrados
for nome_do_arquivo in lista_de_imagens_nao_encontradas:
    print(nome_do_arquivo)