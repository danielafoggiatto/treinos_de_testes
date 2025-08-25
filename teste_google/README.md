# Plano de Teste: Acessar a página home do Google e testar funcionalidades

## Informações Gerais
- **Id:** 001  
- **Objetivo:** Acessar a página home do Google e testar funcionalidades, como pesquisar, estou com sorte, imagens, etc  
- **Ferramentas:** Selenium, Pytest  
- **Critérios de Aceite:** Página do Google disponível.  

## Escopo
- Validação do carregamento da página inicial do Google.  
- Teste da barra de pesquisa (consultas válidas e inválidas).  
- Teste do botão “Pesquisa Google” e “Estou com sorte”.  
- Acesso à aba Imagens.  

## Fora do Escopo
- Funcionalidades de login/conta Google.  
- Testes relacionados ao Gmail, Google Drive, YouTube, Maps, etc.  
- Desempenho e tempo de resposta da página.  

## Resultado Geral Esperado
Todas as funcionalidades funcionando conforme solicitado.  

---

## Casos de Teste

| Id  | Caso de Teste (Objetivo) | Pré-condições | Passos | Resultado Esperado | Prioridade |
|-----|--------------------------|---------------|--------|--------------------|------------|
| 001 | Validar se a pesquisa por “Pytest” no Google retorna a página | Estar com a página inicial do Google aberta | 1. Digitar na barra de pesquisa: “Pytest” <br> 2. Clicar em “Pesquisa Google” <br> 3. Clicar em ‘pytest documentation’ nos resultados | O sistema deve abrir corretamente a página oficial do pytest documentation, sem erros de navegação | Baixa |
| 002 | Validar pesquisa com palavra sem sentido no Google | Estar com a página inicial do Google aberta | 1. Digitar na barra de pesquisa: “asdjioasijfoiaskfopaisf0kopsq” <br> 2. Clicar em “Pesquisa Google” | O Google deve exibir mensagem: “Sua pesquisa não encontrou nenhum documento correspondente” com sugestões | Baixa |
| 003 | Validar se a pesquisa “Pytest Estou com sorte” acessa a página de documentação | Estar com a página inicial do Google aberta | 1. Digitar na barra de pesquisa: “Pytest” <br> 2. Clicar em “Estou com sorte” | O sistema deve abrir corretamente a página de documentação com o título: “pytest: helps you write better programs” | Baixa |
| 004 | Validar se a pesquisa de Imagens funciona | Estar com a página inicial do Google aberta | 1. Clicar em Imagens <br> 2. Digitar “pytest” <br> 3. Clicar em “Pesquisa Google” | O sistema deve abrir imagens correspondentes à “pytest” sem erros | Baixa |
