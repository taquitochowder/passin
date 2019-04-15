import click
from . import functions


@click.group()
def main():
    """A command line tool for generating and managing passwords
    at the exact same time."""
    pass


@main.command('setup', short_help='setup secret key')
@click.option(
    '--use-existing',
    is_flag=True,
    help='User can input their own secret key.')
def setup(use_existing):
    """Setups the config file and adds a secret key. A custom secret key can also
    be provided.
    """
    if functions.key_exists():
        click.secho(
            'It looks like already have a secret key. Running this command will RESET it!',
            fg='red')
        click.confirm('Do you want to continue?', abort=True)

    if use_existing:
        user_key = click.prompt(
            "Please enter your secret key",
            confirmation_prompt=True,
            hide_input=True)
        functions.set_secretkey(user_key)
        click.echo('Secret key set!')
    else:
        functions.gen_secretkey()
        click.echo('Secret key set!')


@main.command('get', short_help='get password for servcice')
@click.argument('service', metavar='<service>')
@click.option('--length', default=8, help='length of password (default: 8)')
def get(service, length):
    """Generates a password for a given service. Correct master password is
    required to generate the intended password, and will not be verified.
    """

    master = click.prompt(
        'Enter your master password',
        hide_input=True,
        confirmation_prompt=True)
    click.echo(
        f'Password for {service}: {functions.password(master, service, length)}')


@main.command('reset', short_help='reset all passwords')
def reset():
    """Resets the secret key set in the config file. This is an irreversible action
    and it's recommended to save the secret key elsewhere if the passwords are
    to be saved.
    """

    click.secho('This will permanently remove your secret key!', fg='red')
    click.confirm('Do you want to continue?', abort=True)

    functions.reset_key()


if __name__ == "__main__":
    main()
