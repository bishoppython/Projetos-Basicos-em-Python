from pytube import YouTube

# URL do vídeo do YouTube
url = input("Insira a URL do vídeo do YouTube: ")

# Criar um objeto YouTube
yt = YouTube(url)

# Obter o primeiro stream de vídeo disponível
video = yt.streams.get_highest_resolution()

# Baixar o vídeo
video.download("Insira o Path onde deve ser salvo")