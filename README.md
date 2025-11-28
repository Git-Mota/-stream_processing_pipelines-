# -stream_processing_pipelines-


-configurar CLI

  instalar lib 
  pip install awscli

  
  verificar instalação
  aws --version
  
  criar arquivo CLI
  caminho:
  C:\Users\{seu usuário}\.aws
  
  crie um arquivo com nome "credentials" e faça a configurar como preferir.

-configurando região
  Rode o comando:
    aws configure
  Quando pedir “Default region name”, coloque por exemplo:
    us-east-1
-Criar kinesis
  Rode o comando:
    aws kinesis create-stream --stream-name shoptrend-events-stream --shard-count 1
  Verifique se foi criado:
    shoptrend-events-stream
-Libs:
    pip install boto3 faker









