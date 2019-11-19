import requests
import shutil
url = "https://www.gstatic.com/webp/gallery/1.jpg"              #Defining sample Image URL here.
resp = requests.get(url, stream=True)                           #request will get the url content and the stream will return true.
local_file = open('local_image.jpg', 'wb')                      #Now open the URL with write binary (wb) permission.
resp.raw.decode_content = True                                  # Set decode_content value to True, otherwise the downloaded image file's size will be zero
shutil.copyfileobj(resp.raw, local_file)                        # Copy the response stream raw data to local image file.
