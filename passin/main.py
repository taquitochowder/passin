import click
from .functions import password, gen_secretkey

@click.group()
def main():
    pass

@main.command()
def start():
    click.echo('Command working!')

@main.command()
def get():
    click.echo('Command working!')

@main.command()
def reset():
    click.echo('Command working!')

if __name__ == "__main__":
    main()