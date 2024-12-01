import os
import cv2
import numpy as np

def carregarImagens(caminhoPasta, tamanhoImagem=(224, 224)):
    imagens, labels = [], []
    for label, subpasta in enumerate(['real', 'falso']):
        pasta = os.path.join(caminhoPasta, subpasta)
        for ficheiro in os.listdir(pasta):
            caminhoImagem = os.path.join(pasta, ficheiro)
            img = cv2.imread(caminhoImagem)
            if img is not None:
                img = cv2.resize(img, tamanhoImagem)
                imagens.append(img)
                labels.append(label)
    return np.array(imagens), np.array(labels)

if __name__ == "__main__":
    # Uso exemplar
    imagens, labels = carregarImagens('../data/')
    print(f"Imagem {len(imagens)} carregada.")
