import os
import boto3
from dotenv import load_dotenv


class AwsManager :
    load_dotenv(verbose=True)
    bucket_name = 'analyzed-images-bucket'

    def aws_session(region_name='us-east-1'):
        return boto3.session.Session(aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                    aws_secret_access_key=os.getenv('AWS_ACCESS_KEY_SECRET'),
                                    region_name=region_name)
    def make_bucket(name, acl):
        session = aws_session()
        s3_resource = session.resource('s3')
        return s3_resource.create_bucket(Bucket='analyzed-images-bucket', ACL='public-read')

    def upload_file_to_bucket(bucket_name, file_path):
        session = aws_session()
        s3_resource = session.resource('s3')
        file_dir, file_name = os.path.split(file_path)

        bucket = s3_resource.Bucket(bucket_name)
        bucket.upload_file(
          Filename=file_path,
          Key=file_name,
          ExtraArgs={'ACL': 'public-read'}
        )

        s3_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
        return s3_url

    def download_file_from_bucket(bucket_name, s3_key, dst_path):
        session = aws_session()
        s3_resource = session.resource('s3')
        bucket = s3_resource.Bucket(bucket_name)
        bucket.download_file(Key=s3_key, Filename=dst_path)



    # S3 버켓을 생성하는 코드, 최초 한번만 쓰면 됨
    # s3_bucket = make_bucket('analyzed-images-bucket', 'public-read')


    s3_url = upload_file_to_bucket(bucket_name, 'static/Images/figure-aws.png')
    print('Log : file is uploaded completely.',s3_url)

    download_file_from_bucket(bucket_name, 'children.csv', 'children_download.csv')
    with open('children_download.csv') as fo:
        print(fo.read())
