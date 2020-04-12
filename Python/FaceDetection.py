import requests


api_url = 'http://api.hibrainy.com/api/v1/Face/FaceAllFeatures'
api_key = 'Your API Key'

image_path = 'Image directory path'
image_name = 'Image name'

files = {'Photo': (image_name, open(image_path + image_name, 'rb'), 'multipart/form-data')}
header = {'API-Key': api_key}
response = requests.post(api_url, files=files, headers=header)

print('Has error:', response.json()['hasError'])
print('Status Code:', response.json()['StatusCode'])
print('Status Message:', response.json()['StatusMessage'])

for i in range(0, len(response.json()['Faces'])):
    print('\nFace', i + 1, 'Information:')
    print('Face ID', response.json()['Faces'][i]['faceID'])
    print('Status', response.json()['Faces'][i]['status'])
    print('Status Message', response.json()['Faces'][i]['statusMessage'])

    print('\nRectangle')
    print('LeftBottom', 'X:', response.json()['Faces'][i]['rectangle']['lb']['x'],
          'Y:', response.json()['Faces'][i]['rectangle']['lb']['y'])
    print('LeftTop', 'X:', response.json()['Faces'][i]['rectangle']['lt']['x'],
          'Y:', response.json()['Faces'][i]['rectangle']['lt']['y'])
    print('LeftTop', 'X:', response.json()['Faces'][i]['rectangle']['rb']['x'],
          'Y:', response.json()['Faces'][i]['rectangle']['rb']['y'])
    print('LeftTop', 'X:', response.json()['Faces'][i]['rectangle']['rt']['x'],
          'Y:', response.json()['Faces'][i]['rectangle']['rt']['y'])

    print('\nAge:', response.json()['Faces'][i]['age']['minAge'], '~', response.json()['Faces'][i]['age']['maxAge'])
    print('Gender:', response.json()['Faces'][i]['gender']['title'])

    print('\nFaceLandMark')
    for land_mark in range(0, len(response.json()['Faces'][i]['faceLandMarks'])):
        print(response.json()['Faces'][i]['faceLandMarks'][land_mark]['title'],
              'X:', response.json()['Faces'][i]['faceLandMarks'][land_mark]['x'],
              'Y:', response.json()['Faces'][i]['faceLandMarks'][land_mark]['y'])

    print('\nImage Blureness Level:', response.json()['Faces'][i]['blur']['level'])
    print('Image Blureness Value:', response.json()['Faces'][i]['blur']['value'])

    print('\nRotate Angle:', response.json()['Faces'][i]['rotateAngel'], '\n')
