from troposphere.cloudformation import AWSCustomObject, AWSProperty, integer


class BeanstalkElastigroupCapacity(AWSProperty):
    props = {
        'minimum': (integer, False),
        'maximum': (integer, False),
        'target': (integer, True),
    }

class BeanstalkEnvironmentNameConfig(AWSProperty):
    props = {
        'Ref': (str, True)
    }

class BeanstalkEnvironmentConfig(AWSProperty):
    props = {
        'environmentName': (BeanstalkEnvironmentNameConfig, True)
    }


class BeanstalkElastigroupConfig(AWSProperty):
    props = {
        'region': (str, True),
        'product': (str, True),
        'name':(str, False),
        'capacity': (BeanstalkElastigroupCapacity, True),
        'spotInstanceTypes': ([str], True),
        'beanstalk': (BeanstalkEnvironmentConfig, True)
    }



class BeanstalkElastigroup(AWSCustomObject):
    resource_type = "Custom::beanstalkElastigroup"

    props = {
        'ServiceToken': (str, True),
        'accessToken': (str, True),
        'accountId': (str, True),
        'beanstalkElastigroup': (BeanstalkElastigroupConfig, True)
    }