from app import database


class Tasks(database.Model):
    __tablename__ = "Tasks"
    id = database.Column(database.Integer, primary_key=True)
    content = database.Column(database.String(200), nullable=True)
    done = database.Column(database.Boolean)
