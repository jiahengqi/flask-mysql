from __future__ import print_function
from flask import Flask
from flask_restful import reqparse, Api, Resource
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
api = Api(app)
Base = declarative_base()

engine = create_engine('mysql+mysqlconnector://root:123@localhost/test')
DBSession = sessionmaker(bind=engine)
session = DBSession()

parser = reqparse.RequestParser()
parser.add_argument('val')

class Row(Base):
    __tablename__ = 't2'
    idx = Column(String(16), primary_key=True)
    val = Column(String(16))


class Work(Resource):
    def get(self, idx):
        try:
            user = session.query(Row).filter(Row.idx==idx).one()
            return {idx: user.val}
        except:
            return {idx: 'not found'}

    def post(self, idx):
        try:
            new_row = Row(idx=idx, val=parser.parse_args()['val'])
            session.add(new_row)
            session.commit()
            return {'idx':'done'}
        except:
            return {'idx':'failed'}

    def delete(self, idx):
        try:
            session.delete(session.query(Row).get(idx))
            session.commit()
            return {idx: 'delete done'}
        except:
            return {idx: 'not found'}

    def put(self, idx):
        val = parser.parse_args()['val']
        session.query(Row).filter(Row.idx==idx).update({'val':val})
        return {idx: val}


class AllData(Resource):
    def get(self):
        d = dict()
        for row in session.query(Row).all():
            d[row.idx] = row.val
        return d


api.add_resource(AllData, '/all')
api.add_resource(Work, '/work/<idx>')

if __name__ == '__main__':
    app.run(debug=True)
