import typer

from implemented import ValidateEmail
from app import db


# Configure ORM
db.generate()

# Create the CLI app
app = typer.Typer()


@app.command()
def validate_email(email: str):
    result = ValidateEmail.validate.run(email=email)
    if result.is_success:
        typer.echo(f'Email {email} is valid')
    else:
        typer.echo(f'Email {email} is invalid')


if __name__ == "__main__":
    app()
