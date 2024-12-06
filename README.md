# Cryptocurrency Incremental ETL Pipeline with AWS CDK

The main goal of this project is to develop an incremental Extract, Transform, Load (ETL) solution
utilizing AWS CDK to analyze cryptocurrency data. This will involve constructing a serverless pipeline in
which lambda functions are utilized to retrieve data from an API and stream it into Kinesis streams.
Additionally, we will create another lambda function to consume the data from the Kinesis stream, apply
necessary transformations, and store it in DynamoDB.

To perform data analytics on the incoming data within the Kinesis streams, we will leverage Apache Flink
and Apache Zeppelin. These tools will enable us to extract insights and derive valuable information from
the data. AWS serverless technologies, such as Amazon Lambda and Amazon Glue, will be employed to
efficiently process and transform the data from the three different data sources.
Furthermore, we will utilize Amazon Athena, a query service, to analyze the transformed data stored in
DynamoDB. This will facilitate efficient querying and exploration of the data, enabling us to extract
meaningful insights and make informed decisions based on the cryptocurrency data.
By combining these AWS services and technologies, we aim to create a robust and scalable solution for
analyzing cryptocurrency data, allowing for comprehensive data processing, transformation, and
analytics.

# Project Architecture

![Project Architecture](./resources/git%20push%20-u%20origin%20main.drawio.svg)


## Project Setup

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project. The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory. To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

Create a file called .env with the environment variables needed, make sure to can your own API Key from Alpha Vantage.

```
$ touch .env
$ echo 'INTRADAY_STREAM_NAME=kinesis-crypto-stream-intraday' >> .env
$ echo 'API_KEY=[YOUR_API_KEY]' >> .env
$ echo 'LAMBDA_PRODUCER_NAME=crypto_data_producer' >> .env
$ echo 'LAMBDA_CONSUMER_NAME=crypto_data_consumer' >> .env
$ echo 'DYNAMO_TABLE_NAME=crypto_intraday' >> .env
$ echo 'PRIMARY_BUCKET_NAME=crypto-incremental-project' >> .env
```

In order to install the Alpha Vantage Layer, do the following:

```
$ mkdir -p layers/alpha_vantage_layer/python
$ pip install -t layers/alpha_vantage_layer/python/ urllib3==1.26.16 alpha_vantage
```

## Project Stack
