from zeep import Client
import requests
# SOAP request URL
url = "http://154.113.16.142:9999/Payments/api?wsdl"

# structured XML
payload = """
    <?xml version=\"1.0\" encoding=\"utf-8\"?>
    <soap:Envelope xmlns:soap=\"http://providus.com\">
    <soap:Body>
        <prov:GetBVNDetails>
            <ns2:GetBVNDetailsResponse xmlns=\"http://providus.com/\">
            <bvn>22153013441</bvn>
            <username>test</username>
            <password>test</password>
        </prov:GetBVNDetails>
    </soap:Body>
</soap:Envelope>"""
# headers
headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}
# POST request
response = requests.post(url, headers=headers, data=payload)

# prints the response
print(response.text)
print(response)

client = Client(wsdl='http://154.113.16.142:/Payments/api?wsdl')
client.service.GetNIPAccount()
'<CountryIntPhoneCode xmlns=\"http://154.113.16.142:/Payments/api\">'