from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from ..models.vacancy import Vacancy
from ..services.vacancy_record import VacancyRecordService


@view_config(route_name='vacancy', renderer='careers:templates/view_vacancy.mako')
def vacancy_view(requset):
    vacancy_id = int(requset.matchdict.get('id', 1))
    print(vacancy_id)
    entry = VacancyRecordService.by_id(vacancy_id, requset)
    print(entry.title)
    if entry is None:
        return HTTPNotFound
    return {'entry': entry}
