from app import app, database

with app.app_context():
    database.create_all()
    database.session.commit()

if __name__ == "__main__":
    app.run()
