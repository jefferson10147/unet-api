from app.extensions import mongo


class StudentsModel():

    def get_all_students(self):
        students = mongo.db.students.find({}, {"_id": 0})
        return students
