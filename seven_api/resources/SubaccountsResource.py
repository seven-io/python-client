from seven_api.classes.Endpoint import Endpoint
from seven_api.classes.Method import Method
from seven_api.classes.Subaccounts import SubaccountsAction
from seven_api.resources.Resource import Resource


class SubaccountsResource(Resource):
    def read(self) -> list:
        return self._client.request(Method.GET, Endpoint.SUBACCOUNTS, {'action': SubaccountsAction.READ}).json()

    def create(self, params: dict) -> dict:
        params['action'] = SubaccountsAction.CREATE
        return self._client.request(Method.POST, Endpoint.SUBACCOUNTS, params).json()

    def auto_charge(self, params: dict) -> dict:
        params['action'] = SubaccountsAction.UPDATE
        return self._client.request(Method.POST, Endpoint.SUBACCOUNTS, params).json()

    def transfer_credits(self, params: dict) -> dict:
        params['action'] = SubaccountsAction.TRANSFER_CREDITS
        return self._client.request(Method.POST, Endpoint.SUBACCOUNTS, params).json()

    def delete(self, params: dict) -> dict:
        params['action'] = SubaccountsAction.DELETE
        return self._client.request(Method.POST, Endpoint.SUBACCOUNTS, params).json()
