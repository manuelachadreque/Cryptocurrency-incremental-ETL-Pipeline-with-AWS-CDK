#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import Tags

from kinesis_stream.kinesis_stream_stack import KinesisStreamStack
from data_consumer.data_consumer_stack import DataconsumerStack
from data_producer.data_producer_stack import DataProducerStack
from S3_bucket.s3_bucket_stack import S3BucketStack




env_LONDON   =cdk.Environment(account="430118814763", region="eu-west-2")

app = cdk.App()

kinesis_stream = KinesisStreamStack(app, "KinesisStreamStack", env=env_LONDON)
data_producer = DataProducerStack(app, "DataProducerStack", env=env_LONDON)
data_consumer = DataconsumerStack(app, "DataConsumerStack", env=env_LONDON)
s3_bucket = S3BucketStack(app, "S3BucketStack", env=env_LONDON)

Tags.of(app).add("ProjectOwner", "Manuela-Chadreque")
Tags.of(app).add("ProjectName", "Crypto_incremental_Pipeline")
app.synth()
