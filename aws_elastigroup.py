from troposphere.cloudformation import AWSCustomObject, integer, AWSProperty


class ElastigroupThirdPartiesIntegrationRancher(AWSProperty):
    props = {
        'accessKey': (bool, True),
        'secretKey': (bool, True),
        'masterHost': (bool, True)
    }


class ElastigroupThirdPartiesIntegrationMesosphere(AWSProperty):
    props = {
        'apiServer': (basestring, True)
    }


class ElastigroupThirdPartiesIntegrationElasticBeanstalkDEploymentPreferencesStrategy(AWSProperty):
    props = {
        'action': (basestring, True),
        'shouldDrainInstances': (bool, False)
    }


class ElastigroupThirdPartiesIntegrationElasticBeanstalkDEploymentPreferences(AWSProperty):
    props = {
        'automaticRoll': (bool, True),
        'batchSizePercentage': (integer, False),
        'gracePeriod': (integer, False),
        'strategy': (ElastigroupThirdPartiesIntegrationElasticBeanstalkDEploymentPreferencesStrategy, False)
    }


class ElastigroupThirdPartiesIntegrationElasticBeanstalk(AWSProperty):
    props = {
        'environmentId': (basestring, True),
        'deploymentPreferences': (ElastigroupThirdPartiesIntegrationElasticBeanstalkDEploymentPreferences, False)
    }


class ElastigroupThirdPartiesIntegrationEcsAutoScaleHeadroom(AWSProperty):
    props = {
        'cpuPerUnit': (integer, False),
        'memoryPerUnit': (integer, False),
        'numOfUnits': (integer, False)
    }


class ElastigroupThirdPartiesIntegrationEcsAutoScaleDown(AWSProperty):
    props = {
        'evaluationPeriods': (integer, False)
    }


class ElastigroupThirdPartiesIntegrationEcsAutoScale(AWSProperty):
    props = {
        'isEnabled': (bool, False),
        'cooldown': (integer, False),
        'headroom': (ElastigroupThirdPartiesIntegrationEcsAutoScaleHeadroom, False),
        'down': (ElastigroupThirdPartiesIntegrationEcsAutoScaleDown, False)
    }


class ElastigroupThirdPartiesIntegrationEcs(AWSProperty):
    props = {
        'clusterName': (basestring, True),
        'autoScale': (ElastigroupThirdPartiesIntegrationEcsAutoScale, False)
    }


class ElastigroupThirdPartiesIntegrationMlbRuntime(AWSProperty):
    props = {
        'deploymentId': (basestring, True)
    }


class ElastigroupThirdPartiesIntegrationKubernetes(AWSProperty):
    props = {
        'apiServer': (basestring, True),
        'token': (basestring, True)
    }


class ElastigroupThirdPartiesIntegrationRightScale(AWSProperty):
    props = {
        'accountId': (basestring, True),
        'refreshToken': (basestring, True),
        'region': (basestring, False),
    }


class ElastigroupThirdPartiesIntegrationOpsWorks(AWSProperty):
    props = {
        'layerId': (basestring, True),
        'stackType': (basestring, True),
    }


class ElastigroupThirdPartiesIntegrationCodeDeployDeploymentGroups(AWSProperty):
    props = {
        'applicationName': (basestring, True),
        'deploymentGroupName': (basestring, True)
    }


class ElastigroupThirdPartiesIntegrationCodeDeploy(AWSProperty):
    props = {
        'deploymentGroups': (ElastigroupThirdPartiesIntegrationCodeDeployDeploymentGroups, True),
        'cleanUpOnFailure': (bool, False),
        'terminateInstanceOnFailure': (bool, False)
    }


class ElastigroupThirdPartiesIntegrationChef(AWSProperty):
    props = {
        'chefServer': (basestring, True),
        'organization': (basestring, True),
        'user': (basestring, True),
        'pemKey': (basestring, True),
        'chefVersion': (basestring, True),
    }


class ElastigroupThirdPartiesIntegrationNomad(AWSProperty):
    props = {
        'masterHost': (basestring, True),
        'masterPort': (integer, True)
    }


class ElastigroupThirdPartiesIntegrationDockerSwarm(AWSProperty):
    props = {
        'masterHost': (basestring, True),
        'masterPort': (integer, True)
    }


class ElastigroupThirdPartiesIntegration(AWSProperty):
    props = {
        'rancher': (ElastigroupThirdPartiesIntegrationRancher, False),
        'mesosphere': (ElastigroupThirdPartiesIntegrationMesosphere, False),
        'elasticBeanstalk': (ElastigroupThirdPartiesIntegrationElasticBeanstalk, False),
        'ecs': (ElastigroupThirdPartiesIntegrationEcs, False),
        'mlbRuntime': (ElastigroupThirdPartiesIntegrationMlbRuntime, False),
        'kubernetes': (ElastigroupThirdPartiesIntegrationKubernetes, False),
        'rightScale': (ElastigroupThirdPartiesIntegrationRightScale, False),
        'opsWorks': (ElastigroupThirdPartiesIntegrationOpsWorks, False),
        'codeDeploy': (ElastigroupThirdPartiesIntegrationCodeDeploy, False),
        'chef': (ElastigroupThirdPartiesIntegrationChef, False),
        'nomad': (ElastigroupThirdPartiesIntegrationNomad, False),
        'dockerSwarm': (ElastigroupThirdPartiesIntegrationDockerSwarm, False)
    }


class ElastigroupComputeInstanceTypeWeight(AWSProperty):
    props = {
        'instanceType': (basestring, True),
        'weightedCapacity': (basestring, True)
    }


class ElastigroupComputeInstanceTypes(AWSProperty):
    props = {
        'ondemand': (basestring, True),
        'spot': ([basestring], True),
        'weights': ([ElastigroupComputeInstanceTypeWeight], False)
    }


class ElastigroupComputeAvailabilityZone(AWSProperty):
    props = {
        'name': (basestring, True),
        'subnetId': (basestring, False),
        'subnetIds': ([basestring], False),
        'placementGroupName': (basestring, False)
    }


class ElastigroupComputeLaunchSpecificationLoadBalancerConfigLoadBalancer(AWSProperty):
    props = {
        'name': (basestring, False),
        'arn': (basestring, False),
        'balancerId': (basestring, False),
        'targetSetId': (basestring, False),
        'azAwareness': (bool, False),
        'autoWeight': (bool, False),
        'type': (basestring, True)
    }


class ElastigroupComputeLaunchSpecificationLoadBalancerConfig(AWSProperty):
    props = {
        'loadBalancers': ([ElastigroupComputeLaunchSpecificationLoadBalancerConfigLoadBalancer], False),
    }


class ElastigroupComputeLaunchSpecificationIamRole(AWSProperty):
    props = {
        'name': (basestring, False),
        'arn': (basestring, False),
        'iamRole': (basestring, False)
    }


class ElastigroupComputeLaunchSpecificationBlockDeviceEbs(AWSProperty):
    props = {
        'deleteOnTermination': (bool, False),
        'encrypted': (bool, False),
        'iops': (integer, False),
        'snapshotId': (basestring, False),
        'volumeSize': (integer, False),
        'volumeType': (basestring, False)
    }


class ElastigroupComputeLaunchSpecificationBlockDevice(AWSProperty):
    props = {
        'deviceName': (basestring, False),
        'eb': (ElastigroupComputeLaunchSpecificationBlockDeviceEbs, False),
        'noDevice': (basestring, False),
        'virtualName': (basestring, False)
    }


class ElastigroupComputeLaunchSpecificationNetworkInterfacePrivateIpAddress(AWSProperty):
    props = {
        'privateIpAddress': (basestring, True),
        'primary': (bool, False)
    }


class ElastigroupComputeLaunchSpecificationNetworkInterface(AWSProperty):
    props = {
        'description': (basestring, False),
        'deviceIndex': (integer, False),
        'secondaryPrivateIpAddressCount': (integer, False),
        'associatePublicIpAddress': (bool, False),
        'deleteOnTermination': (bool, False),
        'groups': ([basestring], False),
        'networkInterfaceId': (basestring, False),
        'privateIpAddress': (basestring, False),
        'privateIpAddresses': ([ElastigroupComputeLaunchSpecificationNetworkInterfacePrivateIpAddress], False),
        'subnetId': (basestring, False),
        'associateIpv6Address': (bool, False),
    }


class ElastigroupComputeLaunchSpecificationTag(AWSProperty):
    props = {
        'tagKey': (basestring, False),
        'tagValue': (basestring, False)
    }


class ElastigroupComputeLaunchSpecification(AWSProperty):
    props = {
        'loadBalancerNames': ([basestring], False),
        'loadBalancersConfig': (ElastigroupComputeLaunchSpecificationLoadBalancerConfig, False),
        'healthCheckType': (basestring, False),
        'healthCheckGracePeriod': (integer, False),
        'healthCheckUnhealthyDurationBeforeReplacement': (integer, False),
        'securityGroupIds': ([basestring], False),
        'monitoring': (bool, False),
        'ebsOptimized': (bool, False),
        'imageId': (basestring, False),
        'tenancy': (basestring, False),
        'iamRole': (ElastigroupComputeLaunchSpecificationIamRole, False),
        'keyPair': (basestring, False),
        'userData': (basestring, False),
        'shutdownScript': (basestring, False),
        'blockDeviceMappings': ([ElastigroupComputeLaunchSpecificationBlockDevice], False),
        'networkInterfaces': ([ElastigroupComputeLaunchSpecificationNetworkInterface], False),
        'tags': ([ElastigroupComputeLaunchSpecificationTag], False)

    }


class ElastigroupCompute(AWSProperty):
    props = {
        'elasticIps': ([basestring], False),
        'instanceTypes': (ElastigroupComputeInstanceTypes, True),
        'product': (basestring, True),
        'availabilityZones': ([ElastigroupComputeAvailabilityZone], True),
        'launchSpecification': (ElastigroupComputeLaunchSpecification, True),
    }


class ElastigroupCapacity(AWSProperty):
    props = {
        'minimum': (integer, False),
        'maximum': (integer, False),
        'target': (integer, True),
        'unit': (basestring, True),
    }


class ElastigroupSignals(AWSProperty):
    props = {
        'name': (basestring, True),
        'timeout': (integer, True)
    }


class ElastigroupScalingStrategy(AWSProperty):
    props = {
        'terminateAtEndOfBillingHour': (bool, True),
    }


class ElastigroupPersistence(AWSProperty):
    props = {
        'shouldPersistBlockDevices': (bool, False),
        'shouldPersistRootDevice': (bool, False),
        'shouldPersistPrivateIp': (bool, False),
        'blockDevicesMode': (basestring, False),
    }


class ElastigroupStrategy(AWSProperty):
    props = {
        'risk': (integer, False),
        'onDemandCount': (integer, False),
        'utilizeReservedInstances': (bool, False),
        'fallbackToOd': (bool, False),
        'availabilityVsCost': (basestring, False),
        'drainingTimeout': (integer, False),
        'spinUpTime': (integer, False),
        'lifetimePeriod': (basestring, False),
        'signals': ([ElastigroupSignals], False),
        'scalingStrategy': (ElastigroupScalingStrategy, False),
        'persistence': (ElastigroupPersistence, False)
    }


class ElastigroupScalingDimension(AWSProperty):
    props = {
        'name': (basestring, True),
        'value': (basestring, False)
    }


class ElastigroupScalingUpAction(AWSProperty):
    props = {
        'type': (basestring, True),
        'adjustment': (basestring, False),
        'minTargetCapacity': (basestring, False),
        'target': (basestring, False),
        'minimum': (basestring, False),
        'maximum': (basestring, False),
    }


class ElastigroupScalingUp(AWSProperty):
    props = {
        'action': (ElastigroupScalingUpAction, False),
        'policyName': (basestring, False),
        'namespace': (basestring, True),
        'source': (basestring, False),
        'metricName': (basestring, True),
        'dimensions': ([ElastigroupScalingDimension], False),
        'statistic': (basestring, False),
        'extendedStatistic': (basestring, False),
        'unit': (basestring, False),
        'threshold': (integer, True),
        'adjustment': (integer, False),
        'minTargetCapacity': (integer, False),
        'period': (integer, False),
        'evaluationPeriods': (integer, False),
        'cooldown': (integer, False),
        'operator': (basestring, False)
    }


class ElastigroupScalingDownAction(AWSProperty):
    props = {
        'type': (basestring, True),
        'adjustment': (basestring, False),
        'minTargetCapacity': (basestring, False),
        'target': (basestring, False),
        'minimum': (basestring, False),
        'maximum': (basestring, False),
    }


class ElastigroupScalingDown(AWSProperty):
    props = {
        'policyName': (basestring, False),
        'namespace': (basestring, True),
        'source': (basestring, False),
        'metricName': (basestring, True),
        'dimensions': ([ElastigroupScalingDimension], False),
        'statistic': (basestring, False),
        'extendedStatistic': (basestring, False),
        'unit': (basestring, False),
        'threshold': (integer, True),
        'adjustment': (integer, False),
        'maxTargetCapacity': (integer, False),
        'period': (integer, False),
        'evaluationPeriods': (integer, False),
        'cooldown': (integer, False),
        'action': (ElastigroupScalingDownAction, False),
        'operator': (basestring, False)
    }


class ElastigroupScaling(AWSProperty):
    props = {
        'up': ([ElastigroupScalingUp], False),
        'down': ([ElastigroupScalingDown], False)
    }


class ElastigroupSchedulingTask(AWSProperty):
    props = {
        'isEnabled': (bool, False),
        'frequency': (basestring, False),
        'cronExpression': (basestring, False),
        'taskType': (basestring, True),
        'scaleTargetCapacity': (integer, False),
        'scaleMinCapacity': (integer, False),
        'scaleMaxCapacity': (integer, False),
        'batchSizePercentage': (integer, False),
        'gracePeriod': (integer, False),
        'adjustment': (integer, False),
        'adjustmentPercentage': (integer, False),
        'targetCapacity': (integer, False),
        'minCapacity': (integer, False),
        'maxCapacity': (integer, False)
    }


class ElastigroupScheduling(AWSProperty):
    props = {
        'tasks': ([ElastigroupSchedulingTask], False)
    }


class ElastigroupConfig(AWSProperty):
    props = {
        'name': (basestring, False),
        'description': (basestring, False),
        'capacity': (ElastigroupCapacity, True),
        'strategy': (ElastigroupStrategy, True),
        'scaling': (ElastigroupScaling, False),
        'scheduling': (ElastigroupScheduling, False),
        'thirdPartiesIntegration': (ElastigroupThirdPartiesIntegration, False),
        'compute': (ElastigroupCompute, True),
    }


class Elastigroup(AWSCustomObject):
    resource_type = "Custom::elastigroup"

    props = {
        'ServiceToken': (basestring, True),
        'accessToken': (basestring, True),
        'accountId': (basestring, True),
        'group': (ElastigroupConfig, True)
    }
