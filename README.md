# Projeto de ETL

Seguindo Workshop 01 - 2023

## Objetivo do Projeto

Realizar uma ETL onde recebe diversos arquivos em formato excel e concatenam ele em um único arquivo, utilizando melhores práticas de padrões de código, com black e isort, como também melhores práticas de pre-commit, documentação, teste e CI.
Projeto bem completo para aplicações em diversas outras situações.

## Stack Utilizada

- Python
- Pyenv
- Poetry
- Pandas
- Pytest
- Black
- Isort
- Pre-Commit
- MkDocs
- Pip-Audit
- Pydocstyle
- Taskipy
  

## Configuração do Computador Utilizado

- Processador: AMD Ryzen 3 5300U with Radeon Graphics 2.6 Ghz
- RAM: 8 GB DDR-4
- SSD Sata: 256 GB
- SO: Windows 11 23H2

## Clonando o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/luhborba/ProjetoDeETL.git
cd ProjetoDeETL
```

2. Configure a versão correta do Python com `pyenv`
```bash
pyenv install 3.11.7
pyenv local 3.11.7
```

3. Ativando Poetry
```bash
poetry env use 3.11.7
poetry shell
```

4. Insatalando dependências
```bash
poetry install
```

5. Rodando ETL
```bash
task run
```

6. Rodando Testes
```bash
task test
```

7. Rodando Documentação
```bash
task docs
```
