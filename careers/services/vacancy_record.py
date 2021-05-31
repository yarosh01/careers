import sqlalchemy as sa
from paginate_sqlalchemy import SqlalchemyOrmPage
from ..models.vacancy import Vacancy


class VacancyRecordService(object):
    @classmethod
    def all(cls, _id, request):
        query = request.dbsession.query(Vacancy)
        return query.order_by(sa.desc(Vacancy.id))

    @classmethod
    def by_id(cls, _id, request):
        query = request.dbsession.query(Vacancy)
        return query.get(_id)

    @classmethod
    def get_paginator(cls, request, page=1):
        query = request.dbsession.query(Vacancy)
        query = query.order_by(sa.desc(Vacancy.id))
        query_params = query.GET.mixed()

        def url_maker(link_page):
            query_params['page'] = link_page
            return request.current_route_url(_query=query_params)

        return SqlalchemyOrmPage(query, page, items_per_page=5, url_maker=url_maker)
