import os
import shutil

#CONFIGURAÇÕES DAS PASTAS
#caminho da pasta principal onde estão as pastas das imagens
origem = r'CAMINHO_DA_SUA_PASTA_STEAM_AQUI'
#exemplo de pasta Steam: r'C:\Program Files (x86)\Steam\userdata\SEU_ID_AQUI\760\remote'

#caminho onde as imagens serão copiadas
destino = r'CAMINHO_ONDE_DESEJA_SALVAR_AQUI'
#exemplo de destino: r'C:\Users\USUARIO\Pictures\Screenshots'

#cria a pasta de destino se não existir
os.makedirs(destino, exist_ok=True)

#percorre cada pasta dos jogos
for pasta_jogo in os.listdir(origem):
    caminho_jogo = os.path.join(origem, pasta_jogo)
    
    if os.path.isdir(caminho_jogo):
        caminho_screenshots = os.path.join(caminho_jogo, "screenshots")
        
        if os.path.isdir(caminho_screenshots):
            for arquivo in os.listdir(caminho_screenshots):
                caminho_arquivo = os.path.join(caminho_screenshots, arquivo)

                #aqui apenas pega arquivos de imagens, e não a pasta "thumbnails"
                if os.path.isfile(caminho_arquivo) and arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                    caminho_destino = os.path.join(destino, arquivo)

                    #verifica se a imagem já existe na pasta de destino; se sim, pula
                    if os.path.exists(caminho_destino):
                        print(f"Arquivo já existe, pulando: {arquivo}")
                        continue
                    
                    shutil.copy2(caminho_arquivo, caminho_destino)

print("Imagens copiadas!")
