from flask import current_app, jsonify
from flask_mongoengine.pagination import Pagination


def is_allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in \
           current_app.config['ALLOWED_EXTENSIONS']


def handle_upload_file(uploaded_file):
    import os
    import uuid

    if not uploaded_file or not is_allowed_file(uploaded_file.filename):
        return None

    filename = uploaded_file.filename

    ext = filename.rsplit('.', 1)[1].lower()
    new_name = f'{uuid.uuid4().hex}.{ext}'
    new_path = os.path.join(current_app.config['UPLOAD_FOLDER'], new_name)

    uploaded_file.save(new_path)

    return dict(name=new_name, source_origin=filename)


def handle_save_image(image_string, source_origin):
    import os
    import base64
    import uuid

    new_name = f'{uuid.uuid4().hex}.png'
    filename = os.path.join(current_app.config['UPLOAD_FOLDER'], new_name)
    img_data = base64.b64decode(image_string.encode('ascii'))
    handler = open(filename, "wb+")
    handler.write(img_data)
    handler.close()

    return dict(name=new_name, source_origin=source_origin)


def get_paginated_list(data: Pagination, url):
    obj = {
        'count': data.total,
        'next': None,
        'previous': None,
        'results': data.items
    }
    if data.has_prev:
        obj['previous'] = f'{url}?page_num={data.prev_num}' \
                          f'&page_size={data.per_page}'
    if data.has_next:
        obj['next'] = f'{url}?page_num={data.next_num}' \
                      f'&page_size={data.per_page}'

    return obj
