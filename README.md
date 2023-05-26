# Cracked-wall-analysis-YOLOv8  
Esse repositório tem como objetivo armazenar os códigos e arquivos para uma atividade avaliada da faculdade Inteli.
O objetivo da atividade é prepara um modelo de detecção de objetos para identificar rachaduras em paredes. O modelo deve ser capaz de receber uma imagem e identificar as rachaduras nela contidas, desenhando um retângulo em volta de cada uma delas. Isso deverá acontecer com imagens estáticas ou com vídeos ao vivo.  
___
**Exemplo**:

___

## O Modelo   
Para a análise da imagem, é utilizado um modelo pré-treinado, o [YOLOv8](https://github.com/ultralytics/ultralytics). YOLOv8 é a versão mais avançada do sistema de detecção de objetos YOLO (You Only Look Once) atualmente. O YOLO é um método popular de detecção de objetos em tempo real que identifica objetos em uma imagem e fornece uma caixa delimitadora ao redor deles. O nome "You Only Look Once" deriva do fato de que o sistema processa a imagem inteira em uma única vez, em vez de procurar objetos em várias regiões de interesse na imagem, como fazem muitos outros sistemas de detecção de objetos.

## Preparação do conjunto de dados
Foi selecionado um conjunto de dados que contém 4029 imagens de rachaduras em paredes. Este conjunto de dados é dividido em treinamento, validação e teste, com 3700, 200 e 129 imagens respectivamente, advindos de [RoboFlow](https://universe.roboflow.com/university-bswxt/crack-bphdr/dataset/2). Nas imagens, as rachaduras são rotuladas com caixas delimitadoras (caso possuam rachaduras).  
___
**_Observação_**: Não foi necessário realizar um pré-processamento personalizado das imagens, uma vez que as imagens coletadas do RoboFlow já estavam adequadamente anotadas conforme a necessidade do modelo. Além disso, o YOLOv8 possui uma pipeline de pré-processamento embutida, que pode incluir uma série de tarefas fundamentais para o processamento adequado das imagens. Quando uma imagem é submetida para predição ou um conjunto de dados para treinamento, o modelo YOLOv8 inicia uma sequência de operações de pré-processamento. Um desses processos é o redimensionamento da imagem para as dimensões esperadas pelo modelo, uma etapa que contribui para a eficiência e consistência do processamento de imagem pela rede neural. Outra operação realizada é a normalização dos pixels da imagem. Este é um passo importante para modelos de aprendizado de máquina em geral, uma vez que garante que todas as imagens tenham uma distribuição semelhante de valores de pixel, reduzindo a sensibilidade do modelo a variações na iluminação e no contraste. Adicionalmente, o modelo YOLOv8 pode incluir outras transformações de pré-processamento, como técnicas de aumento de dados. Estas podem envolver operações como rotações, translações, zoom e inversões da imagem, que ajudariam a aumentar a robustez do modelo, permitindo que ele reconheça objetos em uma variedade maior de condições e orientações. Portanto, mesmo que não tenha sido aplicado um tratamento específico às imagens, isso não significa que elas não foram processadas.  
___
## Treinamento  
Para o treinamento do modelo, foi utilizado o Google Colab (o Jupyter Notebook pode ser encontrado [aqui](./YOLOv8_train.ipynb)). Como estamos utilizando um modelo pré-treinado, o treinamento com os dados selecionados foi realizado em 10 épocas, com um tamanho de batch de 16 e uma taxa de aprendizado de 0.001, tendo como base o modelo padrão do YOLOv8.  
O código abaixo mostra a configuração do treinamento (observe que estamos colocando um ponto de exclamação antes do comando, pois estamos executando um comando do sistema operacional no Google Colab):  
```jupyter
!yolo train data=/content/crack-2/data.yaml model=yolov8n.pt epochs=10 lr0=0.01 
```
- **Épocas**: Uma época representa uma passagem completa de todos os exemplos de treinamento através do modelo. No nosso caso, o modelo é treinado por 10 épocas, ou seja, ele vê todos os exemplos de treinamento 10 vezes.  

- **Batch Size**: O tamanho do batch refere-se ao número de exemplos de treinamento usados em uma única atualização do gradiente. Um tamanho de batch menor pode levar a atualizações mais frequentes, enquanto um tamanho de batch maior resulta em atualizações menos frequentes. No nosso caso, usamos um tamanho de batch de 16.  

- **Taxa de Aprendizado (Learning Rate)**: A taxa de aprendizado é o controle do tamanho de cada atualização de pesos e vieses ao longo do treinamento do modelo. Essas atualizações acontecem a cada batch. Uma taxa de aprendizado muito alta pode causar oscilações e a incapacidade do modelo de aprender, enquanto uma taxa de aprendizado muito baixa pode fazer com que o aprendizado seja muito lento. No nosso caso, a taxa de aprendizado inicial é 0.001.  

Ao final, o modelo é salvo em um [arquivo .pt](./YOLOv8-model/model/best.pt), o qual importamos para esse projeto.
## Predição  
Após o treinamento, o modelo é capaz de prever a localização de rachaduras em novas imagens. Ele faz isso ao analisar a imagem e identificar áreas que se assemelham às rachaduras que aprendeu durante o treinamento. Para a análise do vídeo ao vivo, foi utilizado a biblioteca OpenCV que efetua a captura de frames do vídeo e os envia para o modelo. O modelo, por sua vez, retorna as imagens com as rachaduras identificadas. Por fim, o vídeo é gerado com as imagens processadas(as imagens processadas podem ser encontradas em: [/Predictions](./Predictions/)).  

## Como rodar o projeto  
Para rodar o projeto, é necessário ter o Python 3.7 ou superior instalado. Além disso, é necessário instalar as bibliotecas necessárias para o projeto. Para isso, basta executar o seguinte comando no terminal:  
```shell
pip install -r requirements.txt
```
Após a instalação das bibliotecas, basta executar os seguintes comandos no terminal para cada tarefa que deseja realizar:
- Para rodar o modelo em imagens estáticas, faça o upload da imagem para a pasta [/Walls](./Walls), modifique o caminho da imagem que está sendo armazenado na variável `image` e execute o seguinte comando no terminal: 
```shell
python3 predict.py
```
A imagem com as rachaduras identificadas será gerada na pasta [/Predictions](./Predictions/).
- Para rodar o modelo de vídeo, bastar executar o seguinte comando no terminal: 
```shell
python3 predict_video.py
```