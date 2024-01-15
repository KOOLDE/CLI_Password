from random import choices

import click
from helper import is_numeric


@click.command
@click.option(
    "--length",
    default=8,
    prompt="length",
    help="Quantidade de caracteres.",
)
def password(length: str) -> None:
    if is_numeric(length):
        upper_case: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_case: str = "abcdefghijklmnopqrstuvwxyz"
        numbers: str = "0123456789"
        symbols: str = "!@#$%[]{}()"

        concatenate_string: str = upper_case + lower_case + numbers + symbols
        filter_character: list = choices(concatenate_string, k=int(length))
        convert_list_into_string: str = "".join(filter_character)

        click.echo(convert_list_into_string)


def main() -> None:
    password()


if __name__ == "__main__":
    main()
