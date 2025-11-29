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


Infra:

  Via terrafomr:
    Windows:

        baixar terraform

        Invoke-WebRequest `
        -Uri "https://releases.hashicorp.com/terraform/1.11.2/terraform_1.11.2_windows_amd64.zip" `
        -OutFile "terraform_1.11.2_windows_amd64.zip"

        Extrair Zip:

        Expand-Archive -Path terraform_1.11.2_windows_amd64.zip -DestinationPath .\terraform

        configurar AWS Account ID

        crie o arquivo "terraform.tfvars" e prencha com seu id:

        aws_account_id = "seu-id-aqui"

        rodar terraform

        .\terraform\terraform.exe init
        .\terraform\terraform.exe validate
        .\terraform\terraform.exe plan



    

-Criar kinesis


  Rode o comando:

    aws kinesis create-stream --stream-name shoptrend-events-stream --shard-count 1


  Verifique se foi criado:

    shoptrend-events-stream


-Libs:

    pip install boto3 faker

--------------------------

Criar S3 


- nome do s3: shoptrend-datalake-landing


Criar Firehose
- Origem: Kinesis
- Destino: S3
- nome do Kinesis: arn:aws:kinesis:us-east-1:100434586124:stream/shoptrend-events-stream
- Bucket do S3: s3://shoptrend-datalake-landing
- Prefixo do bucket S3: raw/events/!{timestamp:yyyy}/!{timestamp:MM}/!{timestamp:dd}/
- Prefixo de saída de erro do bucket S3: raw/errors/!{firehose:error-output-type}/
- Compactação para registros de dados: GZIP










-----------------

checkout:

Ele representa o momento em que o cliente:
entrou na página de fechamento da compra, ou
revisou o carrinho, endereço e pagamento, ou
clicou em “Finalizar Compra”, mas ainda não concluiu o pagamento.
É um evento que mostra intenção forte de compra, mas não é a compra finalizada.

pageview:

A visualização de uma página do site
O início ou continuação de uma sessão
A navegação do usuário (ex.: página do produto, homepage, carrinho, checkout)

add_to_cart:

mostra quais produtos estão chamando atenção
permite medir conversão entre “ver produto → adicionar ao carrinho”
alimenta KPIs de interesse e demanda
ajuda a prever estoque necessário
permite ações de remarketing (ex: lembrar que ele deixou itens no carrinho)

order_confirmed

representa o momento em que a compra é realmente concluída no e-commerce 
o pedido foi finalizado, o pagamento aprovado e o sistema confirma a ordem.





