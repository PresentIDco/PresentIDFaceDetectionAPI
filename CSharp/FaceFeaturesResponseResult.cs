public class FaceFeaturesResponseResult
{
    public bool hasError { set; get; }
    public int StatusCode { set; get; }
    public string StatusMessage { set; get; }
    public List<FaceDetectionResult> Faces { set; get; }
}

public class FaceDetectionResult
{
    public string faceID { set; get; }
    public int status { set; get; }
    public string statusMessage { set; get; }
    public Rect rectangle { set; get; }
    public AgeBoundary age { set; get; }
    public Gender gender { set; get; }
    public List<FaceLanMark> faceLandMarks { set; get; }
    public Blureness blur { set; get; }
    public int rotateAngel { set; get; }
}

public class Rect
{
    public Dot lb { set; get; }
    public Dot lt { set; get; }
    public Dot rb { set; get; }
    public Dot rt { set; get; }
}

public class Gender
{
    public int index { set; get; }
    public string title { set; get; }
}

public class Emotion
{
    public int Index { set; get; }
    public string Title { set; get; }
    public double Prob { set; get; }
}

public class AgeBoundary
{
    public int minAge { set; get; }
    public int maxAge { set; get; }
}

public class FaceLanMark
{
    public string title { set; get; }
    public int x { set; get; }
    public int y { set; get; }
}

public class HeadPose
{
    public double Pitch { set; get; }
    public double Roll { set; get; }
    public double Yaw { set; get; }
}

public class Blureness
{
    public string level { set; get; }
    public double value { set; get; }
}

public class Dot
{
    public int x { set; get; }
    public int y { set; get; }
}