# Gerador de Senhas Seguras (Safe Password Generator)

Uma aplicação profissional de linha de comando (CLI) e Web que gera senhas aleatórias e seguras com base em critérios definidos pelo usuário (tamanho, inclusão de caracteres especiais, números e letras maiúsculas/minúsculas).

## Tecnologias
- **Linguagem:** Python 3.9+
- **Frontend Web:** Streamlit
- **CLI:** `argparse` (nativo do Python)
- **Testes e Qualidade:** `pytest`, `black`, `flake8`

## Estrutura do Projeto
- `src/safe_password_generator/core`: Lógica de negócio e geração de senhas seguras.
- `src/safe_password_generator/cli`: Interface de linha de comando.
- `src/safe_password_generator/web`: Interface web construída com Streamlit.
- `tests/`: Bateria de testes automatizados com `pytest`.

## Instalação (Desenvolvimento)

1. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

2. Instale as dependências de desenvolvimento:
```bash
pip install -r requirements-dev.txt
pip install -e .
```

## Como Usar
*(Instruções detalhadas serão adicionadas em breve)*

## Testes
Para rodar a suíte de testes:
```bash
pytest
```

## Licença
Este projeto está licenciado sob a licença MIT.