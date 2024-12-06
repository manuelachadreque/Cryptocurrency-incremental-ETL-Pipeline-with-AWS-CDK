from aws_cdk import Stack, aws_kinesis as kinesis, Duration
from constructs import Construct
from decouple import config
from aws_cdk import aws_lambda as _lambda





INTRADAY_STREAM_NAME = config("INTRADAY_STREAM_NAME")

class KinesisStreamStack(Stack):
    def __init__(self, scope:Construct, construct_id:str,**kwargs) ->None:
        super().__init__(scope, construct_id, **kwargs)

        self.intraday_stream = kinesis.Stream(
            self,
            "intraday_stream",
            stream_name=INTRADAY_STREAM_NAME,
            shard_count=1,
            retention_period=Duration.hours(24)
        )
