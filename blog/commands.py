import click
from flask.cli import with_appcontext

from blog.models import User, Post, db

@click.command(name = 'create_tables')
@with_appcontext
def create_tables():
    db.create_all()
    db.session.commit()
