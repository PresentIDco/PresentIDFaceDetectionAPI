public class HiBrainyFaceDetectionAPI
{
	string apiKey;

	public HiBrainyFaceDetectionAPI(string apiKey)
	{
		this.apiKey = apiKey;
	}

	public async Task<FaceFeaturesResponseResult> FaceDetectionAsync(string FileName)
	{
		var content = new MultipartFormDataContent();
		var response = new HttpResponseMessage();
		string apiUrl = "https://face-recognition4.p.rapidapi.com/FaceDetection";
		FaceFeaturesResponseResult Faces = new FaceFeaturesResponseResult();
		try
		{
			content.Headers.Add("x-rapidapi-host", "face-recognition4.p.rapidapi.com");
			content.Headers.Add("x-rapidapi-key", apiKey);
			content.Add(new ByteArrayContent(File.ReadAllBytes(FileName)), "Photo", FileName.Split('\\').LastOrDefault());
		}
		catch (Exception ex) { throw new Exception(ex.Message); }
		try
		{
			using (var http = new HttpClient())
			{
				response = await http.PostAsync(apiUrl, content);
			}
			string resMessage = await response.Content.ReadAsStringAsync();
			if (response.IsSuccessStatusCode)
			{
				Faces = JsonConvert.DeserializeObject<FaceFeaturesResponseResult>(resMessage);
				return Faces;
			}
			else
			{ throw new Exception(resMessage); }
		}
		catch (Exception ex) { throw new Exception(ex.Message); }
	}
}