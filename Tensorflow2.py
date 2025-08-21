import cv2
import pytesseract
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pyttsx3
import time

# Atualize o caminho para o local correto do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\maratona\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Inicializa o motor de texto para fala
engine = pyttsx3.init()

# Defina o formato de entrada; por exemplo, se você estiver usando imagens 28x28 pixels
input_shape = 784  # 28x28 imagens achatadas em um vetor de 784

# Criação do modelo
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(input_shape,)),
    layers.Dense(10, activation='softmax')  # Saída para 10 classes
])

# Compilação do modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Resumo do modelo
model.summary()

# Captura da câmera
cap = cv2.VideoCapture(1)

# Para armazenar o texto lido
previous_text = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Pré-processamento
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Reconhecimento de texto
    text = pytesseract.image_to_string(gray, lang='por')
    if text != previous_text and text.strip() != "":
        print("Texto reconhecido:", text)
        engine.say(text)  # Fala o texto reconhecido
        engine.runAndWait()  # Aguarda a fala terminar
        previous_text = text  # Atualiza o texto anterior

    # Exibir a imagem
    cv2.imshow('Captura', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




