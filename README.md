# Site Porto Máquinas

Este é o repositório do site da **Porto Máquinas**.

## Estrutura do Projeto

O código-fonte principal do site está contido na pasta `/SITE PORTO MAQUINAS`, que possui a seguinte estrutura de arquivos:

* `index.html` - Página principal do site.
* `produtos.html` - Catálogo de produtos.
* `servicos.html` - Descrição de serviços.
* `sobre.html` - Página institucional.
* `orcamento.html` - Formulário ou página de contato/orçamento.
* `/css` - Arquivos de estilos CSS.
* `/js` - Scripts Javascript.
* `/assets`, `/catalog`, `/products`, `/services` - Pastas com imagens e recursos do site.

## Como Contribuir (Fluxo de Trabalho Git)

### 1. Clonar o Repositório
No computador do colaborador:
```bash
git clone https://github.com/Linkadas/site-porto-maquinas.git
```

### 2. Criar uma Branch de Trabalho
Evite trabalhar direto na branch `main`. Crie uma branch própria para as suas alterações:
```bash
# Para criar e mudar para a sua branch:
git checkout -b <nome-da-sua-branch>
```

### 3. Enviar Alterações
Após fazer as alterações:
```bash
git add .
git commit -m "Descrição clara da sua alteração"
git push -u origin <nome-da-sua-branch>

## Como Testar Localmente

Para rodar o site no seu navegador com todas as funcionalidades (como imagens, fontes e persistência do localStorage) funcionando sem problemas de permissão local, inicie o servidor interno do Python na raiz do projeto:

```bash
# Iniciar o servidor local na porta 8080
python -m http.server 8080 --directory "SITE PORTO MAQUINAS"
```

Depois, acesse no seu navegador: **[http://localhost:8080](http://localhost:8080)**.

## Funcionalidades Adicionadas

### Carrinho de Compras (Orçamento)
Adicionada uma gaveta lateral interativa de carrinho de compras que facilita a simulação de orçamentos:
- **Botões "Adicionar ao carrinho":** Disponíveis em todos os cards nas páginas de **Produtos** e **Acessórios**.
- **Preços Fictícios:** Inseridos em todos os produtos e acessórios para viabilizar o cálculo do orçamento.
- **Persistência local:** Armazenamento automático no `localStorage`, mantendo o carrinho intacto mesmo ao mudar de página ou recarregar o navegador.
- **Controles de quantidade:** Botões para adicionar ou diminuir quantidades diretamente na barra lateral, recalculando subtotais e valor total estimado instantaneamente.
- **Finalização de Pedido:** Simulação de conclusão de orçamento com um modal de feedback moderno e limpeza automática do carrinho.

