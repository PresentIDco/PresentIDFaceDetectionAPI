# HiBrainyAPIs - Face Detection
The Face Detection Web Service is called Restful and in the post method. The parameters and input files are sent to the API in the form of Multi-part Form. The service output is returned in Json format.

## Output Template
```
{
  'hasError': bool, 
  'statusCode': int,
  'statusMessage': string, 
  'data': 
  [
    {
      'faceID': string, 
      'status': int, 
      'statusMessage': string, 
      'rectangle': 
        {
          'lb': {'x': int, 'y': int}, 
          'lt': {'x': int, 'y': int}, 
          'rb': {'x': int, 'y': int}, 
          'rt': {'x': int, 'y': int}
        }, 
      'age': {'minAge': int, 'maxAge': int}, 
      'gender': {'index': int, 'title': string}, 
      'faceLandMarks': 
        [
	  {'title': 'CenterRightEye', 'x': int, 'y': int}, 
	  {'title': 'CenterLeftEye', 'x': int, 'y': int}, 
	  {'title': 'NoseTip', 'x': int, 'y': int}, 
	  {'title': 'LipsRightCorner', 'x': int, 'y': int}, 
	  {'title': 'LipsLeftCorner', 'x': int, 'y': int}
	], 
      'blur': {'level': string, 'value': float}, 
      'rotateAngel': int
    }
  ]
}
```

## Languages
  * [Python](#python)
  * [C#](#csharp)

## Python

### Prerequisites
  [requests](https://pypi.org/project/requests/) python package

#### Installation
To install [requests](https://pypi.org/project/requests/), simply:
 ```
 $ pip install requests
 ```

### Usage
The python sample code is [Here](Python/FaceDetection.py).  

* Give your API Key from [rapidapi](https://rapidapi.com/HiBrainy/api/face-recognition4) and assign 'api_key' variable. 

  ```python
  api_key = 'Your API Key'
  ```
* Assign the variables `image_path` and `image_name`, by image path and image name.  
  ```python
  image_path = 'Image directory path'
  image_name = 'Image name'
  ```

## CSharp  
### Prerequisites
 [Newtonsoft.Json](https://www.nuget.org/packages/Newtonsoft.Json/) framework for .NET    

#### Installation
Run this command in the Package Manager Console:  
``` 
Install-Package Newtonsoft.Json
```

### Usage
 * Add `FaceFeaturesResponseResult.cs` class in your project, with following "using" statements.  
   ```c#
   using System;
   using System.Collections.Generic;
   ```
   [Here](CSharp/FaceFeaturesResponseResult.cs) is the content of the `FaceFeaturesResponseResult.cs` class. 

 * Add `HiBrainyFaceDetectionAPI.cs` class in your project, with following "using" statements.  
   ```c#
   using Newtonsoft.Json;
   using System;
   using System.Collections.Generic;
   using System.IO;
   using System.Linq;
   using System.Net.Http;
   using System.Threading.Tasks;
   ```
   [Here](CSharp/HiBrainyFaceDetectionAPI.cs) is the content of the `HiBrainyFaceDetectionAPI.cs` class.
  
  * Create "HiBrainyFaceDetectionAPI" class Instance. You can get all the features through below:
    
    ```c#
	string apiKey = "Your API Key";
	HiBrainyFaceDetectionAPI faceDetection = new HiBrainyFaceDetectionAPI(apiKey);
	var detectionResult = faceDetection.FaceDetectionAsync("Path to image").Result;

	Console.WriteLine("Has error: " + detectionResult.hasError);
	Console.WriteLine("Status Code: " + detectionResult.statusCode);
	Console.WriteLine("Status Message: " + detectionResult.statusMessage);

	for (int i = 0; i<detectionResult.data.Count; i++)
	{
	    Console.WriteLine("\nFace " + i + 1 + " Information:");
	    Console.WriteLine("Face ID: " + detectionResult.data[i].faceID);
	    Console.WriteLine("Status: " + detectionResult.data[i].status);
	    Console.WriteLine("Status Message: " + detectionResult.statusMessage);

	    Console.WriteLine("\nRectangle");
	    Console.WriteLine("LeftBottom " + " X:" + detectionResult.data[i].rectangle.lb.x + " Y:" + detectionResult.data[i].rectangle.lb.y);
	    Console.WriteLine("LeftRight " + " X:" + detectionResult.data[i].rectangle.lt.x + " Y:" + detectionResult.data[i].rectangle.lt.y);
	    Console.WriteLine("RightTop " + " X:" + detectionResult.data[i].rectangle.rt.x + " Y:" + detectionResult.data[i].rectangle.rt.y);
	    Console.WriteLine("RightBottom " + " X:" + detectionResult.data[i].rectangle.rb.x + " Y:" + detectionResult.data[i].rectangle.rb.y);

	    Console.WriteLine("\nAge: " + detectionResult.data[i].age.minAge + "~" + detectionResult.data[i].age.maxAge);
	    Console.WriteLine("Gender: " + detectionResult.data[i].gender.title);

	    Console.WriteLine("\nFaceLandMarks:");
	    foreach (FaceLanMark item in detectionResult.data[i].faceLandMarks)
	    {
		Console.WriteLine(item.title + " X:" + item.x + " Y:" + item.y);
	    }

	    Console.WriteLine("\nImage Blureness Level: " + detectionResult.data[i].blur.level);
	    Console.WriteLine("Image Blureness Value: " + detectionResult.data[i].blur.value);
	    Console.WriteLine("\nRotate Angle: " + detectionResult.data[i].rotateAngel);
	}
    ```
	Give your API Key from [rapidapi](https://rapidapi.com/HiBrainy/api/face-recognition4) and assign apiKey variable.
