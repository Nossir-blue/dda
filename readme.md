# DEEPFAKE

## COMO CONTINUAR?

Baixa o Python 3.10 porque não sei quais são as versões do Python em que o Tensorflow funciona
portanto para safe measure, instale essa versão

https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe

### Como instalar?

Abra o instalador e tem dois checkboxes em baixo, aperte neles

depois vá em "install now"

depois daí é só tudo "Next"

## Python instalado, e agora?

Aperta na tecla Windows e procure por CMD

Uma vez aberto, tu vai instalar todas as coisas que estão no ./requisitos.txt usando  "pip install [nome_da_biblioteca]

### Uma maneira mais fácil e rápida de instalar tudo

vá nos ./requisitos.txt e copie tudo, depois vá no CMD e escreva "pip install [aqui tu dás ctrl + v para colar tudo que copiaste]

Espera tudo instalar

### OBS -> A instalação de todas essas bibliotecas são com internet

## Ok, baixei tudo, e agora?

Agora procura por imagens deepfakes e imagens reais, as reais tu vais meter em ./data/real e as falsas vais meter em ./data/falso

### OBS -> Elas precisam ser imagens da mesma fonte

Por exemplo, a imagem real tem que ser tua, a imagem falsa tem que ser o deepfake onde meteram a cara do Will Smith na tua cara

## Ok, fiz isso, e agora?

Se tens o VSCode, vá no terminal do VSCode e escreva nesta ordem:

python scripts/preprocess.py

python scripts/train.py

python scripts/detect.py
