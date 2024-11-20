
# Django Blog Project

Este é um projeto Django básico para um blog. O projeto inclui funcionalidades como criação de postagens, tags, e autenticação de usuário admin.

## Pré-requisitos

Antes de começar, você precisa ter o Python instalado em seu sistema.

- Python 3.x

## Configuração do Ambiente

Siga os passos abaixo para configurar o ambiente de desenvolvimento para o projeto.

### 1. Criar um ambiente virtual

Para criar um ambiente virtual, execute o seguinte comando no terminal:

```bash
python -m venv [nome_da_venv]
```

Substitua `[nome_da_venv]` pelo nome que você deseja para o seu ambiente virtual.

### 2. Ativar o ambiente virtual

#### No Linux/macOS:

```bash
source [nome_da_venv]/bin/activate
```

#### No Windows:

```bash
[nome_da_venv]\Scripts\activate
```

### 3. Instalar dependências

Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### 4. Aplicar migrações

Para configurar o banco de dados e aplicar as migrações, execute o seguinte comando:

```bash
python manage.py migrate
```

### 5. Criar um superusuário

Rode o comando abaixo para que o usuário padrão seja aplicado ao banco de dados:

```bash
python create_superuser.py
```

### 6. Executar o servidor

Agora, você pode iniciar o servidor de desenvolvimento local com o comando:

```bash
python manage.py runserver
```

O servidor estará disponível em `http://127.0.0.1:8000/`.

## Estrutura do Projeto

- `core/` - Interface do app 'core' com templates, controle de exibição de posts e rotas.
- `blog/` - Contém a configuração principal (geral) do projeto.

## License

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
