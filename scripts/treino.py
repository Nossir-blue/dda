import tensorflow as tf
from tensorflow.keras import layers, models
from scripts.preprocesso import carregarImagens

# Carrega os dados
directorioDados = '../data/'
imagens, labels = carregarImagens(directorioDados)
imagens = imagens / 255.0  # Normaliza os valores dos píxeis

# Separa os dados em conjuntos de treino e de testes
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(imagens, labels, test_size=0.2, random_state=42)

# Define o modelo
modelo = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid')  # Classificação de binário
])

# Compila o modelo
modelo.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Treina o modelo
historico = modelo.fit(X_train, y_train, epochs=10, validation_split=0.2, batch_size=32)

# Guarda o modelo
modelo.save('../modelo/deepfake_detector.h5')

# Avalia o modelo
test_loss, test_acc = modelo.evaluate(X_test, y_test, verbose=2)
print(f"Precisão do teste: {test_acc:.2f}")
