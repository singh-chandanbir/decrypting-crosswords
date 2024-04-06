##### .......................................... Importing Libraries .............................................#####
# from crosswords.crosswordsolver.crosssolve import cross
from flask import Flask, render_template as rt
from os import getenv
from flask_mail import Mail
from flask_socketio import SocketIO


##### .......................................... Flask App .............................................#####
app=Flask(__name__)
app.config['SECRET_KEY'] = getenv("SECRET_KEY")
socketio = SocketIO(app)

##### .......................................... Mail Configuration .............................................#####
app.config.update(
    MAIL_SERVER = getenv('SMTP_SERVER'),
    MAIL_PORT = getenv('SMTP_PORT'),
    MAIL_USE_SSL = True,
    MAIL_USERNAME = getenv('SMTP_USERNAME'),
    MAIL_PASSWORD = getenv('SMTP_PASSWORD')
)
mail = Mail(app)


##### .......................................... Static Pages .............................................#####

@app.route('/')
def homepage():

    return rt('index.html')

@app.route('/synopsis')
def synopsis():
    return rt('synopsis.html')

@app.route('/contact-us')
def contact_us():
    flash("This form is not working yet")
    return rt('contact-us.html')

@app.route('/about-us')
def about_us():
    return rt('about-us.html')

@app.route('/upload')
def upload():
    return rt('upload.html')


# @app.route('/test' , methods=['GET', 'POST'])
# def test():
#     puzzle_file = './crosswords/crosswordsolver/puzzles/LA_times/20240301.puz'
#     solution = cross(puzzle_file)
#     return 


#####.......................................... Errors Pages  .............................................#####
@app.errorhandler(404)
def badlink(e):
    return rt('pagenotfound.html') , 404



##### .......................................... Importing Routes and Sockets .............................................#####
from users.routes import *
from crosswords.routes import *
import socketIO.sockets as sockets




if __name__ == '__main__':
    socketio.run(app ,debug=True)
