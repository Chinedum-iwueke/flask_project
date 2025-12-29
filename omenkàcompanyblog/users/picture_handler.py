import os
from PIL import Image
from flask import current_app

def add_profile_pic(pic_upload, username):
    filename = pic_upload.filename
    ext_type = filename.rsplit('.', 1)[-1].lower()

    storage_filename = f"{username}.{ext_type}"

    upload_folder = os.path.join(
        current_app.root_path,
        'static',
        'profile_pics'
    )

    # Ensure directory exists
    os.makedirs(upload_folder, exist_ok=True)

    filepath = os.path.join(upload_folder, storage_filename)

    output_size = (200, 200)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
