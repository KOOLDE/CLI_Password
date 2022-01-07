# CLI_Password
##### Generate a password

###### Requerimentos:
Este projeto faz uso de um módulo do python chamado click.
```bash
# Instalação
pip install click
```

###### Como utilizar: 

```bash
# Clone este repositório
git clone <https://github.com/KOOLDE/CLI_Password.git>

# Acesse a pasta do projeto onde contem o arquivo password.py
cd CLI_Password

# Rodar o script via prompt de comando
python password.py 
```

###### Opções:
Por padrão é gerado uma senha de 8 dígitos, porém você pode especificar a quantidade de dígitos que desejar.
```bash
# Em <number> você pode colocar qualquer número
python password.py --length <number>

# Exemplo 
python password.py --length 12
```

###### Ajuda:
Para saber como usar o script digite o comando.
```bash
# Como utilizar a CLI
python password.py --help
```