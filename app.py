from flask import Flask
import d20
import statblock
import os
app=Flask(__name__)
@app.route('/')
def helloworld():
    return 'hell world'

@app.route('/help')
def no():
    return str(d20.roll('1d20+5'))

@app.route('/character')
def character():
    a= statblock.statblock('Jason',25,18,[10,10,10,10,10],2)
    return a.data
app.run(debug=True)