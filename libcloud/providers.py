from libcloud.types import Provider, ProviderCreds

def get_provider(provider):
  if provider == Provider.DUMMY:
    from libcloud.dummy import DummyProvider
    return DummyProvider
  if provider == Provider.EC2:
    from libcloud.ec2 import EC2Provider
    return EC2Provider

def connect(provider, key, secret=None):
  creds = ProviderCreds(provider, key, secret)
  return get_provider(provider)(creds)
