# Gerador de Senhas Seguras (Safe Password Generator)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B.svg)](https://streamlit.io/)

Uma aplicação profissional que oferece tanto uma **Interface de Linha de Comando (CLI)** quanto uma **Interface Web (Streamlit)** para gerar senhas aleatórias e criptograficamente seguras.

---

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido para o **Laboratório Introdutório: Construindo um Mini-projeto com Inteligência Artificial Generativa [ESP T1 ES C4]**, oferecido pela Pós-Graduação em *Engenharia de Software: Automação e Inovação com Inteligência Artificial Generativa*, da **AKCIT - UFG**.

---

## 🔒 Por que as senhas geradas são realmente seguras?

Muitos geradores de senha utilizam funções de pseudo-aleatoriedade (como o módulo `random` tradicional do Python), que **não** são adequadas para fins de segurança, pois seus padrões podem ser previstos.

Este projeto foi construído focando em segurança de alto nível:
1. **Módulo `secrets`:** Utilizamos exclusivamente o módulo `secrets` nativo do Python, que é projetado especificamente para criptografia e gerenciamento de senhas. Ele acessa a fonte de aleatoriedade mais confiável provida pelo Sistema Operacional (ex: `/dev/urandom` no Linux, ou `CryptGenRandom` no Windows).
2. **Garantia de Critérios:** A lógica garante que, se você pedir uma senha com números, letras e caracteres especiais, a senha gerada **sempre** terá no mínimo um caractere de cada grupo escolhido, evitando senhas fracas por pura probabilidade.
3. **Embaralhamento Seguro:** Após a seleção dos caracteres, utilizamos o `SystemRandom().shuffle()` para embaralhar a senha, garantindo que não haja padrões previsíveis na ordem dos caracteres (como por exemplo, sempre terminar com um número).

---

## 🏗️ Arquitetura do Projeto

O projeto foi construído adotando as melhores práticas do ecossistema Python:

- `src/safe_password_generator/core`: A lógica central e segura do gerador. Totalmente desacoplada da interface.
- `src/safe_password_generator/cli`: Interface rápida de linha de comando baseada no `argparse`.
- `src/safe_password_generator/web`: Interface gráfica interativa construída com Streamlit, utilizando CSS customizado (gradientes, *glassmorphism*).
- `tests/`: Bateria de testes rigorosa construída com `pytest`.

---

## 🚀 Como Instalar e Rodar

### Pré-requisitos
- Python 3.9 ou superior

### 1. Instalação

Primeiro, clone o repositório e crie um ambiente virtual:
```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar no Windows:
venv\Scripts\activate
# Ativar no Linux/Mac:
source venv/bin/activate
```

Instale as dependências (incluindo o próprio pacote no modo editável):
```bash
pip install -r requirements-dev.txt
pip install -e .
```

### 2. Rodando a Interface Web (Recomendado)

Inicie o servidor do Streamlit para visualizar a interface gráfica moderna:
```bash
streamlit run src/safe_password_generator/web/app.py
```
Acesse [http://localhost:8501](http://localhost:8501) no seu navegador.

### 3. Usando a Interface de Linha de Comando (CLI)

Após instalar (`pip install -e .`), um executável global `safe-password-gen` ficará disponível no seu terminal!

**Gerar uma senha com o tamanho padrão (16 caracteres):**
```bash
safe-password-gen
```

**Gerar uma senha de 32 caracteres:**
```bash
safe-password-gen --length 32
```

**Gerar uma senha que inclua APENAS letras (sem números e sem especiais):**
```bash
safe-password-gen --no-numbers --no-specials
```

**Obter ajuda sobre todos os comandos:**
```bash
safe-password-gen --help
```

---

## 🧪 Rodando os Testes Automatizados

O projeto possui 100% de cobertura nos cenários centrais, utilizando a biblioteca `pytest`. Para executá-los, basta rodar na raiz do projeto:

```bash
pytest
```

---

## 📄 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.