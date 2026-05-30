import boto3
import os
from PIL import Image
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):

    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        response = s3.get_object(Bucket=bucket, Key=key)

        image = Image.open(response['Body'])

        resized_image = image.resize((300, 300))

        buffer = io.BytesIO()
        resized_image.save(buffer, "JPEG")
        buffer.seek(0)

        output_bucket = os.environ['OUTPUT_BUCKET']

        s3.put_object(
            Bucket=output_bucket,
            Key='resized-' + key,
            Body=buffer,
            ContentType='image/jpeg'
        )

        return {
            'statusCode': 200,
            'body': 'Success'
        }

    except Exception as e:
        print(str(e))
        return {
            'statusCode': 500,
            'body': str(e)
        }
