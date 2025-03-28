from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    discount = db.Column(db.Integer)
    active = db.Column(db.Boolean)

@app.route('/')
def index():
    db.create_all()

    # v1 = Vendor(id=1, name = 'Microsoft', discount=0, active=True)
    # db.session.add(v1)
    # db.session.commit()
    # v1 = Vendor(id=2, name='Samsung', discount=5, active=True)
    # db.session.add(v1)
    # db.session.commit()
    # v1 = Vendor(name='Samsung', discount=5, active=True)
    # db.session.add(v1)
    # db.session.commit()

    # vendors = Vendor.query.all()
    vendors = Vendor.query.filter(Vendor.name.like('%sa%')).all()
    ret = ''
    for v in vendors:
        ret += v.name + '<br>'

    return f'Hello<br>{ret}'



if __name__ == '__main__':
    app.run(debug=True)