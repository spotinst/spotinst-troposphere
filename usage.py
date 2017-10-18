from troposphere import Template
from troposphere.elasticbeanstalk import OptionSettings, Environment

from beanstalk_elastigroup import BeanstalkEnvironmentConfig, BeanstalkElastigroup, BeanstalkElastigroupCapacity, \
    BeanstalkElastigroupConfig, BeanstalkEnvironmentNameConfig

t = Template()

t.add_description(
    "Create a beanstalk elastigroup based on a beanstalk environment import through a Cloudformation custom resource"
)

# Create the beanstalk environment
beanstalk = t.add_resource(
    Environment(
        title='beanstalkEnv',
        ApplicationName='Spotinst App Test',
        Description='Spotinst Beanstalk Test Environment',
        EnvironmentName='SpotinstBeanstalkTestEnv',
        SolutionStackName='64bit Amazon Linux 2017.03 v2.5.4 running Java 8',
        VersionLabel='Sample Application',
        OptionSettings=[
            OptionSettings(
                Namespace='aws:autoscaling:asg',
                OptionName='MinSize',
                Value='0'),
            OptionSettings(
                Namespace='aws:autoscaling:asg',
                OptionName='MaxSize',
                Value='0')
        ]))


# Import the beanstalk environment into an elastigroup
beanstalk_elastigroup = t.add_resource(BeanstalkElastigroup(
    "SpotinstBeanstalkElastigroup",
    ServiceToken="arn:aws:lambda:us-west-2:178579023202:function:spotinst-cloudformation",
    accessToken="your-token",
    accountId="your-account-id",
    beanstalkElastigroup=BeanstalkElastigroupConfig(
        region='us-west-2',
        product="Linux/UNIX",
        name='BeanstalkName',
        capacity=BeanstalkElastigroupCapacity(
            minimum=0,
            maximum=10,
            target=0),
        spotInstanceTypes=["c3.large", "m3.large"],
        beanstalk=BeanstalkEnvironmentConfig(
            environmentName=BeanstalkEnvironmentNameConfig(
                Ref="beanstalkEnv"))),
    DependsOn='beanstalkEnv'
))

print(t.to_json())
