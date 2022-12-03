import os

def listaArquivos():
    pasta = 'C:/Users/Papai/Google Drive/5.Projetos/estudopy/estudopy/arquivos'
    #C:\Users\Papai\Google Drive\5.Projetos\estudopy\estudopy\arquivos
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            #print(os.path.join(diretorio, arquivo))
            print(os.path.join(arquivo))
            return arquivo