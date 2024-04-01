# TODO
#- [x] Escutar a fila do SQS
#- [x] Coletar o payload com o path
#- [x] Consumir arquivo CSV do S3
#- [ ] Treinar o modelo scykitlearn
#- [ ] Calcular accuracy
#- [ ] Fazer o upload do arquivo do modelo
#- [ ] Atualizar o documento no mongodb
#- [ ] Caso dê erro no treinamento, atualizar o documento com status Failed


# Arquitetura

## Publisher (Node)
- Recebe a requisição com o arquivo de treino e dados do classifier
- Faz o upload do arquivo de treino
- Valida o arquivo
- Cria um documento no mongodb com os dados do classificador
- Publica evento no SQS


## Worker (Python e Node)
- Escura a fila no SQS
- Lê os dados do evento com os dados do arquivo de treino
- Consome o arquivo de treino 
- Tenta:
    - Realiza o treinamento
    - Salva o treinamento em um modelo
    - Envia o modelo para o S3
    - Atualiza o mongodb com sucesso
- Caso falhe:
    - Atualiza o mongodb com falha


## Classifier (Node, Python)
- Recebe a requisição com sample e id
- Lê o classifier do mongodb baseado no id
- Consome o modelo do S3 baseado no path presente no documento
- Recupera o algoritmo do arquivo
- Realiza a classificação
- Responde com a cçassificação


## API (Node)
- Lê os classifiers do mongodb


    