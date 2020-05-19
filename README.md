# HiBrainy - Face Detection API Documentation
The HiBrainy Face Detection API is organized around RESTful and is called through post method. The parameters and input files are sent to the API in the form of Multipart Form. The service output is returned in JSON format.

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
  * [Java](#java)

## Python

### Prerequisites
 - Face Recognition API-Key
    - You can get a free trial API-Key by creating your free account from [HiBrainy.com](https://my.hibrainy.com/home/signup). Login to your account, click on Tokens and get your Face Recognition API-Key.
    
 - [Requests](https://pypi.org/project/requests/) python package
    - To install [requests](https://pypi.org/project/requests/), simply:
   ```
   $ pip install requests
   ```

### Usage
The python sample code is [Here](Python/FaceDetection.py).  

* Assign the variable `api_key` by API-Key you took from [your account](https://my.hibrainy.com).

  ```python
  api_key = 'Your API-Key'
  ```
* Assign the variables `image_path` and `image_name`, by image path and image name.  
  ```python
  image_path = 'Image directory path'
  image_name = 'Image name'
  ```

## CSharp  

### Prerequisites
 - Face Recognition API-Key
    - You can get a free trial API-Key by creating your free account from [HiBrainy.com](https://my.hibrainy.com/home/signup). Login to your account, click on Tokens and get your Face Recognition API-Key.
    
 - [Newtonsoft.Json](https://www.nuget.org/packages/Newtonsoft.Json/) framework for .NET 
    - Run this command in the Package Manager Console:  
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
	string apiKey = "Your API-Key";
	HiBrainyFaceDetectionAPI faceDetection = new HiBrainyFaceDetectionAPI(apiKey);
	var detectionResult = faceDetection.FaceDetectionAsync("Path to image").Result;

	Console.WriteLine("Has error: " + detectionResult.hasError);
	Console.WriteLine("Status Code: " + detectionResult.StatusCode);
	Console.WriteLine("Status Message: " + detectionResult.StatusMessage);

	for (int i = 0; i < detectionResult.Faces.Count; i++)
	{
		Console.WriteLine("\nFace " + i + 1 + " Information:");
		Console.WriteLine("Face ID: " + detectionResult.Faces[i].faceID);
		Console.WriteLine("Status: " + detectionResult.Faces[i].status);
		Console.WriteLine("Status Message: " + detectionResult.StatusMessage);

		Console.WriteLine("\nRectangle");
		Console.WriteLine("LeftBottom " + " X:" + detectionResult.Faces[i].rectangle.lb.x + " Y:" + detectionResult.Faces[i].rectangle.lb.y);
		Console.WriteLine("LeftRight " + " X:" + detectionResult.Faces[i].rectangle.lt.x + " Y:" + detectionResult.Faces[i].rectangle.lt.y);
		Console.WriteLine("RightTop " + " X:" + detectionResult.Faces[i].rectangle.rt.x + " Y:" + detectionResult.Faces[i].rectangle.rt.y);
		Console.WriteLine("RightBottom " + " X:" + detectionResult.Faces[i].rectangle.rb.x + " Y:" + detectionResult.Faces[i].rectangle.rb.y);

		Console.WriteLine("\nAge: " + detectionResult.Faces[i].age.minAge + "~" + detectionResult.Faces[i].age.maxAge);
		Console.WriteLine("Gender: " + detectionResult.Faces[i].gender.title);

		Console.WriteLine("\nFaceLandMarks:");
		foreach (FaceLanMark item in detectionResult.Faces[i].faceLandMarks)
		{
			Console.WriteLine(item.title + " X:" + item.x + " Y:" + item.y);
		}
		
		Console.WriteLine("\nImage Blureness Level: " + detectionResult.Faces[i].blur.level);
		Console.WriteLine("Image Blureness Value: " + detectionResult.Faces[i].blur.value);
		Console.WriteLine("\nRotate Angle: " + detectionResult.Faces[i].rotateAngel);
	}
    ```
  	Assign the variable `apiKey` by API-Key you took from [your account](https://my.hibrainy.com).


## Java

### Prerequisites
 - Face Recognition API-Key
    - You can get a free trial API-Key by creating your free account from [HiBrainy.com](https://my.hibrainy.com/home/signup). Login to your account, click on Tokens and get your Face Recognition API-Key.
    
 - [OkHttp package](https://github.com/square/okhttp/) package  

### Usage
 * Add `FaceFeaturesResponseResult` class in your project.  
   [Here](Java/FaceFeaturesResponseResult.java) is the content of the `FaceFeaturesResponseResult.java` class. 

 * Add following "import" statements to your project.  
   ```java
    import com.fasterxml.jackson.databind.ObjectMapper;
    import okhttp3.*;
    import java.io.File;
    import java.util.HashMap;
   ```
 * You can get all the features through below:

    ```java
    String apiURL = "http://api.hibrainy.com/api/v1/Face/FaceAllFeatures";
    String apiKey = "Your API-Key";
    String imagePath = "Path to image file";
    String imageName = "Image name"; 
    File file = new File(imagePath + imageName);
    byte[] fileContent = new byte[(int) file.length()];

    OkHttpClient client = new OkHttpClient();
    Request request = new Request.Builder()
                .url(apiURL)
                .post(RequestBody.create(MediaType.get("multipart/form-data"), fileContent))
                .header("API-Key", apiKey)
                .build();

    Call call = client.newCall(request);
    Response response = call.execute();
    ObjectMapper mapper = new ObjectMapper();
        
    FaceFeaturesResponseResult faceDetection = mapper.readValue(response.body().string(), FaceFeaturesResponseResult.class);
    System.out.println("Has Error: " + faceDetection.gethasError());
    System.out.println("Status Code: " + faceDetection.getStatusCode());
    System.out.println("Status Message: " + faceDetection.getStatusMessage());          
    System.out.println("FaceID:" + faceDetection.getFaceID());
    System.out.println("Status:" + faceDetection.getStatus());
    System.out.println("StatusMessage:" + faceDetection.getstatusMessage());

    System.out.println("Rectangle:");
    int [] lb = faceDetection.getlb();
    int [] lt = faceDetection.getlt();
    int [] rb = faceDetection.getrb();
    int [] rt = faceDetection.getrt();
    System.out.print("Left Bottom: "+Integer.toString(lb[0])+','+Integer.toString(lb[1]));
    System.out.print("Left Top: "+Integer.toString(lt[0])+','+Integer.toString(lt[1]));
    System.out.print("Right Bottom: "+Integer.toString(rb[0])+','+Integer.toString(rb[1]));
    System.out.print("Right Top: "+Integer.toString(rt[0])+','+Integer.toString(rt[1]));

    System.out.print("Age:\n" +Integer.toString(faceDetection.getminAge())+
			" ~ "+Integer.toString(faceDetection.getmaxAge()));
    System.out.println("Gender:" + faceDetection.gettitle());

    System.out.println("\nFaceLandMark:");
    int [] cr = faceDetection.getCenterRightEye();
    int [] cl = faceDetection.getCenterLeftEye();
    int [] np = faceDetection.getNoseTip();
    int [] lr = faceDetection.getLipsRightCorner();
    int [] ll = faceDetection.getLipsLeftCorner();
    System.out.print("CenterRightEye: "+Integer.toString(cr[0])+','+Integer.toString(cr[1])+"\n");
    System.out.print("CenterLeftEye: "+Integer.toString(cl[0])+','+Integer.toString(cl[1])+"\n");
    System.out.print("NoseTip: "+Integer.toString(np[0])+','+Integer.toString(np[1])+"\n");
    System.out.print("LipsRightCorner: "+Integer.toString(lr[0])+','+Integer.toString(lr[1])+"\n");
    System.out.print("LipsLeftCorner: "+Integer.toString(ll[0])+','+Integer.toString(ll[1])+"\n");
    System.out.print("Image Blureness Level: "+ faceDetection.getblur()+"\tImage Blureness Value: "+Float.toString(faceDetection.getvalue()));
    ```

      Assign the variable `apiKey` by API-Key you took from [your account](https://my.hibrainy.com).
