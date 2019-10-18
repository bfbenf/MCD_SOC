from saba.client import SabaClient
#from saba.auth.certificate import CertificateAuthentication

host = 'mcdcampus-api.sabacloud.com'
user = '00702@uk.mcd.com'
password = 'Password1'

cert = CertificateAuthentication(host, user, password)

client = SabaClient(host, cert)

print(client.courses.all())