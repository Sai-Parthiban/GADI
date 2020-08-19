'''
Created on Sep 18, 2019

@author: Sai
'''
from flask import Flask,render_template

app = Flask(__name__)
 
@app.route('/')
@app.route('/home')
def home():   
    return render_template('home.html')

@app.route('/help')
def help():   
    return render_template('help.html')

@app.route('/login')
def login():   
    return render_template('login.html')

@app.route('/register')
def register():   
    return render_template('register.html')

@app.route('/about')
def about():   
    return render_template('about.html')

@app.route('/contact')
def contact():   
    return render_template('contact.html')

@app.route('/home/fuelprize')
def fuelprize():   
    return render_template('fuelprize.html')

if __name__ == '__main__':
    app.run()
    
