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





