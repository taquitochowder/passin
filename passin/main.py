import click
from .functions import password, gen_secretkey, set_secretkey, key_exists


@click.group()
def main():
    """A command line tool for generating and managing passwords
    at the exact same time."""
    pass


@main.command('setup', short_help='setup secret key')
@click.option('--use-existing', is_flag=True, help='User can input their own secret key.')
def setup(use_existing):
    if key_exists():
        click.echo('It looks like already have a secret key. Running this command will RESET it!')
        click.confirm('Do you want to continue?', abort=True)
    
    if use_existing:
        user_key = click.prompt("Please enter your secret key", confirmation_prompt=True,
        hide_input=True)
        set_secretkey(user_key)
        click.echo('Secret key set!')
    else:
        gen_secretkey()
        click.echo('Secret key set!')


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
