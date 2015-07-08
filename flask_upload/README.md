# List files under a folder and upload them to flask server  
___
- 1. put the files you want to upload to server in the subfolder data/
- 2. run upload.py in the cmd line, then open http://127.0.0.1:5050/
- 3. click the file you want to upload, then it will be saved to uploaded/ subfolder under current folder.
- 4. afte clicking, it shows the content of the uploaded file.

by modifying:
- app.config['UPLOAD_FOLDER'] = os.path.join(curpath, 'uploaded/')
- app.config['DATA_FOLDER'] = os.path.join(curpath, 'data/')

You can upload files from any accessible URL to any.