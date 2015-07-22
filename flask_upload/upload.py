# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
'''
refs: 
http://code.runnable.com/UiPcaBXaxGNYAAAL/how-to-upload-a-file-to-the-server-in-flask-for-python
http://stackoverflow.com/questions/10961378/how-to-generate-an-html-directory-list-using-python
'''
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from werkzeug.datastructures import FileStorage

curpath = os.path.dirname(os.path.realpath(__file__))

# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = os.path.join(curpath, 'uploaded/')
app.config['DATA_FOLDER'] = os.path.join(curpath, 'data/')
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','json','py'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('app.html', tree=make_tree(app.config['DATA_FOLDER']))
    # return render_template(curpath+'/app.html')


# Route that will process the file upload
# @app.route('/upload', methods=['POST'])
# def upload():
#     # Get the name of the uploaded file
#     file = request.files['file']
#     print type(file)
#     # Check if the file is one of the allowed types/extensions
#     if file and allowed_file(file.filename):
#         # Make the filename safe, remove unsupported chars
#         filename = secure_filename(file.filename)
#         # Move the file form the temporal folder to
#         # the upload folder we setup
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         # Redirect the user to the uploaded_file route, which
#         # will basicaly show on the browser the uploaded file
#         return redirect(url_for('uploaded_file',
#                                 filename=filename))

@app.route('/query')
def upload_file():
    filename = request.args.get('file')
    # Get the name of the uploaded file
    filepath = os.path.join(app.config['DATA_FOLDER'], filename)
    with open(filepath, 'r') as fp:
        file = FileStorage(fp)
        # Check if the file is valid
        if file:
            # Make the filename safe, remove unsupported chars
            filename = secure_filename(file.filename)
            # Move the file form the temporal folder to
            # the upload folder we setup
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Redirect the user to the uploaded_file route, which
            # will basicaly show on the browser the uploaded file
            return redirect(url_for('uploaded_file',
                                    filename=filename))

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploaded/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


def make_tree(path):
    tree = dict(name=os.path.basename(path), children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=name))
    return tree

if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=int("5050"),
        debug=True
    )
