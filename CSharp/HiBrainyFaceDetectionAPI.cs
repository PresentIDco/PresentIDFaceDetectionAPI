public class PresentIDFaceDetectionAPI
{
	string apiKey;

	public PresentIDFaceDetectionAPI(string apiKey)
	{
		this.apiKey = apiKey;
	}

	public async Task<FaceFeaturesResponseResult> FaceDetectionAsync(string FileName)
	{
		var content = new MultipartFormDataContent();
		var response = new HttpResponseMessage();
		string apiUrl = "http://api.hibrainy.com/api/v1/Face/FaceAllFeatures";
		FaceFeaturesResponseResult faces = new FaceFeaturesResponseResult();
		try
		{
			content.Headers.Add("API-Key", apiKey);
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
				faces = JsonConvert.DeserializeObject<FaceFeaturesResponseResult>(resMessage);
				return faces;
			}
			else
			{ throw new Exception(resMessage); }
		}
		catch (Exception ex) { throw new Exception(ex.Message); }
	}
}
