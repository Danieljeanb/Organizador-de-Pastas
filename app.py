import os
import shutil

# Define a pasta que está bagunçada
PASTA_ALVO = "C:/Users/Seu_Usuario/Downloads"

# Define as pastas de destino para cada tipo de arquivo
REGRAS = {
    "Documentos": [".pdf", ".docx", ".txt"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Vídeos": [".mp4", ".avi", ".mkv"],
    "Músicas": [".mp3", ".wav"],
    "Arquivos Compactados": [".zip", ".rar"],
}

for arquivo in os.listdir(PASTA_ALVO):
    nome, extensao = os.parth.splitext(arquivo)


    # Proximo passo: mover se encaixar na regra!

for pasta, extensoes in REGRAS.items():
    if extensao.lower() in extensoes:
        destino = os.path.join(PASTA_ALVO, pasta)
        os.makedirs(destino, exist_ok=True)

        shutil.move(os.path.join(PASTA_ALVO, arquivo), destino)

print("Organização concluída!")
   