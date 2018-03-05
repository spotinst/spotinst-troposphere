from troposphere.cloudformation import AWSCustomObject, integer, AWSProperty


class ElastigroupThirdPartiesIntegrationRancher(AWSProperty):
    props = {
        'accessKey': (bool, True),
        'secretKey': (bool, True),
        'masterHost': (bool, True)
    }


class ElastigroupThirdPartiesIntegrationMesosphere(AWSProperty):
    props = {
        'apiServer': (str, True)
    }


class ElastigroupThirdPartiesIntegrationElasticBeanstalkDEploymentPreferencesStrategy(AWSProperty):
    props = {
        'action': (str, True),
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
        'environmentId': (str, True),
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
        'clusterName': (str, True),
        'autoScale': (ElastigroupThirdPartiesIntegrationEcsAutoScale, False)
    }


class ElastigroupThirdPartiesIntegrationMlbRuntime(AWSProperty):
    props = {
        'deploymentId': (str, True)
    }


class ElastigroupThirdPartiesIntegrationKubernetes(AWSProperty):
    props = {
        'apiServer': (str, True),
        'token': (str, True)
    }


class ElastigroupThirdPartiesIntegrationRightScale(AWSProperty):
    props = {
        'accountId': (str, True),
        'refreshToken': (str, True),
        'region': (str, False),
    }


class ElastigroupThirdPartiesIntegrationOpsWorks(AWSProperty):
    props = {
        'layerId': (str, True),
        'stackType': (str, True),
    }


class ElastigroupThirdPartiesIntegrationCodeDeployDeploymentGroups(AWSProperty):
    props = {
        'applicationName': (str, True),
        'deploymentGroupName': (str, True)
    }


class ElastigroupThirdPartiesIntegrationCodeDeploy(AWSProperty):
    props = {
        'deploymentGroups': (ElastigroupThirdPartiesIntegrationCodeDeployDeploymentGroups, True),
        'cleanUpOnFailure': (bool, False),
        'terminateInstanceOnFailure': (bool, False)
    }


class ElastigroupThirdPartiesIntegrationChef(AWSProperty):
    props = {
        'chefServer': (str, True),
        'organization': (str, True),
        'user': (str, True),
        'pemKey': (str, True),
        'chefVersion': (str, True),
    }


class ElastigroupThirdPartiesIntegrationNomad(AWSProperty):
    props = {
        'masterHost': (str, True),
        'masterPort': (integer, True)
    }


class ElastigroupThirdPartiesIntegrationDockerSwarm(AWSProperty):
    props = {
        'masterHost': (str, True),
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
        'instanceType': (str, True),
        'weightedCapacity': (str, True)
    }


class ElastigroupComputeInstanceTypes(AWSProperty):
    props = {
        'ondemand': (str, True),
        'spot': ([str], True),
        'weights': ([ElastigroupComputeInstanceTypeWeight], False)
    }


class ElastigroupComputeAvailabilityZone(AWSProperty):
    props = {
        'name': (str, True),
        'subnetId': (str, False),
        'subnetIds': ([str], False),
        'placementGroupName': (str, False)
    }


class ElastigroupComputeLaunchSpecificationLoadBalancerConfigLoadBalancer(AWSProperty):
    props = {
        'name': (str, False),
        'arn': (str, False),
        'balancerId': (str, False),
        'targetSetId': (str, False),
        'azAwareness': (bool, False),
        'autoWeight': (bool, False),
        'type': (str, True)
    }


class ElastigroupComputeLaunchSpecificationLoadBalancerConfig(AWSProperty):
    props = {
        'loadBalancers': ([ElastigroupComputeLaunchSpecificationLoadBalancerConfigLoadBalancer], False),
    }


class ElastigroupComputeLaunchSpecificationIamRole(AWSProperty):
    props = {
        'name': (str, False),
        'arn': (str, False),
        'iamRole': (str, False)
    }


class ElastigroupComputeLaunchSpecificationBlockDeviceEbs(AWSProperty):
    props = {
        'deleteOnTermination': (bool, False),
        'encrypted': (bool, False),
        'iops': (integer, False),
        'snapshotId': (str, False),
        'volumeSize': (integer, False),
        'volumeType': (str, False)
    }


class ElastigroupComputeLaunchSpecificationBlockDevice(AWSProperty):
    props = {
        'deviceName': (str, False),
        'eb': (ElastigroupComputeLaunchSpecificationBlockDeviceEbs, False),
        'noDevice': (str, False),
        'virtualName': (str, False)
    }


class ElastigroupComputeLaunchSpecificationNetworkInterfacePrivateIpAddress(AWSProperty):
    props = {
        'privateIpAddress': (str, True),
        'primary': (bool, False)
    }


class ElastigroupComputeLaunchSpecificationNetworkInterface(AWSProperty):
    props = {
        'description': (str, False),
        'deviceIndex': (integer, False),
        'secondaryPrivateIpAddressCount': (integer, False),
        'associatePublicIpAddress': (bool, False),
        'deleteOnTermination': (bool, False),
        'groups': ([str], False),
        'networkInterfaceId': (str, False),
        'privateIpAddress': (str, False),
        'privateIpAddresses': ([ElastigroupComputeLaunchSpecificationNetworkInterfacePrivateIpAddress], False),
        'subnetId': (str, False),
        'associateIpv6Address': (bool, False),
    }


class ElastigroupComputeLaunchSpecificationTag(AWSProperty):
    props = {
        'tagKey': (str, False),
        'tagValue': (str, False)
    }


class ElastigroupComputeLaunchSpecification(AWSProperty):
    props = {
        'loadBalancerNames': ([str], False),
        'loadBalancersConfig': (ElastigroupComputeLaunchSpecificationLoadBalancerConfig, False),
        'healthCheckType': (str, False),
        'healthCheckGracePeriod': (integer, False),
        'healthCheckUnhealthyDurationBeforeReplacement': (integer, False),
        'securityGroupIds': ([str], False),
        'monitoring': (bool, False),
        'ebsOptimized': (bool, False),
        'imageId': (str, False),
        'tenancy': (str, False),
        'iamRole': (ElastigroupComputeLaunchSpecificationIamRole, False),
        'keyPair': (str, False),
        'userData': (str, False),
        'shutdownScript': (str, False),
        'blockDeviceMappings': ([ElastigroupComputeLaunchSpecificationBlockDevice], False),
        'networkInterfaces': ([ElastigroupComputeLaunchSpecificationNetworkInterface], False),
        'tags': ([ElastigroupComputeLaunchSpecificationTag], False)

    }


class ElastigroupCompute(AWSProperty):
    props = {
        'elasticIps': ([str], False),
        'instanceTypes': (ElastigroupComputeInstanceTypes, True),
        'product': (str, True),
        'availabilityZones': ([ElastigroupComputeAvailabilityZone], True),
        'launchSpecification': (ElastigroupComputeLaunchSpecification, True),
    }


class ElastigroupCapacity(AWSProperty):
    props = {
        'minimum': (integer, False),
        'maximum': (integer, False),
        'target': (integer, True),
        'unit': (str, True),
    }


class ElastigroupSignals(AWSProperty):
    props = {
        'name': (str, True),
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
        'blockDevicesMode': (str, False),
    }


class ElastigroupStrategy(AWSProperty):
    props = {
        'risk': (integer, False),
        'onDemandCount': (integer, False),
        'utilizeReservedInstances': (bool, False),
        'fallbackToOd': (bool, False),
        'availabilityVsCost': (str, False),
        'drainingTimeout': (integer, False),
        'spinUpTime': (integer, False),
        'lifetimePeriod': (str, False),
        'signals': ([ElastigroupSignals], False),
        'scalingStrategy': (ElastigroupScalingStrategy, False),
        'persistence': (ElastigroupPersistence, False)
    }


class ElastigroupScalingDimension(AWSProperty):
    props = {
        'name': (str, True),
        'value': (str, False)
    }


class ElastigroupScalingUpAction(AWSProperty):
    props = {
        'type': (str, True),
        'adjustment': (str, False),
        'minTargetCapacity': (str, False),
        'target': (str, False),
        'minimum': (str, False),
        'maximum': (str, False),
    }


class ElastigroupScalingUp(AWSProperty):
    props = {
        'action': (ElastigroupScalingUpAction, False),
        'policyName': (str, False),
        'namespace': (str, True),
        'source': (str, False),
        'metricName': (str, True),
        'dimensions': ([ElastigroupScalingDimension], False),
        'statistic': (str, False),
        'extendedStatistic': (str, False),
        'unit': (str, False),
        'threshold': (integer, True),
        'adjustment': (integer, False),
        'minTargetCapacity': (integer, False),
        'period': (integer, False),
        'evaluationPeriods': (integer, False),
        'cooldown': (integer, False),
        'operator': (str, False)
    }


class ElastigroupScalingDownAction(AWSProperty):
    props = {
        'type': (str, True),
        'adjustment': (str, False),
        'minTargetCapacity': (str, False),
        'target': (str, False),
        'minimum': (str, False),
        'maximum': (str, False),
    }


class ElastigroupScalingDown(AWSProperty):
    props = {
        'policyName': (str, False),
        'namespace': (str, True),
        'source': (str, False),
        'metricName': (str, True),
        'dimensions': ([ElastigroupScalingDimension], False),
        'statistic': (str, False),
        'extendedStatistic': (str, False),
        'unit': (str, False),
        'threshold': (integer, True),
        'adjustment': (integer, False),
        'maxTargetCapacity': (integer, False),
        'period': (integer, False),
        'evaluationPeriods': (integer, False),
        'cooldown': (integer, False),
        'action': (ElastigroupScalingDownAction, False),
        'operator': (str, False)
    }


class ElastigroupScaling(AWSProperty):
    props = {
        'up': ([ElastigroupScalingUp], False),
        'down': ([ElastigroupScalingDown], False)
    }


class ElastigroupSchedulingTask(AWSProperty):
    props = {
        'isEnabled': (bool, False),
        'frequency': (str, False),
        'cronExpression': (str, False),
        'taskType': (str, True),
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
        'name': (str, False),
        'description': (str, False),
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
        'ServiceToken': (str, True),
        'accessToken': (str, True),
        'accountId': (str, True),
        'group': (ElastigroupConfig, True)
    }
