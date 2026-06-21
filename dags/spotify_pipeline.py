# airflow dag orchestration 

from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.amazon.aws.operators.lambda_function import LambdaInvokeFunctionOperator 
from airflow.providers.amazon.aws.operators.glue_crawler import GlueCrawlerOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'spotify_cloud_pipeline',
    default_args=default_args,
    description='Triggers the cloud Lambda function from local Airflow',
    schedule='@weekly',  
    catchup=False
) as dag:
    # Node 1: Triggers the Lambda function (API -> S3)
    trigger_lambda_extract = LambdaInvokeFunctionOperator(  
        task_id='trigger_spotify_lambda',
        function_name='spotify_api_extraction',  
        invocation_type='RequestResponse',
        aws_conn_id='aws_default',  
    )
    # Node 2: Triggers the Glue Crawler to update the virtual map
    trigger_glue_crawler = GlueCrawlerOperator(
        task_id='trigger_spotify_glue_crawler',
        config={'Name': 'spotify_raw_crawler'},  
        aws_conn_id='aws_default',
    )

    trigger_lambda_extract >> trigger_glue_crawler
   