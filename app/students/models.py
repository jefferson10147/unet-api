from app.extensions import mongo


class StudentsModel():

    def get_all_students(self):
        return mongo.db.students.find({}, {"_id": 0})

    def get_student_by_id(self, id):
        return mongo.db.students.find_one({"_id": id}, {"_id": 0})

    def get_student_by_dni(self, dni):
        return mongo.db.students.find({"dni": dni}, {"_id": 0})

    def get_students_by_name(self, name):
        return mongo.db.students.find({"name": name.capitalize()})

    def get_students_by_second_name(self, second_name):
        return mongo.db.students.find({"second_name": second_name.capitalize()}, {"_id": 0})

    def get_students_by_lastname(self, lastname):
        return mongo.db.students.find({"lastname": lastname.capitalize()}, {"_id": 0})

    def get_students_by_second_lastname(self, second_lastname):
        return mongo.db.students.find({"second_lastname": second_lastname.capitalize()}, {"_id": 0})

    def get_students_by_career(self, career):
        return mongo.db.students.find({"career_name": career}, {"_id": 0})

    def get_students_by_expression(self, expression):
        return mongo.db.students.find(
            {"$text": {"$search": expression}},
            {"accuracy": {"$meta": "textScore"}},
        ).sort([("accuracy", {"$meta": "textScore"})])
