import os
from amphora.client import AmphoraDataRepositoryClient, Credentials
password=os.getenv("password")
credentials = Credentials(username='JonoPye', password=password)
client = AmphoraDataRepositoryClient(credentials)
amphora = client.get_amphora('ee6120e2-354a-41d6-b347-ad8b1d36b91f')

def uploadfile(path:str):
    s=path.split("/")
    print(s)
    amphora.push_file(path,file_name=s[1])