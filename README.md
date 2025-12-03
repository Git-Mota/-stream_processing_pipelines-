# Stream Processing Pipelines - AWS

<details>
<summary>Configuração CLI</summary>

### Instalar CLI

```bash
pip install awscli
```

### Verificar instalação

```bash
aws --version
```

### Criar arquivo CLI

Caminho do arquivo:

```
C:\Users\{seu usuário}\.aws
```

Crie um arquivo chamado `credentials` e configure suas credenciais da AWS como preferir.

</details>

<details>
<summary>Configuração Região</summary>

### Rodar comando de configuração

```bash
aws configure
```

Quando pedir “Default region name”, coloque por exemplo:

```
us-east-1
```

</details>

<details>
<summary>Configuração Ambiente</summary>

### Criar ambiente virtual se ainda não tiver:

```bash
python -m venv venv
```

Ativar ambiente:

Windows:

```
venv\Scripts\activate.bat
```
Linux:

```
source venv/bin/activate
```

</details>

<details>
<summary>Configuração Dependências</summary>

### Rodar comando de instalação

```bash
pip install -r requirements.txt
```

</details>

<details>
<summary>Infra</summary>

<details>
<summary>Via Terraform</summary>

<details>
<summary>Windows</summary>

### Baixar Terraform

```powershell
Invoke-WebRequest `
-Uri "https://releases.hashicorp.com/terraform/1.11.2/terraform_1.11.2_windows_amd64.zip" `
-OutFile "terraform_1.11.2_windows_amd64.zip"
```

### Extrair ZIP

```powershell
Expand-Archive -Path terraform_1.11.2_windows_amd64.zip -DestinationPath .\terraform
```

### Configurar AWS Account ID

Crie o arquivo `terraform.tfvars` e preencha:

```hcl
aws_account_id = "seu-id-aqui"
```

### Rodar Terraform

```powershell
.\terraform\terraform.exe init
.\terraform\terraform.exe validate
.\terraform\terraform.exe plan
```

</details>

<details>
<summary>Linux</summary>

### Baixar Terraform

```bash
wget https://releases.hashicorp.com/terraform/1.11.2/terraform_1.11.2_linux_amd64.zip
```

### Extrair ZIP

```bash
unzip terraform_1.11.2_linux_amd64.zip -d terraform
```

### Configurar AWS Account ID

Crie o arquivo `terraform.tfvars`:

```hcl
aws_account_id = "seu-id-aqui"
```

### Rodar Terraform

```bash
./terraform/terraform init
./terraform/terraform validate
./terraform/terraform plan
```

</details>


</details>
<details>
<summary>Manual</summary>

<details>


<summary>Criar Kinesis</summary>

Rode o comando:

```bash
aws kinesis create-stream --stream-name shoptrend-events-stream --shard-count 1
```

Verifique se foi criado:

```
shoptrend-events-stream
```

</details>

<details>
<summary>Criar S3</summary>

* Nome do bucket: `shoptrend-datalake-landing`

</details>

<details>
<summary>Criar Firehose</summary>

* Origem: Kinesis
* Destino: S3
* Nome do Kinesis: `arn:aws:kinesis:us-east-1:100434586124:stream/shoptrend-events-stream`
* Bucket do S3: `s3://shoptrend-datalake-landing`
* Prefixo do bucket S3: `raw/events/!{timestamp:yyyy}/!{timestamp:MM}/!{timestamp:dd}/`
* Prefixo de saída de erro do bucket S3: `raw/errors/!{firehose:error-output-type}/`
* Compactação para registros de dados: GZIP

</details>
</details>
</details>





<details>
<summary>Eventos</summary>

### checkout

* Representa o momento em que o cliente:

  * entrou na página de fechamento da compra, ou
  * revisou o carrinho, endereço e pagamento, ou
  * clicou em “Finalizar Compra”, mas ainda não concluiu o pagamento.
* É um evento que mostra intenção forte de compra, mas não é a compra finalizada.

### pageview

* A visualização de uma página do site
* O início ou continuação de uma sessão
* A navegação do usuário (ex.: página do produto, homepage, carrinho, checkout)

### add_to_cart

* Mostra quais produtos estão chamando atenção
* Permite medir conversão entre “ver produto → adicionar ao carrinho”
* Alimenta KPIs de interesse e demanda
* Ajuda a prever estoque necessário
* Permite ações de remarketing (ex: lembrar que ele deixou itens no carrinho)

### order_confirmed

* Representa o momento em que a compra é realmente c
