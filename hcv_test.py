import hvac   

client = hvac.Client(
    url='https://vault-int.app.corpintra.net/',
    namespace='HCV-test',
    token='hvs.CAESIAiBabSB_0VVYQFXqHTb9A6vmYpFreFhULsKPHAFL9h9GikKImh2cy5ldDluRGdLWG03NFc1UjFqS2dwdGs3SHouNjBybmoQonYYBA',
)

# Reading a secret - HCV-test/kv/test
read_response = client.secrets.kv.read_secret_version(path='test', mount_point='kv')

password = read_response['data']['data']['bar']


print(password)