from flask import send_file, Blueprint, render_template, request, flash
from werkzeug.utils import secure_filename
from .static import converterAlg
from PIL import Image
import numpy as np
import os
import io

views = Blueprint('views', __name__)
converter = converterAlg.ImageConverter()
filepath_to_remove = None
result_name = None

@views.route('/', methods=['GET', 'POST'])
def home():
    global result_name, filepath_to_remove
    if filepath_to_remove:
        os.remove(filepath_to_remove) 
        result_name = None
        filepath_to_remove = None
    if request.method == 'POST':
        image = request.files.get('image')
        if image:
            filename = secure_filename(image.filename)
            image = Image.open(io.BytesIO(image.read())).convert('L')
            image_np = np.array(image)
            converter.img = image_np 
            
            converter.Convert(filename)

            result_name = converter.upload_filename

            flash('Image added', category='success')
            

    return render_template("home.html")

@views.route('/download')
def download():
    global result_name, filepath_to_remove
    if result_name:
        path = 'uploads/' + result_name   
        file_to_send = send_file(path, as_attachment=True)
        filepath_to_remove = os.getcwd() + '/website/' + path
        return file_to_send

    return render_template("home.html")