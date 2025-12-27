from flask import redirect, url_for

def upload_file(filename):
    return redirect(url_for('static', filename= f'uploads/{filename}'))