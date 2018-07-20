from __future__ import print_function
import time
from flask import Flask, Markup, request, render_template, json
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:123@localhost/test')
DBSession = sessionmaker(bind=engine)
session = DBSession()

class User(Base):
    __tablename__ = 't1'
    user_name = Column(String(16), primary_key=True)
    pwd = Column(String(16))


@app.route('/')
def index_page():
    return 'index page'

@app.route('/hello<name>')
def hello_world(name):
    return Markup('<strong>Hello!</strong>') + name

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_request', methods=['GET'])
def login_request():
    # engine = create_engine('mysql+mysqlconnector://root:123@localhost/test')
    # DBSession = sessionmaker(bind=engine)
    # session = DBSession()
    try:
	    user = session.query(User).filter(User.user_name==request.args.get('username')).one()
    except:
        print('user_name error')
        # session.close()
        return json.dumps({'html':'<span>user_name error!</span>'})
    # session.close()
    if user.pwd==request.args.get('password'):
        print('login!')
        return {User.username:'login!'}
        #return json.dumps({'html':'<span>login!</span>'})
    else:
        print('pwd error')
        return json.dumps({'html':'<span>password error!</span>'})

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup_request', methods=['POST'])
def signup_request():
    pwd = request.form['password']
    print(pwd)
    if request.form['password2'] != pwd:
        print('pwd not equal')
        return 'pwd not equal'
    # engine = create_engine('mysql+mysqlconnector://root:123@localhost/test')
    # DBSession = sessionmaker(bind=engine)
    # session = DBSession()
    if session.query(User).filter(User.user_name==request.form['username']).count() > 0:
        # session.close()
        return 'username exist'
    new_user = User(user_name=request.form['username'], pwd=pwd)
    session.add(new_user)
    session.commit()
    # session.close()
    #return render_template('login.html')
    return request.form['username']+'signup success'

@app.route('/newpwd')
def newpwd():
    return render_template('newpwd.html')

@app.route('/newpwd_request', methods=['PUT'])
def newpwd_request():
    print('enter newpwd_request')
    pwd = request.form['password']
    if request.form['password2'] != pwd:
        print('pwd not equal')
        return 'pwd not equal'
    # engine = create_engine('mysql+mysqlconnector://root:123@localhost/test')
    # DBSession = sessionmaker(bind=engine)
    # session = DBSession()
    if session.query(User).filter(User.user_name==request.form['username']).update({'pwd':pwd})==0:
        print('username not exist')
        return 'username not exist'
    else:
        session.commit()
        # session.close()
        #return render_template('login.html')
        return request.form['username']+'change password success'

@app.route('/delete_request', methods=['DELETE'])
def delete_request():
    print('enter delete_request')
    pwd = request.form['password']
    print(request.form)
    # engine = create_engine('mysql+mysqlconnector://root:123@localhost/test')
    # DBSession = sessionmaker(bind=engine)
    # session = DBSession()
    try:
        user = session.query(User).filter(User.user_name==request.form['username']).one()
        if user.pwd != pwd:
            print('pwd error')
            return 'pwd error'
        session.query(User).filter(User.user_name==request.form['username']).delete()
        session.commit()
        # session.close()
        print('done')
        #return render_template('login.html')
        return request.form['username']+'delete account success'
    except:
        print('username not exist')
        return 'username not exist'

@app.route('/all', methods=['GET'])
def get_all():
    l=[]
    for row in session.query(User).all():
        l.append(row.user_name + ':' + row.pwd)
    return '<br>'.join(l)


if __name__ == "__main__":
    app.run(port=5002)