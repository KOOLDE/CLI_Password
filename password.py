import click
from random import choices

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%[]{}()"

concatenate_string = (upper_case + lower_case + numbers + symbols)

@click.command()
@click.option('--length', default=8, help='Set password length.')
def main(length):
    filter_character = choices(concatenate_string, k=length)
    convert_list_into_string = "".join(filter_character)
    
    click.echo(convert_list_into_string)

if __name__ == "__main__":
    main()