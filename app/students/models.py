from bson import json_util
from app.extensions import mongo


class StudentsModel():

    def get_all_students(self):
        return mongo.db.students.find({}, {"_id": 0})

    def get_student_by_id(self, id):
        return mongo.db.students.find_one_or_404({"_id": id}, {"_id": 0})

    def get_student_by_dni(self, dni):
        return mongo.db.students.find_one_or_404({"dni": dni}, {"_id": 0})

    def get_students_by_name(self, name):
        response = mongo.db.students.find(
            {"name": name.capitalize()},
            {"_id": 0}
        )
        if response.count():
            return json_util.dumps(response)

    def get_students_by_second_name(self, second_name):
        response = mongo.db.students.find({"second_name": second_name.capitalize()}, {"_id": 0})
        if response.count():
            return json_util.dumps(response)


    def get_students_by_lastname(self, lastname):
        response = mongo.db.students.find({"lastname": lastname.capitalize()}, {"_id": 0})
        if response.count():
            return json_util.dumps(response)

    def get_students_by_second_lastname(self, second_lastname):
        response = mongo.db.students.find({"second_lastname": second_lastname.capitalize()}, {"_id": 0})
        if response.count():
            return json_util.dumps(response)

    def get_students_by_name_and_lastname(self, name, lastname):
        response = mongo.db.students.find({"name": name.capitalize(), "lastname": lastname.capitalize()}, {"_id": 0})
        if response.count():
            return json_util.dumps(response)

    def get_students_by_career(self, career):
        response = mongo.db.students.find({"career_name": career}, {"_id": 0})
        if response.count():
            return json_util.dumps(response)

    def get_students_by_expression(self, expression):
        return mongo.db.students.find(
            {"$text": {"$search": expression}},
            {"accuracy": {"$meta": "textScore"}}
        ).sort([("accuracy", {"$meta": "textScore"})])

    def insert_one_student(self, document):
        return mongo.db.students.insert_one(document).inserted_id

    def insert_students(self, documents):
        result = mongo.db.students.insert_many(documents)
        return [{"__id": str(id)} for id in list(result.inserted_ids)]

    def update_student_by_dni(self, document):
        return mongo.db.students.update_one({"dni": document["dni"]}, {"$set": document}).modified_count

    def delete_student_by_dni(self, dni):
        result = self.get_student_by_dni(dni)
        mongo.db.students.delete_one({"dni": dni})
        return result
