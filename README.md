# CLI Password
Gerar senha com script python usando a biblioteca click.

## Requerimentos
Este projeto faz uso de um módulo do python chamado click.
```bash
# Instalação
pip install -r .\requirements.txt
```
ou usar Makefile Tools do VsCode.

## Como utilizar

```bash
# Clone este repositório
git clone https://github.com/doniztjnr/cli-password.git

# Acesse a pasta do projeto onde contem o arquivo password.py
cd .\cli-password\sample\

# Rodar o script via prompt de comando
python .\password.py
```

## Opções
Por padrão é gerado uma senha de 8 dígitos, porém você pode especificar a quantidade de dígitos que desejar.
```bash
# Em <number> você pode colocar qualquer número
python .\password.py --length <number>

# Exemplo 
python .\password.py --length 12
```

## Ajuda
Para saber como usar o script digite o comando.
```bash
# Como utilizar a cli
python .\password.py --help
```