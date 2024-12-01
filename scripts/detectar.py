import tensorflow as tf
import cv2
import numpy as np

def detetarImagem(caminhoImagem, caminhoModelo='../model/deepfake_detector.h5'):
    # Carrega o modelo
    modelo = tf.keras.models.load_model(caminhoModelo)
    
    # Preprocessamento da imagem
    img = cv2.imread(caminhoImagem)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    
    # Faz previsões
    previsao = modelo.predict(img)[0][0]
    return "Falso" if previsao > 0.5 else "Real"

if __name__ == "__main__":
    # Uso exemplar
    resultado = detetarImagem('../data/falso/example.jpg')
    print(f"Esta imagem foi detectada como: {resultado}")
