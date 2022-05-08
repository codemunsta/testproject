from zeep import Client

client = Client(wsdl='http://154.113.16.142:9999/Payments/api?wsdl')
account_number = '0002842719'
bank_code = '000013'
username = 'test'
password = 'test'
transaction_reference = '1324536'
# print(client.service.GetNIPAccount(account_number, bank_code, username, password))
# print(client.service.GetNIPTransactionStatus())
# print(client.service.GetNIPTransactionStatus(transaction_reference, username, password))
# print(client.service.GetProvidusAccount(account_number, username, password))
print((client.service. GetProvidusTransactionStatus(transaction_reference, username, password)))
'''
    amount, currency, narration, transaction_reference, debit_account, recipient_account_number, recipient_bank_code, \
    account_name, originator_name, username, password
'''