from flask import request, Response, jsonify
from flask_restx import Namespace, Resource

import json

from feedback.parsers import pagination_parser, item_parser, bulk_items_parser
from feedback.dto import ItemDto
from feedback.models import Item, USERS
from feedback.utils import (
    is_allowed_file, handle_upload_file, get_paginated_list, handle_save_image
)

api = Namespace('feedback', description='Object detector feedback')


@api.route('/items')
class ItemList(Resource):
    @api.doc('list_items')
    @api.expect(pagination_parser)
    # @api.marshal_list_with(item_fields)
    def get(self):
        """List all items"""
        p_args = pagination_parser.parse_args()
        paginator = Item.objects().paginate(
            page=p_args.get('page_num'), per_page=p_args.get('page_size')
        )

        return jsonify(get_paginated_list(paginator, request.path))

    @api.doc('create item')
    @api.expect(item_parser)
    # @api.marshal_with(id, code=201)
    def post(self):
        """Create new item"""
        args = item_parser.parse_args()
        image = args.pop('image', None)
        args['image'] = handle_upload_file(image)

        item_data = ItemDto(**args).__dict__()
        item_data['created_by'] = 'other'  # Anonymous User
        item = Item(**item_data).save()
        item_id = item.id
        return {'id': str(item_id)}, 201


@api.route('/items/<string:item_id>')
class ItemList(Resource):
    @api.doc(description="Get an item info")
    # @api.marshal_with(item_fields)
    def get(self, item_id):
        """Retrieve item"""
        item = Item.objects.get_or_404(id=item_id).to_json()
        return Response(item, mimetype='application/json', status=200)

    @api.doc(responses={204: "Feedback Item deleted"})
    def delete(self, item_id):
        """Remove an item"""
        Item.objects.get_or_404(id=item_id).delete()
        return '', 204

    @api.expect(item_parser)
    def put(self, item_id):
        """Update a given item"""
        args = item_parser.parse_args()
        image = args.pop('image', None)
        args['image'] = handle_upload_file(image)

        item_data = ItemDto(**args).__dict__()
        item_data['modified_by'] = 'other'  # Anonymous User

        Item.objects.get_or_404(id=item_id).update(**item_data)
        item = Item.objects.get_or_404(id=item_id).to_json()
        return Response(item, mimetype='application/json', status=200)


@api.route('/bulk_items')
class ItemList(Resource):
    @api.expect(bulk_items_parser)
    def post(self):
        """insert data"""
        args = bulk_items_parser.parse_args()
        image_str = args.pop('image_str', '')
        source_origin = args.pop('source_origin', '')

        items_str = args.pop('items', '[]')
        items = json.loads(items_str)
        dto_items = []
        if items:
            image_name = handle_save_image(image_str, source_origin)
            for item in items:
                item['image'] = image_name
                item_data = ItemDto(**item).__dict__()
                created_by = item.pop('created_by', None)
                item_data['created_by'] = created_by if \
                    created_by else USERS['auto']
                modified_by = item.pop('modified_by', None)
                item_data['modified_by'] = modified_by if \
                    modified_by else None

                dto_items.append(Item(**item_data))

            Item.objects.insert(dto_items)

        return {'total': len(items)}, 201
