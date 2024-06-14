## Fluxo de Processamento dos Dados

Aqui está o fluxo de processamento dos dados no código Python:

```mermaid
graph TD;
    A[Abrir arquivo CSV] --> B[Ler linhas do CSV];
    B --> C[Agrupar por motorista];
    C --> D[Para cada motorista];
    D --> E[Inicializar mensagem];
    E --> F[Adicionar detalhes de cada pacote];
    F --> G[Calcular total do prejuízo];
    G --> H[Adicionar informações adicionais];
    H --> I[Imprimir mensagem formatada];
