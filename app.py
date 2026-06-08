import os
import shutil


# Define a pasta que está bagunçada
PASTA_ALVO = "C:\\Users\\SEU_USUARIO\\Downloads"

# Define as pastas de destino para cada tipo de arquivo
REGRAS = {
    "Documentos": [".pdf", ".docx", ".txt" "excel", ".xlsx"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Vídeos": [".mp4", ".avi", ".mkv"],
    "Músicas": [".mp3", ".wav"],
    "Arquivos Compactados": [".zip", ".rar"],
}

for arquivo in os.listdir(PASTA_ALVO):
    nome, extensao = os.path.splitext(arquivo)


    # Proximo passo: mover se encaixar na regra!

for pasta, extensoes in REGRAS.items():
    if extensao.lower() in extensoes:
        destino = os.path.join(PASTA_ALVO, pasta)
        os.makedirs(destino, exist_ok=True)

        shutil.move(os.path.join(PASTA_ALVO, arquivo), destino)

def organizar_pastas():
    for arquivo in os.listdir(PASTA_ALVO):
        nome, extensao = os.path.splitext(arquivo)

        for pasta, extensoes in REGRAS.items():
            if extensao.lower() in extensoes:
                destino = os.path.join(PASTA_ALVO, pasta)
                os.makedirs(destino, exist_ok=True)

                shutil.move(os.path.join(PASTA_ALVO, arquivo), destino)

def mover_arquivo(arquivo, destino):
    shutil.move(os.path.join(PASTA_ALVO, arquivo), destino)
    pdf = "C:\\Users\\DNJJ\\Downloads\\documento.PDF"
    excel = "C:\\Users\\DNJJ\\Downloads\\documento.EXCEL"
    return pdf, excel

if __name__ == "__main__":
    organizar_pastas()
    print("Organização concluída!")
           