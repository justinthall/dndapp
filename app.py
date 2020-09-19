from flask import *
from datetime import timedelta
from forms import CommandForm, LoginForm, NewCharacter, newBattle
from config import SECRET_KEY
from flask_socketio import SocketIO, send, join_room, emit, rooms
from character import process_character
import commander
from secrets import token_hex
from time import sleep
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.permanent_session_lifetime = timedelta(weeks=12)
socketio = SocketIO(app)

battlelist = []


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
    return render_template('characters.html', form=form)


@app.route('/battles', methods=['GET', 'POST'])
def battleList():
    form = newBattle()
    if form.validate_on_submit():
        return redirect('/battles/{}'.format(request.form['battle'] + '_' + token_hex(4)))
    return render_template('battlemaster.html', form=form, battlelist=battlelist)


@app.route('/battles/<battle>', methods=['GET', 'POST'])
def battle(battle):
    battlename = battle.split("_")[0]
    battleid = battle
    room = battle
    try:
        return render_template('battle.html', battle=battlename, battleid=battleid, nickname=session['nickname'], room=room)
    except(KeyError):
        flash("You must set a nickname before continuing!", 'error')
        return redirect('/login')


@app.route('/test')
def testtest():
    test()
    return render_template('base.html')


@socketio.on('message')
def handleMessage(msg):
    headers = {}
    try:
        headers.update({'characters': session['characters']})
    except:
        headers = {'characters': "null"}
    headers.update({'datetime': str(datetime.utcnow())})
    headers.update({'nickname': session['nickname']})
    if msg['msg'][0] == "/":
        result = commander.parseCommand(msg['msg'], msg['room'], headers)
        emit("message", result, room=msg['room'])
    else:
        emit("message", msg['msg'], room=msg['room'])


@socketio.on('connect')
def connect():
    pass


@socketio.on('disconnect')
def disc():
    pass


@socketio.on('join')
def on_join(data):
    name = data['nickname']
    join_room(data['room'])
    emit('joinRoomAnnouncement', name, room=data['room'])
    if ['battle'] not in battlelist:
        battlelist.append(data['battle'])


@socketio.on('leave')
def on_leave():
    print('yes!!!!!!!!!!!!!!!!!!!!!')


if __name__ == '__main__':
    socketio.run(app, debug=True)
