import requests
import json
import time
import datetime

class Baxi():
    base_url = 'https://payments.baxipay.com.ng/api/baxipay/'  # test parameters
    username = 'baxi_test'
    user_secret = '5xjqQ7MafFJ5XBTN'
    api_key = '5adea9-044a85-708016-7ae662-646d59'
    Accept = "application/json"
    Content_Type = "application/json"

    def requery_transaction(agentReference):
        url = f'{Baxi.base_url}superagent/transaction/requery'
        headers = {
            'x-api-key': Baxi.api_key,
            'Accept': Baxi.Accept,
            'Content-Type': Baxi.Content_Type,
        }
        print(agentReference)
        datum = {
            'agentReference': agentReference
        }
        x = requests.get(url, headers=headers, data=json.dumps(datum))
        return x.json()

    def get_balance(self):
        url = f'{Baxi.base_url}superagent/account/balance'
        headers = {
            'x-api-key': Baxi.api_key,
            'Accept': Baxi.Accept,
            'Content-Type': Baxi.Content_Type
        }
        x = requests.get(url, headers=headers)
        return x.json()

    def fetch_biller_categories(self):
        url = f'{Baxi.base_url}billers/category/all'
        headers = {
            'x-api-key': Baxi.api_key,
            'Accept': Baxi.Accept,
            'Content-Type': Baxi.Content_Type
        }
        x = requests.get(url, headers=headers)
        return x.json()

    def fetch_biller_all(self):
        url = f'{Baxi.base_url}billers/services/list'
        headers = {
            'x-api-key': Baxi.api_key,
            'Accept': Baxi.Accept,
            'Content-Type': Baxi.Content_Type
        }
        x = requests.get(url, headers=headers)
        return x.json()

    def fetch_biller_by_category(category):
        url = f'{Baxi.base_url}billers/services/category'
        headers = {
            'x-api-key': Baxi.api_key,
            'Accept': Baxi.Accept,
            'Content-Type': Baxi.Content_Type
        }
        datum = {
            'service_type': 'databundle'
        }
        x = requests.post(url, headers=headers, data=json.dumps(datum))
        return x.json()

    def get_airtime_recharge_providers(self):
        url = f'{Baxi.base_url}services/airtime/providers'
        headers = {
            'x-api-key': Baxi.api_key,
            'Accept': Baxi.Accept,
            'Content-Type': Baxi.Content_Type
        }
        x = requests.get(url=url, headers=headers)
        return x.json()

    def purchase_airtime(agentReference, agentId, service_type, amount, phone):
        url = f'{Baxi.base_url}services/airtime/request'
        headers = {
            'x-api-key': Baxi.api_key,
            'Accept': Baxi.Accept,
            'Content-Type': Baxi.Content_Type
        }
        datum = {
            'agentReference': agentReference,
            'agentId': agentId,
            'plan': 'prepaid',
            'service_type': service_type,
            'amount': amount,
            'phone': phone
        }
        x = requests.post(url=url, headers=headers, data=json.dumps(datum))
        return x.json()

    def get_databundle_providers(self):
        url = f'{Baxi.base_url}services/databundle/providers'
        headers = {
            'x-api-key': Baxi.api_key,
            'Accept': Baxi.Accept,
            'Content-Type': Baxi.Content_Type,
            'Baxi-date': str(datetime.datetime.now())
        }
        x = requests.get(url=url, headers=headers)
        return x.json()

    def retrieve_provider_bundles(service_type, account_number=None):
        url = f'{Baxi.base_url}services/databundle/bundles'
        headers = {
            'x-api-key': Baxi.api_key,
            'Accept': Baxi.Accept,
            'Content-Type': Baxi.Content_Type,
            'Baxi-date': str(datetime.datetime.now())
        }
        datum = {
            'service_type': service_type
        }
        if service_type == 'SPECTRANET':
            datum = {
                'service_type': service_type,
                'account_number': account_number
            }
        x = requests.post(url=url, headers=headers, data=json.dumps(datum))
        return x.json()

    def purchase_data_bundle(agentReference, agentId, datacode, service_type, amount, phone, package=None):
        url = f'{Baxi.base_url}services/databundle/request'
        headers = {
            'x-api-key': Baxi.api_key,
            'Accept': Baxi.Accept,
            'Content-Type': Baxi.Content_Type,
            'Baxi-date': str(datetime.datetime.now())
        }
        datum = {
            "agentReference": agentReference,
            "agentId": agentId,
            "datacode": datacode,
            "service_type": service_type,
            "amount": amount,
            "phone": phone
        }
        if service_type == 'SPECTRANET':
            datum = {
                "agentReference": agentReference,
                "agentId": agentId,
                "datacode": datacode,
                "service_type": service_type,
                "amount": amount,
                "phone": phone,
                "package": package
            }
        x = requests.post(url=url, headers=headers, data=json.dumps(datum))
        return x.json()

    def account_name_validation(account_number, service_type):
        url = f'{Baxi.base_url}services/namefinder/query'
        headers = {
            'x-api-key': Baxi.api_key,
            'Accept': Baxi.Accept,
            'Content-Type': Baxi.Content_Type,
        }
        datum = {
            'account_number': account_number,
            "service_type": service_type
        }
        x = requests.post(url=url, headers=headers, data=json.dumps(datum))
        return x.json()

    def renewal_cable(total_amount, products_monthsPaidFor, product_code, service_type, agentId, agentReference, \
                      smartcard_number, isBoxOffice='False'):
        url = f'{Baxi.base_url}services/multichoice/request'
        headers = {
            'x-api-key': Baxi.api_key,
            'Accept': Baxi.Accept,
            'Content-Type': Baxi.Content_Type,
        }
        datum = {
            'total_amount': total_amount,
            'products_monthsPaidFor': products_monthsPaidFor,
            'product_code': product_code,
            'service_type': service_type,
            'agentId': agentId,
            'agentReference': agentReference,
            'smartcard_number': smartcard_number
        }
        if isBoxOffice:
            datum['isBoxOffice'] = isBoxOffice
        x = requests.post(url=url, headers=headers, data=json.dumps(datum))
        return x.json()

    def retrieve_provider_bouquets(service_type):  # for only change of bouquets and subscription plans
        url = f'{Baxi.base_url}services/multichoice/list'
        headers = {
            'x-api-key': Baxi.api_key,
            'Accept': Baxi.Accept,
            'Content-Type': Baxi.Content_Type,
        }
        datum = {
            'service_type': service_type
        }
        x = requests.post(url=url, headers=headers, data=json.dumps(datum))
        return x.json()

    def retrieve_provider_addons(service_type, product_code):  # for only change of bouquets and subscription plans
        url = f'{Baxi.base_url}services/multichoice/addons'
        headers = {
            'x-api-key': Baxi.api_key,
            'Accept': Baxi.Accept,
            'Content-Type': Baxi.Content_Type,
        }
        datum = {
            'service_type': service_type,
            'product_code': product_code
        }
        x = requests.post(url=url, headers=headers, data=json.dumps(datum))
        return x.json()

    def get_e_pin_service_providers(self):
        url = f'{Baxi.base_url}services/epin/providers'
        headers = {
            'x-api-key': Baxi.api_key,
            'Accept': Baxi.Accept,
            'Content-Type': Baxi.Content_Type,
        }
        x = requests.get(url=url, headers=headers)
        return x.json()


category = 'Airtime Recharge'
service_type = 'mtn'
phone = '08139021881'
datacode = '1500'
amount = 1500
agentId = 207
agentReference = 'AX14s68P2k'
# test smartcard number
DSTV = '4131953321'
GOTV = '2005129242'
Startimes = '02110144711'

# print(Baxi.fetch_biller_categories(self='self'))
# print(Baxi.fetch_biller_by_category(category))
# print(Baxi.get_airtime_recharge_providers(self='self'))
# print(Baxi.get_databundle_providers(self='self'))
# print(time)
print(Baxi.get_e_pin_service_providers(self='self'))
n = datetime.datetime.now(datetime.timezone.utc)
n.isoformat()
print(n)


# print(Baxi.retrieve_provider_bundles(service_type))
# print(Baxi.purchase_data_bundle(
#    agentReference=agentReference,
#    agentId=agentId,
#    datacode=datacode,
#    service_type=service_type,
#    amount=amount,
#    phone=phone
#))
# print(Baxi.account_name_validation(account_number=DSTV, service_type='dstv'))
print(Baxi.retrieve_provider_bouquets(service_type='dstv'))
print('break')
print(Baxi.retrieve_provider_addons(service_type='dstv', product_code='PRWFRNSE36'))

# data = {
#        'status': 'success',
#        'message': 'Successful',
#        'code': 200,
#        'data': {
#            'user': {
#                'name': 'Sten Mockett',
#                'address': None,
#                'outstandingBalance': 2500,
#                'dueDate': '2022-05-14T21:37:51.399+01:00',
#                'district': None,
#                'accountNumber': None,
#                'minimumAmount': None,
#                'rawOutput': {
#                    'accountStatus': 'OPEN',
#                    'firstName': 'Sten',
#                    'lastName': 'Mockett',
#                    'customerType': 'SUD',
#                    'invoicePeriod': 1,
#                    'dueDate': '2022-06-09T21:37:51.219+01:00',
#                    'customerNumber': 25002641
#                    },
#                'errorMessage': None,
#                'hasDiscount': False,
#                'currentBouquetRaw': {
#                    'amount': 14025,
#                    'items': [
#                        {
#                            'code': 'COMPE36',
#                            'price': 6975,
#                            'name': 'DStv Compact Bouquet E36',
#                            'description': 'DStv Compact Bouquet E36'
#                        },
#                        {
#                            'code': 'ASIADDE36',
#                            'price': 5540,
#                            'name': 'Asian Add-on',
#                            'description': 'Asian Add-on'
#                        },
#                        {
#                            'code': 'FRN7E36',
#                            'price': 1510, 'name':
#                            'French Touch',
#                            'description': 'French Touch'
#                        }
#                    ]
#                },
#                'currentBouquet': 'DStv Compact Bouquet E36 + Asian Add-on + French Touch'
#        }
#    }

