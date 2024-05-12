
<div align="center">
<img align="center" alt="Povoa-java" height="250" width="250" src="https://github.com/devpovoa/DevPovoa/assets/75958253/447062bb-16b9-4a8d-96ae-882a725e6562"">

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

![GitHub Org's stars](https://img.shields.io/github/stars/DevPovoa?style=social)
</div>

# Sumário :bookmark_tabs:
### Códigos em Python 🐍

<p>Projeto de um gerenciador de cadastro de Produtos usando Python e PostgreSQL.</p>


### Ferramentas utilizada para desenvolvimento :hammer:

<ul>
    <li>Sistema Operacional Linux - Distro Ubuntu</li>
    <li>VSCode</li>
    <li>Python</li>
    <li>PostgreSQL</li>
</ul>

### O modelo para a criação da tabela no Banco de Dados Postgres.
```Postgres
CREATE TABLE IF NOT EXISTS public."PRODUTO"
(
    codigo integer NOT NULL,
    nome text COLLATE pg_catalog."default" NOT NULL,
    preco real NOT NULL,
    CONSTRAINT "PRODUTO_pkey" PRIMARY KEY (codigo)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."PRODUTO"
    OWNER to postgres;
```
## ⚠️ Warning 
### ℹ️ Não deixe de trocar as informaçoes de conexão no AppDB.py, caso contrário não vai funcionar.

```Python
self.connection = connectar.connect(
                database="seu_bancoDeDados_BD", host="seu_host_de_preferencia", user="seu_usuário", password="sua_senha", port="sua_porta_configurada")
```
