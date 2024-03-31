# Exemplo de uso
#from src.infra.ClassifierController import ClassifierController
from src.infra.SQSConsumer import SQSConsumer

# TODO
#- [x] Escutar a fila do SQS
#- [ ] Coletar o payload com o path
#- [ ] Consumir arquivo CSV do S3
#- [ ] Treinar o modelo scykitlearn
#- [ ] Calcular accuracy
#- [ ] Fazer o upload do arquivo do modelo
#- [ ] Atualizar o documento no mongodb
#- [ ] Caso dê erro no treinamento, atualizar o documento com status Failed


queue_url = 'URL_DA_SUA_FILA_SQS'
print(queue_url)

sqs_consumer = SQSConsumer(queue_url)

#sqs_consumer.poll_messages(
#    handler=ClassifierController.handle_message
#)