====================
spotinst troposphere
====================

About
=====

An addition to troposphere - which allows for the creation of spotinst resources.
Currently only the spotinst beanstalk elastigroup is supported

Installation
============

After installing troposphere, add the beanstalk_elastigroup file to your library, and use the code in the usage.py file as an example.

Examples
========
For Usage example, please see usage.py

Output example
::
    {
        "Description": "Create a beanstalk elastigroup based on a beanstalk environment import through a Cloudformation custom resource",
        "Resources": {
            "SpotinstBeanstalkElastigroup": {
                "Properties": {
                    "ServiceToken": "arn:aws:lambda:us-west-2:178579023202:function:spotinst-cloudformation",
                    "accessToken": "your-token",
                    "accountId": "your-account-id",
                    "beanstalkElastigroup": {
                        "DependsOn": "beanstalkEnv",
                        "beanstalk": {
                            "environmentName": {
                                "Ref": "beanstalkEnv"
                            }
                        },
                        "capacity": {
                            "maximum": 10,
                            "minimum": 0,
                            "target": 0
                        },
                        "product": "Linux/UNIX",
                        "region": "us-west-2",
                        "spotInstanceTypes": [
                            "c3.large",
                            "m3.large"
                        ]
                    }
                },
                "Type": "Custom::beanstalkElastigroup"
            },
            "beanstalkEnv": {
                "Properties": {
                    "ApplicationName": "Spotinst App Test",
                    "Description": "Spotinst Beanstalk Test Environment",
                    "EnvironmentName": "SpotinstBeanstalkTestEnv",
                    "OptionSettings": [
                        {
                            "Namespace": "aws:autoscaling:asg",
                            "OptionName": "MinSize",
                            "Value": "0"
                        },
                        {
                            "Namespace": "aws:autoscaling:asg",
                            "OptionName": "MaxSize",
                            "Value": "0"
                        }
                    ],
                    "SolutionStackName": "64bit Amazon Linux 2017.03 v2.5.4 running Java 8",
                    "VersionLabel": "Sample Application"
                },
                "Type": "AWS::ElasticBeanstalk::Environment"
            }
        }
    }