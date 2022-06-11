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

    def fetch_jamb_products(service_type):
        url = f'{Baxi.base_url}exampins/products'
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


class AccessBank():
    url = "https://api-sandbox.accessbankplc.com/openaccount/v1"
    authorization = 'SNWeS39P9xOQUsyUI6aCYy=='
    subscription_key = '0ddc8cf576594839a65d5a398b361a78'

    def open_account(title, email):
        base_url = f'{AccessBank.url}/CreateAccount'

        if title == 'Mr':
            gender = 'M'
        else:
            gender = 'F'

        datum = {
            "channelCode": "SANWOPAY",
            "customerID": "",
            "accountPurpose": "For Personal uses",
            "bvn": "22188829172",
            "title": "Mr.",
            "firstName": "Olatunde",
            "middleName": "Ade",
            "lastName": "Adebowale",
            "dateOfBirth": "1990-01-14",
            "gender": "M",
            "maritalStatus": "Married",
            "email": "tundetest@gmail.com",
            "phoneNumber1": "08038087624",
            "birthCountry": "NG",
            "placeOfbirth": "Lagos",
            "nationality": "NG",
            "religion": "Christianity",
            "maidenName": "Adebayo",
            "identificationType": "Driver's License",
            "idIssueState": "Lagos",
            "idIssueCountry": "NG",
            "identificationNo": "A02383830",
            "identityIssuedate": "2020-01-07",
            "identityExpirydate": "2024-01-07",
            "productCode": "020008",
            "accountCcyCode": "NGN",
            "accountBrCode": "014",
            "profession": "Banking",
            "annualIncome": "25000000",
            "referralCode": "A007",
            "staffID": "12338618",
            "residentialAddressLine1": "NewBase Estate",
            "residentialAddressLine2": "4 County Road",
            "residentialAddressLine3": "Off Arobiodun Street",
            "residentialAddressLine4": "Ogba, Lagos",
            "permanentAddressLine1": "Blue Cross",
            "permanentAddressLine2": "Saka Tinubu Street",
            "permanentAddressLine3": "Victoria Island",
            "permanentAddressLine4": "V.I, Lagos",
            "lgaOfResidence": "Yaba",
            "stateOfResidence": "Lagos State",
            "streetOfResidence": "County Road",
            "cityOfResidence": "Ogba",
            "houseLandmark": "Ogba",
            "pictureBase64": "",
            "signatureBase64": "",
            "imageBase64ID1": "",
            "imageBase64ID2": "",
            "imageBase64ID3": "",
            "imageBase64ID4": "",
            "imageBase64ID5": "",
            "imageBase64ID6": "",
            "refereeName1": "Sade Badmus",
            "refereeMobileno1": "08037078000",
            "refereeEmail1": "sadetest@yahoo.com",
            "refereeName2": "Kunle Peters",
            "refereeMobileno2": "08027770000",
            "refereeEmail2": "peterstest@yahoo.com",
            "needChequeBook": "Y",
            'subcription-key': AccessBank.subscription_key,
        }

        headers = {
            "Content-Type": "application/json",
            'Authorization': AccessBank.authorization,
            'Ocp-Apim-Subscription-Key': AccessBank.subscription_key,
        }
        response = requests.post(url=base_url, headers=headers, data=json.dumps(datum))

        return response.json()


def verifyNIN(nin, first_name, last_name):
    url = "https://vapi.verifyme.ng/v1/verifications/identities/nin/" + nin
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjgwOTAxLCJlbnYiOiJsaXZlIiwiaWF0IjoxNjIxMzQ0OTI1fQ.7FbuwOP7TiJxGYWgyt5PsBtaMN8M9jlfXOxw2s-H8YQ'
    }
    datum = {
        "firstname": first_name,
        "lastname": last_name
    }
    x = requests.post(url, data=json.dumps(datum), headers=headers)
    if x.status_code == 201:
        return x.json()
    else:
        results = {
            "status": "error",
            "message": x.json()["message"]
        }
        return results


class Dojah():

    base_url = 'https://sandbox.dojah.io/'
    live_url = 'https://api.dojah.io/'
    app_id = '628387965dfa1d003411c89b'
    secret_key = 'prod_sk_ynExQplYBSoEYMYfvWzWnSw0U'

    def verify_bvn(bvn):
        url = f'{Dojah.base_url}api/v1/kyc/bvn/full?bvn={bvn}'
        headers = {
            'Accept': 'text/plain',
            'AppId': Dojah.app_id,
            'Authorization': Dojah.secret_key,
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def verify_nin(nin):
        url = f'{Dojah.base_url}api/v1/kyc/nin?nin={nin}'
        headers = {
            'Accept': 'text/plain',
            'AppId': Dojah.app_id,
            'Authorization': Dojah.secret_key,
        }
        response = requests.get(url, headers=headers)
        return response.json()


print(Dojah.verify_nin(nin='89244161044'))


# print(AccessBank.open_account(title='Mr', email='click2bundi@gmail.com'))


# data = verifyNIN(nin='89244161044', first_name='Caleb', last_name='Pedro')
# print(data)



# title = "title"
# email = 'email'
# gender = 'gender'
# for_class = {
#     "channelCode": "SANWOPAY",
#     "accountPurpose": "For Personal uses",
#     "bvn": data['bvn'],
#     "title": title,
#     "firstName": data['first_name'],
#     "middleName": data['middle_name'],
#     "lastName": data['lastname'],
#     "dateOfBirth": data['date_of_birth'],
#     "gender": gender,
#     "maritalStatus": data["marital_status"],
#     "email": email,
#     "phoneNumber1": data['phone_number1'],
#     "nationality": "NG",
#     "stateOfResidence": data['state_of_residence']
# }


params = {
    'bvn': '22444225463',
    'first_name': 'Jack',
    'middle_name': 'Hendricks',
    'lastname': 'Alphonso',
    'date_of_birth': '25-May-1989',
    'marital_status': 'single',
    'phone_number1': '08139021881',
    'state_of_residence': 'lagos'
}
params2 = {
    "channelCode": "TESTAPP",
    "customerID": "",
    "accountPurpose": "For Personal uses",
    "bvn": "22188829172",
    "title": "Mr.",
    "firstName": "Olatunde",
    "middleName": "Ade",
    "lastName": "Adebowale",
    "dateOfBirth": "1990-01-14",
    "gender": "M",
    "maritalStatus": "Married",
    "email": "tundetest@gmail.com",
    "phoneNumber1": "08037077625",
    "birthCountry": "NG",
    "placeOfbirth": "Lagos",
    "nationality": "NG",
    "religion": "Christianity",
    "maidenName": "Adebayo",
    "identificationType": "Driver's License",
    "idIssueState": "Lagos",
    "idIssueCountry": "NG",
    "identificationNo": "A02383830",
    "identityIssuedate": "2020-01-07",
    "identityExpirydate": "2024-01-07",
    "productCode": "020008",
    "accountCcyCode": "NGN",
    "accountBrCode": "014",
    "profession": "Banking",
    "annualIncome": "25000000",
    "referralCode": "A007",
    "staffID": "12338618",
    "residentialAddressLine1": "NewBase Estate",
    "residentialAddressLine2": "4 County Road",
    "residentialAddressLine3": "Off Arobiodun Street",
    "residentialAddressLine4": "Ogba, Lagos",
    "permanentAddressLine1": "Blue Cross",
    "permanentAddressLine2": "Saka Tinubu Street",
    "permanentAddressLine3": "Victoria Island",
    "permanentAddressLine4": "V.I, Lagos",
    "lgaOfResidence": "Yaba",
    "stateOfResidence": "Lagos State",
    "streetOfResidence": "County Road",
    "cityOfResidence": "Ogba",
    "houseLandmark": "Ogba",
    "pictureBase64": "",
    "signatureBase64": "",
    "imageBase64ID1": "",
    "imageBase64ID2": "",
    "imageBase64ID3": "",
    "imageBase64ID4": "",
    "imageBase64ID5": "",
    "imageBase64ID6": "",
    "refereeName1": "Sade Badmus",
    "refereeMobileno1": "08037078000",
    "refereeEmail1": "sadetest@yahoo.com",
    "refereeName2": "Kunle Peters",
    "refereeMobileno2": "08027770000",
    "refereeEmail2": "peterstest@yahoo.com",
    "needChequeBook": "Y"
}
#account = AccessBank.open_account(
#    title='Mr',
#    email='codebundi@gmail.com'
#)
#print(account)
# jamb = Baxi.fetch_jamb_products(service_type='jamb')
# print(jamb)


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
# print(Baxi.get_e_pin_service_providers(self='self'))
n = datetime.datetime.now(datetime.timezone.utc)
n.isoformat()
# print(n)


# print(Baxi.retrieve_provider_bundles(service_type))
# print(Baxi.purchase_data_bundle(
#    agentReference=agentReference,
#    agentId=agentId,
#    datacode=datacode,
#    service_type=service_type,
#    amount=amount,
#    phone=phone
#))
# verify = Baxi.account_name_validation(account_number=DSTV, service_type='dstv')
# print(verify['status'])
# print(Baxi.retrieve_provider_bouquets(service_type='dstv'))
# print('break')
# print(Baxi.retrieve_provider_addons(service_type='dstv', product_code='PRWFRNSE36'))

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

