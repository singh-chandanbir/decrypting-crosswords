##### .......................................... Importing Libraries .............................................#####
from flask import Flask, render_template as rt
from os import getenv
from flask_mail import Mail
from flask_socketio import SocketIO



##### .......................................... Flask App .............................................#####
app=Flask(__name__)
app.config['SECRET_KEY'] = getenv("SECRET_KEY")
socketio = SocketIO(app)


@socketio.on('time')
def handle_connect(time):
    client_sid = request.sid
    print(time)
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


@app.route('/test' , methods=['GET', 'POST'])
def test():
    print(request.method)
    print(current_user.email)
    if request.method == 'POST':
        print(request.form)


    return rt('test.html')

#####.......................................... Errors Pages  .............................................#####
@app.errorhandler(404)
def badlink(e):
    return rt('pagenotfound.html') , 404



##### .......................................... Importing Routes .............................................#####
from users.routes import *
from crosswords.routes import *




if __name__ == '__main__':
    socketio.run(app ,debug=True)



def evaluate(self, solution):
        # print puzzle accuracy results given a generated solution
        letters_correct = 0
        letters_total = 0
        for i in range(len(self.crossword.letter_grid)):
            for j in range(len(self.crossword.letter_grid[0])):
                if self.crossword.letter_grid[i][j] != "":
                    letters_correct += (self.crossword.letter_grid[i][j] == solution[i][j])
                    letters_total += 1
        words_correct = 0
        words_total = 0
        for var in self.crossword.variables:
            cells = self.crossword.variables[var]["cells"]
            matching_cells = [self.crossword.letter_grid[cell[0]][cell[1]] == solution[cell[0]][cell[1]] for cell in cells]
            if len(cells) == sum(matching_cells):
                words_correct += 1
            else:
                print('evaluation: correct word', ''.join([self.crossword.letter_grid[cell[0]][cell[1]] for cell in cells]), 'our prediction:', ''.join([solution[cell[0]][cell[1]] for cell in cells]))
            words_total += 1
        print("Letters Correct: {}/{} | Words Correct: {}/{}".format(int(letters_correct), int(letters_total), int(words_correct), int(words_total)))
        print("Letters Correct: {}% | Words Correct: {}%".format(float(letters_correct/letters_total*100), float(words_correct/words_total*100)))