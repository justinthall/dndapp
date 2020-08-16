from flask import *
from datetime import timedelta
from forms import CommandForm,LoginForm, NewCharacter
from config import SECRET_KEY
from character import process_character
app=Flask(__name__)
app.config['SECRET_KEY']= SECRET_KEY
app.permanent_session_lifetime= timedelta(weeks=12)

test='test'
@app.route('/',methods=['GET','POST'])
def working():
    form=CommandForm()
    form1= LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('working.html',form=form,form1= form1)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if request.method == 'POST':
        session['nickname']= request.form['nickname']
        print(session)
        return redirect('/')
    return render_template('login.html',form=form)

@app.route('/characters',methods=['GET','POST'])
def characters():
    form= NewCharacter()
    if form.validate_on_submit():
        result =process_character(request.files['pdf'])
        if type(result)== str:
            flash(result)
        elif type(result)== dict:
            try:
                session['characters'].update({result['charactername']:result})
            except:
                session['characters']={result['charactername']:result}
            session.permanent= True
            print(session)
            pass
    return render_template('characters.html',form=form)


if __name__=='__main__':
    app.run(debug=True)
