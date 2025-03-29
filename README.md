# projeto_techstore

Documento Técnico – TechStore Amorim
1. Tecnologias Utilizadas

- Python: Linguagem de programação utilizada para o desenvolvimento do back-end.
- Django: Framework web que segue o padrão MTV, responsável por estruturar o projeto.
- SQLite: Banco de dados utilizado por padrão no Django para armazenar as informações dos produtos.
- HTML5/CSS3: Linguagens de marcação e estilização para a criação dos templates.
- Bootstrap + Bootswatch: Framework CSS para um design responsivo e visualmente agradável.
- Google Fonts: Serviço para inclusão de fontes web, como a fonte 'Roboto'.

2. Instruções para Execução do Projeto
Pré-requisitos:

- Python 3.13 (ou versão compatível).
- Pip: Gerenciador de pacotes do Python. 

Passos para Configuração e Execução:

1. Clonar o repositório ou criar a estrutura do projeto:
   git clone 
   cd projeto_CRUD

2. Instalar as dependências:
   pip install -r requirements.txt
   (Caso não haja um arquivo requirements.txt, instale o Django com: pip install django)

3. Configurar o banco de dados:
   - O Django já vem configurado para utilizar SQLite. Para usar outro SGBD, ajuste o arquivo settings.py.

4. Realizar as migrações do banco de dados:
   python manage.py makemigrations
   python manage.py migrate

5. Executar o servidor de desenvolvimento:
   python manage.py runserver

6. Acessar a aplicação no navegador:
   http://127.0.0.1:8000/produtos/

3. Possíveis Melhorias Futuras

- **Segurança:**
  - Implementar autenticação e autorização para gerenciar acessos e restrições no CRUD.
  - Integrar proteções adicionais como rate limiting e proteção contra ataques de força bruta.

- **Interface e Experiência do Usuário:**
  - Investir em um design customizado utilizando frameworks modernos, como Tailwind CSS.
  - Adicionar feedbacks visuais (notificações, loaders, mensagens de sucesso/erro) e animações suaves.

- **Funcionalidades Adicionais:**
  - Implementar filtros de busca e ordenação para facilitar a navegação pelos produtos.
  - Adicionar paginação para melhorar a usabilidade em listas extensas.
  - Permitir o upload de imagens para os produtos, integrando funcionalidades de armazenamento de arquivos.
  - Desenvolver uma API RESTful para integração com aplicativos mobile ou outros sistemas.

- **Infraestrutura e Deploy:**
  - Preparar o projeto para deploy em produção com servidores como Gunicorn e Nginx.
  - Migrar do SQLite para um SGBD mais robusto, como PostgreSQL ou MySQL.
  - Integrar ferramentas de monitoramento e logging para acompanhar o desempenho do sistema.

