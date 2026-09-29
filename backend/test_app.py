import traceback
from app import create_app
from app.extensions import db

try:
    print("Testing app creation")
    app = create_app()
    print("App created")
    with app.app_context():
        print("Creating DB tables")
        db.create_all()
        print("DB tables created")
    print("SUCCESS")
except Exception as e:
    with open("test_errors.txt", "w", encoding="utf-8") as f:
        f.write(traceback.format_exc())
