from seven_api.classes.Analytics import AnalyticsGroupBy
from seven_api.classes.Endpoint import Endpoint
from seven_api.classes.Method import Method
from seven_api.resources.Resource import Resource


class AnalyticsResource(Resource):
    def by_country(self, params=None) -> list:
        return self.__get(AnalyticsGroupBy.COUNTRY, params)

    def by_date(self, params=None) -> list:
        return self.__get(AnalyticsGroupBy.DATE, params)

    def by_label(self, params=None) -> list:
        return self.__get(AnalyticsGroupBy.LABEL, params)

    def by_subaccount(self, params=None) -> list:
        return self.__get(AnalyticsGroupBy.SUBACCOUNT, params)

    def __get(self, group_by: AnalyticsGroupBy, params=None) -> list:
        if params is None: params = {}
        params['group_by'] = group_by.value
        return self._client.request(Method.GET, Endpoint.ANALYTICS, params)
