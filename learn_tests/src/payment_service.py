import requests

class PaymentService:

    def pay(self, amount):
        url = 'https://httpbin.org/post'
        response = requests.post(url, json={'amount': amount})

        if response.status_code != 200:
            return False
        response_amount = response.json()['json']['amount']

        return response_amount == amount

