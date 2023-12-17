import click
from click import echo

from db import sqlCon
from db.mongo import mongoMigrate


@click.command()
@click.version_option("1.0.0")
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
def hello(verbose):
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello World")


@click.command("showDBsqlite")
def showdbsqlite():
    sqlCon.tabulate(headers=["ID", "Name", "Age"], tablefmt="grid", tabular_data=sqlCon.data)


@click.command("migrateDB")
def migratedb():
    mongoMigrate.migrate_data()
    echo("Data has been migrated.")


@click.group()
def main():
    pass


main.add_command(hello)
main.add_command(showdbsqlite)
main.add_command(migratedb)

if __name__ == "__main__":
    main()
