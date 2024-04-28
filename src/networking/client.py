import requests
  
def upload_image(filename, url):
    files = {'image': open(filename, 'rb')}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        print("Image uploaded successfully")
    else:    
        print(response.text)

if __name__ == '__main__':
    filename = 'img/david_00001.jpg'
    upload_url = 'http://10.49.87.7:5000/upload_image'
    upload_image(filename, upload_url)

