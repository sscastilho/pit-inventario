# 📦 Sistema de Controle de Inventário VERSÃO 2.0

Este repositório contém o código-fonte do **Projeto Integrador Transdisciplinar em Engenharia de Software II**. Trata-se de uma aplicação web para gestão de estoque, desenvolvida seguindo a arquitetura **MVC** (Model-View-Controller) e princípios de melhoria contínua (*Kaizen*).

## 🚀 Sobre o Projeto

O objetivo foi desenvolver uma solução funcional (MVP) para controle de entradas e saídas de materiais, garantindo a integridade dos dados e usabilidade. O sistema permite o cadastro de itens, categorização e registro de movimentações com validações de regras de negócio.

**Versão Atual:** 2.0 (Com correções de usabilidade e regras de negócio aplicadas após testes de usuário).

## ✨ Funcionalidades

* **Autenticação:** Sistema de Login seguro com controle de sessão.
* **Dashboard:** Visão geral do estoque com indicadores visuais de nível crítico (cores).
* **CRUD Completo:**
    * **C**adastro de novos itens.
    * **L**eitura/Listagem de itens.
    * **A**tualização (Edição) de itens.
    * **E**xclusão de itens (com confirmação de segurança).
* **Movimentação de Estoque:** Registro de Entradas e Saídas.
* **Regras de Negócio:** Bloqueio automático de saídas caso o estoque seja insuficiente (impede estoque negativo).
* **Responsividade:** Interface adaptável para mobile e desktop (Bootstrap 5).

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Framework Web:** Flask (Micro-framework)
* **Banco de Dados:** SQLite3
* **Front-end:** HTML5, Jinja2, CSS3 (Framework Bootstrap 5.3)
* **Ambiente de Desenvolvimento:** Replit

## 📂 Estrutura do Projeto (MVC)

```text
pit-inventario/
│
├── database.db          # Banco de Dados SQLite
├── main.py              # Controller (Lógica de rotas e conexão com DB)
├── README.md            # Documentação do projeto
└── templates/           # Views (Interfaces HTML)
    ├── login.html       # Tela de Acesso
    ├── dashboard.html   # Tela Principal (Listagem)
    ├── novo_item.html   # Formulário de Cadastro
    ├── editar_item.html # Formulário de Edição
    └── movimentacao.html# Tela de Entrada/Saída

Com certeza\! Um bom `README.md` é essencial para apresentar seu projeto no GitHub. Ele serve como a "capa" do seu trabalho, explicando o que é, como funciona e quais tecnologias foram usadas.

Abaixo está um modelo profissional e pronto, adaptado exatamente para o **Sistema de Inventário V2.0** que construímos.

### 📝 Como adicionar ao seu projeto:

1.  No **Replit** ou no **GitHub**, crie um novo arquivo chamado **`README.md`** (exatamente assim, com letras maiúsculas).
2.  Copie todo o código abaixo e cole nesse arquivo.
3.  Faça o **Commit & Push** para atualizar no GitHub.

-----

````markdown
# 📦 Sistema de Controle de Inventário

Este repositório contém o código-fonte do **Projeto Integrador Transdisciplinar em Engenharia de Software II**. Trata-se de uma aplicação web para gestão de estoque, desenvolvida seguindo a arquitetura **MVC** (Model-View-Controller) e princípios de melhoria contínua (*Kaizen*).

## 🚀 Sobre o Projeto

O objetivo foi desenvolver uma solução funcional (MVP) para controle de entradas e saídas de materiais, garantindo a integridade dos dados e usabilidade. O sistema permite o cadastro de itens, categorização e registro de movimentações com validações de regras de negócio.

**Versão Atual:** 2.0 (Com correções de usabilidade e regras de negócio aplicadas após testes de usuário).

## ✨ Funcionalidades

* **Autenticação:** Sistema de Login seguro com controle de sessão.
* **Dashboard:** Visão geral do estoque com indicadores visuais de nível crítico (cores).
* **CRUD Completo:**
    * **C**adastro de novos itens.
    * **L**eitura/Listagem de itens.
    * **A**tualização (Edição) de itens.
    * **E**xclusão de itens (com confirmação de segurança).
* **Movimentação de Estoque:** Registro de Entradas e Saídas.
* **Regras de Negócio:** Bloqueio automático de saídas caso o estoque seja insuficiente (impede estoque negativo).
* **Responsividade:** Interface adaptável para mobile e desktop (Bootstrap 5).

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Framework Web:** Flask (Micro-framework)
* **Banco de Dados:** SQLite3
* **Front-end:** HTML5, Jinja2, CSS3 (Framework Bootstrap 5.3)
* **Ambiente de Desenvolvimento:** Replit

## 📂 Estrutura do Projeto (MVC)

```text
pit-inventario/
│
├── database.db          # Banco de Dados SQLite
├── main.py              # Controller (Lógica de rotas e conexão com DB)
├── README.md            # Documentação do projeto
└── templates/           # Views (Interfaces HTML)
    ├── login.html       # Tela de Acesso
    ├── dashboard.html   # Tela Principal (Listagem)
    ├── novo_item.html   # Formulário de Cadastro
    ├── editar_item.html # Formulário de Edição
    └── movimentacao.html# Tela de Entrada/Saída
````

## ⚙️ Como Executar

### Pré-requisitos

  * Python 3 instalado.
  * Bibliotecas: `flask`

### Passo a Passo

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/sscastilho/pit-inventario.git](https://github.com/sscastilho/pit-inventario.git)
    ```
2.  Instale as dependências (caso rode localmente):
    ```bash
    pip install flask
    ```
3.  Execute o servidor:
    ```bash
    python main.py
    ```
4.  Acesse no navegador: `http://localhost:8080`

## 🔑 Acesso para Testes

Para fins acadêmicos e de teste, utilize as credenciais padrão já configuradas no banco de dados:

  * **Usuário:** `admin@email.com`
  * **Senha:** `1234`

## 📈 Melhorias da Versão 2.0 (Ciclo Kaizen)

Após a etapa de validação com usuários (Situação-Problema 3), foram implementadas as seguintes correções:

1.  **Trava de Estoque:** Implementação de lógica condicional no Back-end para impedir que o saldo de um item fique negativo durante uma saída.
2.  **Gestão de Itens:** Adição das rotas e botões de **Editar** e **Excluir**, permitindo a correção de erros de cadastro.

-----

**Desenvolvido por:** Sullivan Castilho

```
```
