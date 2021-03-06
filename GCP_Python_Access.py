"""Programatically interact with a Google Cloud Storage bucket."""
from google.cloud import storage
from os import environ

#Create and Delete bucket
create_bucket('my_bucket_name') #creates a new bucket with the given name.
bucket.delete() #deletes an existing bucket.

# Data
localFolder = r'/content/drive/MyDrive/ColabNotebooks/PDFFiles/'

storage_client = storage.Client()
bucket = storage_client.get_bucket('eattachments')
print(bucket)


#Upload Files
from os import listdir
from os.path import isfile, join

...

def upload_files(bucketName):
    """Upload files to GCP bucket."""
    files = [f for f in listdir(localFolder) if isfile(join(localFolder, f))]
    for file in files:
        localFile = localFolder + file
        blob = bucket.blob(file)
        blob.upload_from_filename(localFile)
    return f'Uploaded {files} to "{bucketName}" bucket.'



#ListFiles
def list_files(bucketName):
    """List all files in GCP bucket."""
    files = bucket.list_blobs()
    fileList = [file.name for file in files if '.' in file.name]
    return fileList


#Download Files
from random import randint

def download_random_file(bucketName, localFolder):
    """Download random file from GCP bucket."""
    fileList = list_files(bucketName)
    for files in range(len(fileList)):
      blob = bucket.blob(fileList[files])
      fileName = blob.name.split('/')[-1]
      blob.download_to_filename(localFolder + fileName)
    return f'{fileList} downloaded from bucket.'

#Delete Files
def delete_file(bucketName):
    """Delete file from GCP bucket."""
    fileList = list_files(bucketName)
    for files in range(len(fileList)):
      bucket.delete_blob(fileList[files])
    return f'{fileList} deleted from bucket.'


