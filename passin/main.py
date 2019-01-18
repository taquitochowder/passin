import click
from .functions import password, gen_secretkey


@click.group()
def main():
    """A command line tool for generating and managing passwords
    at the exact same time."""
    pass


@main.command('setup', short_help='setup secret key')
@click.option('--use-existing', is_flag=True, help='User can input their own secret key.')
def setup(use_existing):

    click.echo('Command working!')
    if use_existing:
        click.echo("Option working!")


@main.command('get', short_help='get password for service')
@click.argument('service', metavar='<service>')
def get(service):
    click.echo('Command working!')
    click.echo(service)


@main.command('reset', short_help='reset all passwords')
def reset():
    click.echo('Command working!')


if __name__ == "__main__":
    main()
