import secrets
import os
from PIL import Image


def Pics_to_db(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join('blog/static/images/users_avatars', picture_fn)    
    i = Image.open(form_picture)
    i.save(picture_path)
    return picture_fn