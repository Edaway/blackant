from flask import Blueprint

vacancies_bp = Blueprint('vacancies', __name__)

@vacancies_bp.route('/vacancies')
def vacancies_list():
    return "Список вакансий"
