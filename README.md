## Fluxo de Processamento dos Dados

O código Python lê dados de um arquivo CSV que contém informações sobre descontos relacionados a entregas afetadas durante o transporte. Ele agrupa essas informações por motorista e gera mensagens personalizadas para cada um. Cada mensagem informa ao motorista sobre a necessidade de aplicar descontos em futuros fretes devido aos eventos ocorridos. As mensagens incluem detalhes específicos de cada entrega afetada, como número de rastreamento (SPX TRACKING NUMBER), data de coleta, e o valor do prejuízo. Além disso, calcula o total do prejuízo para cada motorista e inclui instruções sobre como será aplicado o desconto e quais as ações a serem tomadas caso haja dificuldades no pagamento dos descontos.

Aqui está o fluxo de processamento dos dados no código Python:
```mermaid
graph TD;
    style A fill:#f9f,stroke:#333,stroke-width:4px;
    style B fill:#f9f,stroke:#333,stroke-width:4px;
    style C fill:#f9f,stroke:#333,stroke-width:4px;
    style D fill:#f9f,stroke:#333,stroke-width:4px;
    style E fill:#f9f,stroke:#333,stroke-width:4px;
    style F fill:#f9f,stroke:#333,stroke-width:4px;
    style G fill:#f9f,stroke:#333,stroke-width:4px;
    style H fill:#f9f,stroke:#333,stroke-width:4px;
    style I fill:#f9f,stroke:#333,stroke-width:4px;

    A[Abrir arquivo CSV] --> B[Ler linhas do CSV];
    B --> C[Agrupar por motorista];
    C --> D[Para cada motorista];
    D --> E[Inicializar mensagem];
    E --> F[Adicionar detalhes de cada pacote];
    F --> G[Calcular total do prejuízo];
    G --> H[Adicionar informações adicionais];
    H --> I[Imprimir mensagem formatada];

    %% Estilos adicionais
    style A fill:#86bbf5,stroke:#333,stroke-width:2px,stroke-dasharray: 5, 5;
    style B fill:#86bbf5,stroke:#333,stroke-width:2px,stroke-dasharray: 5, 5;
    style C fill:#86bbf5,stroke:#333,stroke-width:2px,stroke-dasharray: 5, 5;
    style D fill:#86bbf5,stroke:#333,stroke-width:2px,stroke-dasharray: 5, 5;
    style E fill:#86bbf5,stroke:#333,stroke-width:2px,stroke-dasharray: 5, 5;
    style F fill:#86bbf5,stroke:#333,stroke-width:2px,stroke-dasharray: 5, 5;
    style G fill:#86bbf5,stroke:#333,stroke-width:2px,stroke-dasharray: 5, 5;
    style H fill:#86bbf5,stroke:#333,stroke-width:2px,stroke-dasharray: 5, 5;
    style I fill:#86bbf5,stroke:#333,stroke-width:2px,stroke-dasharray: 5, 5;

    %% Personalizando setas
    B -->|Leitura de Dados| C;
    C -->|Agrupamento| D;
    D -->|Iteração| E;
    E -->|Montagem de Mensagem| F;
    F -->|Cálculo de Prejuízo| G;
    G -->|Adição de Detalhes| H;
    H -->|Finalização e Impressão| I;
