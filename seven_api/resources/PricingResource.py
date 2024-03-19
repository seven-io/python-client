from seven_api.classes.Endpoint import Endpoint
from seven_api.classes.Method import Method
from seven_api.resources.Resource import Resource


class PricingResource(Resource):
    def retrieve(self, country: str = None) -> dict:
        return self._client.request(Method.GET, Endpoint.PRICING, {'country': country}).json()
