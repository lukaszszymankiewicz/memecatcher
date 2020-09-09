import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

import settings
from app.app import app, db

app.config.from_object(os.environ.get("APP_CONFIG"))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()