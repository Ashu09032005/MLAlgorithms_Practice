###Put and delete 
###working apis
from flask import Flask, jsonify, request
app = Flask(__name__)
items=[
    {'id': 1, 'name': 'item1', 'description': 'This is item1'},
    {'id': 2, 'name': 'item2', 'description': 'This is item2'},
    
]
###get for items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)
## get a specific id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404
    ## post
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    items.append(new_item)
    return jsonify(new_item), 201
if __name__ == '__main__':
    app.run(debug=True)