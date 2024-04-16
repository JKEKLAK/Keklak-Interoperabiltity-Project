#Jared Keklak INFO 762 Dr.Walters API Project

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy, FSADeprecationWarning

# define application and database variables
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app_version = "v1/"

#DISABLE THIS WARNING
#FSADeprecationWarning = False

class CatModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    image_url = db.Column(db.String, nullable = False)
    facts = db.Column(db.String, nullable = False) #make this array or list .. ?

    def __repr__(self):
        return f"Cat(name = {name}, image_url = {image_url}, facts = {facts})"

#run this statement the first thme to create the database structure
#db.create_all()

cat_put_args = reqparse.RequestParser()
cat_put_args.add_argument("name", type=str, help="Name of Cat required", required=True)
cat_put_args.add_argument("image_url", type=str, help="image url of cat", required=True)
cat_put_args.add_argument("facts", type=list, help="list of cat facts", required=False)

cat_update_args = reqparse.RequestParser()
cat_update_args.add_argument("name", type=str, help="Name of Cat required")
cat_update_args.add_argument("image_url", type=str, help="image url of cat")
cat_update_args.add_argument("facts", type=list, help="list of cat facts")


# in_memory_datastore = {
#     "siamese": {"name": "siamese", "image url": "siamese.jpg"},
#     "russian blue": {"name": "russian blue", "image url": "russianblue.jpg"},
#     "callico": {"name": "callico", "image url": "callico.jpg"}
# }
#
#
# @app.get('/cat_data_base')
# def list_programming_languages():
#     return {"cat_data_base": list(in_memory_datastore.values())}

# Map the types to columns extracted from the database object
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'image_url': fields.String,
    'facts': fields.List
}

# Set up the Resource Functions for CRUD
class Cat(Resource):

    # GET (READ in CRUD)
    # @marshal_with serializes output from the DB as a dictionary (json object) so we can work with it in python
    @marshal_with(resource_fields)
    def get(self, cat_id):
        result = CatModel.query.filter_by(id=cat_id).first()
        if not result:
            abort(404, message="could not find cat with that id")
        return result

    # POST (CREATE in CRUD)
    @marshal_with(resource_fields)
    def put(self, cat_id):
        args = cat_put_args.parse_args()
        result = CatModel.query.filter_by(id=cat_id).first()
        if result:
            abort(409, message="cat id taken...")

        cat = CatModel(id=cat_id, name=args['name'], image_url=args['image_url'], facts=args['facts'])
        db.session.add(cat)
        db.session.commit()
        return cat, 201

    # PUT (UPDATE in CRUD)
    @marshal_with(resource_fields)
    def patch(self, cat_id):
        args = cat_update_args.parse_args()
        result = CatModel.query.filter_by(id=cat_id).first()
        if not result:
            abort(404, message="cat doesn't exist, cannot update")

        if args['name']:
            result.name = args['name']
        if args['image_url']:
            result.image_url = args['image_url']
#        if args['facts']:
#            result.likes = args['likes'] i dont want ppl searching by cat facts

        db.session.commit()

        return result, 200

    # DELETE (DELETE in CRUD)
    def delete(self, cat_id):
        #abort_if_cat_id_doesnt_exist(cat_id) purpose of this line ?
        del CatModel[cat_id]
        return '', 204

# Register the Resource called cat to the API (remember to change versions when making changes for submission)
api.add_resource(Cat, "/" + app_version + "cat/<int:cat_id>")



# Run the API body
if __name__ == "__main__":
    app.run(debug=True)