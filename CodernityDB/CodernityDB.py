import CodernityDB



db = database.Database.connect('/db')

db.create()

for x in range(100):
    print(db.insert(dict(x=x)))

for curr in db.all('id'):
    print(curr)