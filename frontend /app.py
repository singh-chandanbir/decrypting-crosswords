##### .......................................... Importing Libraries .............................................#####
from flask import Flask, render_template as rt
from os import getenv
from flask_mail import Mail

##### .......................................... Flask App .............................................#####
app=Flask(__name__)
app.config['SECRET_KEY'] = getenv("SECRET_KEY")


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
    return rt('contact-us.html')

@app.route('/about-us')
def about_us():
    return rt('about-us.html')


#####.......................................... Errors Pages  .............................................#####
@app.errorhandler(404)
def badlink(e):
    return rt('pagenotfound.html') , 404



##### .......................................... Importing Routes .............................................#####
from users import routes
from crosswords import routes




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0' ,port=8080)