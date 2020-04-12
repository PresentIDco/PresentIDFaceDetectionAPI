import requests


api_url = 'https://face-recognition4.p.rapidapi.com/FaceDetection'
api_key = 'Your API Key'

image_path = 'Image directory path'
image_name = 'Image name'

files = {'Photo': (image_name, open(image_path + image_name, 'rb'), 'multipart/form-data')}
header = {
    "x-rapidapi-host": "face-recognition4.p.rapidapi.com",
    "x-rapidapi-key": api_key
    }
response = requests.post(api_url, files=files, headers=header)

print('Has error:', response.json()['hasError'])
print('Status Code:', response.json()['statusCode'])
print('Status Message:', response.json()['statusMessage'])

for i in range(0, len(response.json()['data'])):
    print('\nFace', i + 1, 'Information:')
    print('Face ID', response.json()['data'][i]['faceID'])
    print('Status', response.json()['data'][i]['status'])
    print('Status Message', response.json()['data'][i]['statusMessage'])

    print('\nRectangle')
    print('LeftBottom', 'X:', response.json()['data'][i]['rectangle']['lb']['x'],
          'Y:', response.json()['data'][i]['rectangle']['lb']['y'])
    print('LeftTop', 'X:', response.json()['data'][i]['rectangle']['lt']['x'],
          'Y:', response.json()['data'][i]['rectangle']['lt']['y'])
    print('RightBottom', 'X:', response.json()['data'][i]['rectangle']['rb']['x'],
          'Y:', response.json()['data'][i]['rectangle']['rb']['y'])
    print('RightTop', 'X:', response.json()['data'][i]['rectangle']['rt']['x'],
          'Y:', response.json()['data'][i]['rectangle']['rt']['y'])

    print('\nAge:', response.json()['data'][i]['age']['minAge'], '~', response.json()['data'][i]['age']['maxAge'])
    print('Gender:', response.json()['data'][i]['gender']['title'])

    print('\nFaceLandMark')
    for land_mark in range(0, len(response.json()['data'][i]['faceLandMarks'])):
        print(response.json()['data'][i]['faceLandMarks'][land_mark]['title'],
              'X:', response.json()['data'][i]['faceLandMarks'][land_mark]['x'],
              'Y:', response.json()['data'][i]['faceLandMarks'][land_mark]['y'])

    print('\nImage Blureness Level:', response.json()['data'][i]['blur']['level'])
    print('Image Blureness Value:', response.json()['data'][i]['blur']['value'])

    print('\nRotate Angle:', response.json()['data'][i]['rotateAngel'] + '\n')

