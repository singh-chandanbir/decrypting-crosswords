from app import app
from flask import render_template as rt, request , session
from flask_login import login_required
from crosswords.modal import puzzle_data, blocked_cells, open_cells

     

##### .......................................... Crossword Routes  .............................................#####



@app.route('/veiw_crosswords/<int:page_number>' )
@login_required
def veiw_crossword(page_number):

    all_objects =[]
    for i in range (10746 ,16746):
        all_objects.append(i)
    start_index = (page_number - 1) * 9
    end_index = start_index + 9
    objects_to_display = all_objects[start_index:end_index]

    total_objects = len(all_objects)
    objects_per_page = 9
    total_pages, remainder = divmod(total_objects, objects_per_page)
    if remainder > 0:
        total_pages += 1
        
    return rt('veiw-crossword.html', objects=objects_to_display, page_number=page_number , total_pages =total_pages )




@app.route('/crossword', methods = ["POST"])
def crossword():
    if (request.method == "POST"):
        crosswordid = int(request.form.get("crossword-id"))
        session["crossword_id"] = crosswordid
        clue_data=puzzle_data(crosswordid)
        blocked_cell_list , inputId_clueId = blocked_cells(clue_data)
        list_open_cells , x = open_cells(clue_data)

            


    return rt('crossword.html', blocked_cell_list = blocked_cell_list, clue_data=clue_data , list_open_cells=list_open_cells )



# @app.route('/upload', methods=['GET','POST'])
# def upload_file():
#     print(request.method) 
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return jsonify({'error': 'No file part'})
#         file = request.files['file']
#         if file.filename == '':
#             return jsonify({'error': 'No selected file'})
#     # Process the file (save it, manipulate it, etc.)
#     # Example: file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
#         return jsonify({'success': True})
#     return rt('upload.html')


from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
import os
from crosswords.crosswordsolver.crosssolve import cross

UPLOAD_FOLDER = 'crosswords/crosswordsolver/uploaded_puzzles'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class PuzzForm(FlaskForm):
    puzz = FileField(validators=[FileRequired()])
    submit = SubmitField("uplaod File")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = PuzzForm()

    if form.validate_on_submit():
        f = form.puzz.data
        print(f)
        if f:
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        else:
            return 'Nofile selected'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        solution = cross(file_path)
        print(solution)
        return solution
    return rt('upload.html', form=form)
