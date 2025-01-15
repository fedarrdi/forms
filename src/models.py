from database import mongo

class Form:
    @staticmethod
    def create_form(data):
        return mongo.db.forms.insert_one(data)

    @staticmethod
    def get_form(form_id):
        return mongo.db.forms.find_one({"_id": form_id})

class Response:
    @staticmethod
    def submit_response(form_id, data):
        return mongo.db.responses.insert_one({"form_id": form_id, "data": data})

    @staticmethod
    def get_responses(form_id):
        return mongo.db.responses.find({"form_id": form_id})

