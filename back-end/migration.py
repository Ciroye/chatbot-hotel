import db

if __name__ == '__main__':
    print("Migration Start")
    db.Base.metadata.create_all(db.engine, checkfirst=False)