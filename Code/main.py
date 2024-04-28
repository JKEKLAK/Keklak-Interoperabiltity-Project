# Import Dependencies
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# define application and database variables
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app_version = "v1/"


# create the data definition
class CatModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    image_url = db.Column(db.String(100), nullable=False)
    youtube = db.Column(db.String(100), nullable=True)
    facts = db.Column(db.String(100), nullable=True)

    # outputs to log/screen to verify data visually
    def __repr__(self):
        return f"Cat(name = {name}, image_url = {image_url}, youtube = {youtube}, facts={facts})"


# run this statement the first thme to create the database structure
#db.create_all()

# handle the incoming data request with a parser
# arguments for a put request
cat_put_args = reqparse.RequestParser()
cat_put_args.add_argument("name", type=str, help="name of cat is required", required=False)
cat_put_args.add_argument("image_url", type=str, help="image url of cat", required=True)
cat_put_args.add_argument("youtube", type=str, help="youtube videos about cat", required=False)
cat_put_args.add_argument("facts", type=str, help="cat facts go here", required=False)

# arguments for an update request
cat_update_args = reqparse.RequestParser()
cat_update_args.add_argument("name", type=str, help="name of cat is required")
cat_update_args.add_argument("image_url", type=str, help="image url of cat")
cat_update_args.add_argument("youtube", type=str, help="youtube videos about cat")
cat_update_args.add_argument("facts", type=str, help="cat facts go here")

# Map the types to columns extracted from the database object
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'image_url': fields.String,
    'youtube': fields.String,
    'facts': fields.String
}


# Set up the Resource Functions for CRUD
class Cat(Resource):
    # GET (READ in CRUD)
    # @marshal_with serializes output from the DB as a dictionary (json object)
    # so we can work with it in python
    @marshal_with(resource_fields)
    def get(self, cat_id):
        result = CatModel.query.filter_by(id=cat_id).first()
        if not result:
            abort(404, message="Could not find cat with that id")
        return result

    # POST (CREATE in CRUD)
    @marshal_with(resource_fields)
    def put(self, cat_id):
        args = cat_put_args.parse_args()
        result = CatModel.query.filter_by(id=cat_id).first()
        if result:
            abort(409, message="Cat id taken...")

        cat = CatModel(id=cat_id, name=args['name'], image_url=args['image_url'], youtube=args['youtube'], facts=args['facts'])
        db.session.add(cat)
        db.session.commit()
        return cat, 201

    # PUT (UPDATE in CRUD)
    @marshal_with(resource_fields)
    def patch(self, cat_id):
        args = cat_update_args.parse_args()
        result = CatModel.query.filter_by(id=cat_id).first()
        if not result:
            abort(404, message="Cat doesn't exist, cannot update")

        if args['name']:
            result.name = args['name']
        if args['image_url']:
            result.image_url = args['image_url']
        if args['youtube']:
            result.youtube = args['youtube']
        if args['facts']:
            result.facts = args['facts']

        db.session.commit()

        return result, 200

    # DELETE (DELETE in CRUD)
    def delete(self, cat_id):
        abort_if_cat_id_doesnt_exist(cat_id)
        del cat[cat_id]
        return '', 204


# Register the Resource called cat to the API
api.add_resource(Cat, "/" + app_version + "cat/<int:cat_id>")

# Run the API body
if __name__ == "__main__":
    app.run(debug=True)
