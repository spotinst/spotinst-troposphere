from troposphere.cloudformation import AWSCustomObject, AWSProperty, integer


class BeanstalkElastigroupCapacity(AWSProperty):
    props = {
        'minimum': (integer, False),
        'maximum': (integer, False),
        'target': (integer, True),
    }

class BeanstalkEnvironmentNameConfig(AWSProperty):
    props = {
        'Ref': (basestring, True)
    }

class BeanstalkEnvironmentConfig(AWSProperty):
    props = {
        'environmentName': (BeanstalkEnvironmentNameConfig, True)
    }


class BeanstalkElastigroupConfig(AWSProperty):
    props = {
        'region': (basestring, True),
        'product': (basestring, True),
        'capacity': (BeanstalkElastigroupCapacity, True),
        'spotInstanceTypes': ([basestring], True),
        'beanstalk': (BeanstalkEnvironmentConfig, True)
    }



class BeanstalkElastigroup(AWSCustomObject):
    resource_type = "Custom::beanstalkElastigroup"

    props = {
        'ServiceToken': (basestring, True),
        'accessToken': (basestring, True),
        'accountId': (basestring, True),
        'beanstalkElastigroup': (BeanstalkElastigroupConfig, True)
    }