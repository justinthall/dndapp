from flask import *
from datetime import timedelta
from forms import CommandForm, LoginForm, NewCharacter, newBattle
from config import SECRET_KEY
from flask_socketio import SocketIO, send, join_room, emit
from character import process_character
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.permanent_session_lifetime = timedelta(weeks=12)
socketio = SocketIO(app)

test = 'test'


@app.route('/', methods=['GET', 'POST'])
def working():
    form = CommandForm()
    form1 = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('working.html', form=form, form1=form1)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        session['nickname'] = request.form['nickname']
        print(session)
        return redirect('/')
    return render_template('login.html', form=form)


@app.route('/characters', methods=['GET', 'POST'])
def characters():
    form = NewCharacter()
    if form.validate_on_submit():
        result = process_character(request.files['pdf'])
        if type(result) == str:
            flash(result)
        elif type(result) == dict:
            try:
                session['characters'].update({result['charactername']: result})
            except:
                session['characters'] = {result['charactername']: result}
            session.permanent = True
            print(session)
            pass
    return render_template('characters.html', form=form)


@app.route('/battles', methods=['GET', 'POST'])
def battleList():
    form = newBattle()
    if form.validate_on_submit():
        return redirect('/battles/{}'.format(request.form['battle']))
    return render_template('battlemaster.html', form=form)


@app.route('/battles/<battle>', methods=['GET', 'POST'])
def battle(battle):
    battlename = battle
    return render_template('battle.html', battle=battlename, nickname=session['nickname'], room="fred")


@socketio.on('message')
def handleMessage(msg):
    emit("message", msg)


@socketio.on('connect')
def connect():
    print('here')


@socketio.on('join')
def on_join(data):
    print(data['nickname'], data['room'])
    join_room(data['room'])
    emit('joinRoomAnnouncement', data)


if __name__ == '__main__':
    socketio.run(app, debug=True)
