from troposphere import Template

from aws_elastigroup import Elastigroup, ElastigroupConfig, ElastigroupCapacity, ElastigroupStrategy;
from aws_elastigroup import ElastigroupCompute, ElastigroupComputeInstanceTypes
from aws_elastigroup import ElastigroupComputeAvailabilityZone, ElastigroupComputeLaunchSpecification, \
    ElastigroupScalingDown, ElastigroupScalingDownAction
from aws_elastigroup import ElastigroupScaling
from aws_elastigroup import ElastigroupScheduling, ElastigroupComputeLaunchSpecificationTag, ElastigroupScalingUpAction;
from aws_elastigroup import ElastigroupThirdPartiesIntegration, ElastigroupSchedulingTask, \
    ElastigroupThirdPartiesIntegrationEcs, \
    ElastigroupThirdPartiesIntegrationEcsAutoScale, ElastigroupThirdPartiesIntegrationMlbRuntime, ElastigroupScalingUp, \
    ElastigroupPersistence;

t = Template()

t.add_description(
    "Create elastigroup through a Cloudformation custom resource"
)

# Create elastigroup
beanstalk_elastigroup = t.add_resource(
    Elastigroup("SpotinstElastigroup",
                ServiceToken="arn:aws:lambda:us-west-2:178579023202:function:spotinst-cloudformation",
                accessToken="spotinst-access-token",
                accountId="account-id",
                group=ElastigroupConfig(
                    name='group-name',
                    description="group-description",
                    capacity=ElastigroupCapacity(
                        minimum=2,
                        maximum=4,
                        target=3,
                        unit="instance"
                    ),
                    strategy=ElastigroupStrategy(
                        risk=100,
                        availabilityVsCost="balanced",
                        drainingTimeout=120,
                        fallbackToOd=True,
                        utilizeReservedInstances=True,
                        lifetimePeriod="days",
                        persistence=ElastigroupPersistence(
                            blockDevicesMode="onLaunch",
                            shouldPersistRootDevice=True,
                            shouldPersistBlockDevices=True,
                            shouldPersistPrivateIp=False
                        ),
                    ),
                    scaling=ElastigroupScaling(
                        up=[ElastigroupScalingUp(
                            policyName="up Scaling Policy 1",
                            metricName="CPUUtilization",
                            statistic="average",
                            unit="percent",
                            threshold=68,
                            action=ElastigroupScalingUpAction(
                                type="adjustment",
                                adjustment="1"
                            ),
                            namespace="AWS/EC2",
                            period=300,
                            evaluationPeriods=3,
                            cooldown=300,
                            operator="gte"

                        )],
                        down=[
                            ElastigroupScalingDown(
                                policyName="down Scaling Policy 1",
                                metricName="CPUUtilization",
                                statistic="average",
                                unit="percent",
                                threshold=40,
                                action=ElastigroupScalingDownAction(
                                    type="adjustment",
                                    adjustment="1"
                                ),
                                namespace="AWS/EC2",
                                period=300,
                                evaluationPeriods=3,
                                cooldown=300,
                                operator="lte"
                            )

                        ]

                    ),

                    scheduling=ElastigroupScheduling(
                        tasks=[
                            ElastigroupSchedulingTask(
                                taskType="scaleUp",
                                cronExpression="0 0 12 1/1 * ? *",
                                isEnabled=True,
                                adjustment=1
                            )
                        ]

                    ),
                    thirdPartiesIntegration=ElastigroupThirdPartiesIntegration(
                        ecs=ElastigroupThirdPartiesIntegrationEcs(
                            clusterName="cluster-name",
                            autoScale=ElastigroupThirdPartiesIntegrationEcsAutoScale(
                                isEnabled=False
                            )
                        ),
                        mlbRuntime=ElastigroupThirdPartiesIntegrationMlbRuntime(
                            deploymentId="dp-123456"
                        ),
                    ),
                    compute=ElastigroupCompute(
                        instanceTypes=ElastigroupComputeInstanceTypes(
                            ondemand="c4.large",
                            spot=[
                                "m3.large",
                                "m4.xlarge",
                                "m3.xlarge",
                                "m4.large"
                            ],
                        ),
                        product="Linux/UNIX",
                        availabilityZones=[
                            ElastigroupComputeAvailabilityZone(
                                name="us-west-2a",
                                subnetIds=[
                                    "subnet-123456"
                                ],
                            )],
                        launchSpecification=ElastigroupComputeLaunchSpecification(
                            userData="IyEvYmluL2Jhc2gKeXVtIHVwZGF0ZSAteQ==",
                            shutdownScript="IyEvYmluL2Jhc2gKeXVtIHVwZGF0ZSAteQ==",

                            securityGroupIds=["sg-123456"],
                            monitoring=True,
                            ebsOptimized=True,
                            imageId="ami-123456",
                            tags=[
                                ElastigroupComputeLaunchSpecificationTag(
                                    tagKey="tag-key",
                                    tagValue="tag-value"
                                ),

                            ],
                            healthCheckType="health-check-type",
                            healthCheckGracePeriod=360,
                            healthCheckUnhealthyDurationBeforeReplacement=360,
                            tenancy="default"
                        )
                    )
                )))

print(t.to_json())
