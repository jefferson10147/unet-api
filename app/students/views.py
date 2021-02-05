from flask import Blueprint


students_blueprint = Blueprint(
    name="students",
    import_name=__name__,
    url_prefix="/api/students"
)


@students_blueprint.route('/')
def student_hi():
    return "here you can get all students"