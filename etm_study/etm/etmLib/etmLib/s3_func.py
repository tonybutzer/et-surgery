import os
import boto3

def s3_hello(person_name):
    print('Hello There Person:', person_name)

def s3_push_delete_local(local_file, bucket, bucket_filepath):
        out_bucket = return_my_bucket(bucket_filepath)
        a = bucket_filepath.split('/')
        bucket_filepath = '/'.join(a[1:]) # strip bucket from path
        print('PUSH', out_bucket, bucket_filepath)
        s3 = boto3.client('s3')
        with open(local_file, "rb") as f:
            s3.upload_fileobj(f, out_bucket, bucket_filepath)
        os.remove(local_file)

def return_s3_list(working_bucket, prefix):
        aws_list = []
        s3 = boto3.resource('s3')
        bucket_name = working_bucket
        bucket = s3.Bucket(bucket_name)
        for obj in bucket.objects.filter(Prefix=prefix):
            obj_key = obj.key
            obj_key = working_bucket + '/' + obj_key
            aws_list.append((obj_key, obj.size))
        return aws_list


def return_my_bucket(prefix_with_slash):
    a = prefix_with_slash.split('/')
    print('a=',a)
    THE_BUCKET=a[0]
    print("the BUCKET=",THE_BUCKET)
    return THE_BUCKET


def s3_list_pseudo_subdirs(prefix_with_slash):


    bucket = return_my_bucket(prefix_with_slash)
    subfolder_list = []
    #Make sure you provide / in the end

    a = prefix_with_slash.split('/')
    prefix_with_slash='/'.join(a[1:])
    prefix = prefix_with_slash 
    
    print('prefix_with_slash', prefix_with_slash)

    client = boto3.client('s3')
    result = client.list_objects(Bucket=bucket, Prefix=prefix, Delimiter='/')
    for o in result.get('CommonPrefixes'):
        #print ('sub folder : ', o.get('Prefix'))
        subfolder_list.append(o.get('Prefix'))
    return subfolder_list,bucket




