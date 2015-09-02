import os
from flask.ext.script import Manager
from hired import app, db, models
from flask.ext.migrate import Migrate, MigrateCommand
import datetime

manager = Manager(app)
app.config.from_object('config.doingitlive')

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def createdb():
    '''Runs the db init, db migrate, db upgrade commands automatically'''
    os.system('python manage.py db init')
    os.system('python manage.py db migrate')
    os.system('python manage.py db upgrade')
    newRule = models.Rules(
        rule='alert tcp any any -> any 80 (msg:"WEB-MISC phf attempt"; flags:A+; content:"/cgi-bin/phf"; priority:10;)')
    db.session.add(newRule)
    newRule = models.Rules(
        rule='alert tcp any any -> any 80 (msg:"EXPLOIT ntpdx overflow"; dsize:>128; classtype:attempted-admin; priority:10 );')
    db.session.add(newRule)
    db.session.commit()


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, models=models)


if __name__ == "__main__":
    manager.run()
