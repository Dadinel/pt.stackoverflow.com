Estou criando chaves primárias e estrangeiras com  a constraint NOT NULL no PostgreSQL, só o jeito que eu estou fazendo isso é indo nas propriedades na tabela e definindo manualmente as chaves como NOT NULL, eu gostaria de fazer isso através dos códigos de criação da tabela.

Logo abaixo está algumas tabelas do meu banco para que possam entender e me ajudar nessa minha dúvida

```
CREATE TABLE endereco_fornecedor (
  cd_endereco_fornecedor SERIAL PRIMARY KEY,
  cidade VARCHAR(30),
  bairro VARCHAR(30),
  endereco VARCHAR(30),
  numero_endereco INT
)

CREATE TABLE telefone_fornecedor (
  cd_telefone_fornecedor SERIAL PRIMARY KEY,
  telefone_fornecedor VARCHAR(15)
)

CREATE TABLE fornecedor (
  cd_fornecedor SERIAL PRIMARY KEY,
  cd_endereco_fornecedor INT,
  cd_telefone_fornecedor INT,
  cnpj_fornecedor VARCHAR(18),
  nome_fornecedor VARCHAR(30),
  email_fornecedor VARCHAR(50),
  foreign key (cd_endereco_fornecedor) references endereco_fornecedor (cd_endereco_fornecedor),
  foreign key (cd_telefone_fornecedor) references telefone_fornecedor (cd_telefone_fornecedor)	
)
```
