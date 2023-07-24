#!/usr/bin/env python3
import requests

url = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230724T234001Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=26f396bbca0bc4bf1ca48c909aa99004fc37ee7fd50b0bc3be35d2b255982707"
response = requests.get(url)

if response.status_code == 200:
    with open("Popular_Baby_Names.csv", "wb") as f:
        f.write(response.content)
else:
    print("Error downloading data.")

