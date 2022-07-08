from flask import Flask
from flask_restx import Api, Resource
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
api = Api(app)

upload_parser = api.parser()
upload_parser.add_argument('file', location = 'files', type=FileStorage)

@api.route('/upload')
@api.expect(upload_parser)
class Upload(Resource):
    def post(self):
        args = upload_parser.parse_args()
        file = args.get('file')
        print(file.filename)
        return file.filename + " was uploaded successfully"

if __name__ == '__main__':
    app.run()

# from flask import Flask
# from flask_restx import Api, Resource, reqparse

# app = Flask(__name__)
# api = Api(app)

# parser = reqparse.RequestParser()
# parser.add_argument('name', help='Specify your name')

# @api.route('/hello/')
# class HelloWorld(Resource):
#     @api.doc(parser=parser)
#     def get(self):        
#         args = parser.parse_args()
#         name = args['name']
#         return "Hello " + name
    
# if __name__ == '__main__':
#     app.run()