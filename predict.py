from ultralytics import YOLO
import cv2 as cv
import os

# Carrengado o modelo treinado
model = YOLO('YOLOv8-model/model/best.pt')

# Path da imagem a ser analisada
image = 'Walls/cracked/8.jpg'

# Fazendo a analise da imagem com o modelo
predict = model.predict(image)

# Olhando quantos arquivos tem na pasta de predições para salvar o arquivo com um nome que ainda não existe
files_amount = len(os.listdir('Predictions'))

# Salvando a imagem com o resultado da analise
print("-------------------------------------------")
print(f"Imagem -> result{files_amount}.jpg <- salva com sucesso!")
print("-------------------------------------------")

cv.imwrite(f'Predictions/result{files_amount}.jpg', predict[0].plot())
