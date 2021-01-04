from flask_restx import reqparse
import werkzeug

item_parser = reqparse.RequestParser()
item_parser.add_argument(
    'label', required=True, location='form'
)
item_parser.add_argument(
    'description', required=True, location='form'
)
item_parser.add_argument(
    'image', type=werkzeug.datastructures.FileStorage, required=False,
    location='files'
)
item_parser.add_argument(
    'box_x', type=int, required=True, location='form',
    help='Bounding box: Axis x'
)
item_parser.add_argument(
    'box_y', type=int, required=True, location='form',
    help='Bounding box: Axis y'
)
item_parser.add_argument(
    'box_w', type=int, required=True, location='form',
    help='Bounding box: Width'
)
item_parser.add_argument(
    'box_h', type=int, required=True, location='form',
    help='Bounding box: Height'
)

# FOR PAGINATION
pagination_parser = reqparse.RequestParser()
pagination_parser.add_argument(
    'page_num', type=int, required=False, default=1, help='Page number'
)
pagination_parser.add_argument(
    'page_size', type=int, required=False, default=5, help='Page size'
)

# FOR BULK INSERT
bulk_items_parser = reqparse.RequestParser()
bulk_items_parser.add_argument(
    'items', required=True, location='form'
)
bulk_items_parser.add_argument(
    'image_str', required=True, location='form'
)
bulk_items_parser.add_argument(
    'source_origin', required=True, location='form'
)
