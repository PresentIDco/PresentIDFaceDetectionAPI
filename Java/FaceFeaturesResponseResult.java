public class FaceFeaturesResponseResult {
    //Connection Status
    boolean hasError;
    int StatusCode;
    String StatusMessage;
    ///Faces
    String FaceID;
    int Status;
    String statusMessage;
    int []lb;
    int []lt;
    int []rb;
    int []rt;
    ///Age
    int minAge;
    int maxAge;
    ///Gender
    int index;
    String title;
    ////faceLandMarks////
    int []CenterRightEye;
    int []CenterLeftEye;
    int []NoseTip;
    int []LipsRightCorner;
    int []LipsLeftCorner;
    String blur;
    float value;
    int rotateAngel;

    public boolean gethasError() {
        return hasError;
    }

    public void sethasError(boolean hasError) {
        this.hasError = hasError;
    }
    
    
    public int getStatusCode() {
        return StatusCode;
    }

    public void setStatusCode(int StatusCode) {
        this.StatusCode = StatusCode;
    }
        
     public String getStatusMessage() {
        return StatusMessage;
    }

    public void setStatusMessage(String StatusMessage) {
        this.StatusMessage = StatusMessage;
    }
        
    public String getFaceID() {
        return FaceID;
    }

    public void setFaceID(String id) {
        this.FaceID = id;
    }

    public int getStatus() {
        return Status;
    }

    public void setStatus(int  Status) {
        this.Status = Status;
    }
    

    public String getstatusMessage() {
        return StatusMessage;
    }

    public void setstatusMessage(String  statusMessage) {
        this.statusMessage = statusMessage;
    }
    
    
    public int [] getlb() {
        return lb;
    }

    public void setlb(int lb[]) {
        this.lb = lb;
    }
    
    
    public int [] getlt() {
        return lt;
    }

    public void setlt(int lt[]) {
        this.lt = lt;
    }
    
    public int [] getrb() {
        return rb;
    }

    public void setrb(int rb[]) {
        this.rb = rb;
    }

    public int [] getrt() {
        return rt;
    }

    public void setrt(int rt[]) {
        this.rt = rt;
    }
    
    public int getminAge() {
        return minAge;
    }

    public void setminAge(int minAge) {
        this.minAge = minAge;
    }
    public int getmaxAge() {
        return maxAge;
    }

    public void setmaxAge(int maxAge) {
        this.maxAge = maxAge;
    } 
    
    public int getindex() {
        return index;
    }

    public void setindex(int index) {
        this.index = index;
    }
    public String gettitle() {
        return title;
    }

    public void settitle(String title) {
        this.title = title;
    }  
    
        
    public int [] getCenterRightEye() {
        return CenterRightEye;
    }

    public void setCenterRightEye(int  CenterRightEye []) {
        this.CenterRightEye[0] = CenterRightEye[0];
        this.CenterRightEye[1] = CenterRightEye[1];
    }
    
    
    public int [] getNoseTip() {
        return NoseTip;
    }

    public void setNoseTip(int  NoseTip []) {
        this.NoseTip[0] = NoseTip[0];
        this.NoseTip[1] = NoseTip[1];
    }
    
       
    public int [] getLipsRightCorner() {
        return LipsRightCorner;
    }

    public void setLipsRightCorner(int  LipsRightCorner []) {
        this.LipsRightCorner[0] = LipsRightCorner[0];
        this.LipsRightCorner[1] = LipsRightCorner[1];
    }
    
   
    public int [] getLipsLeftCorner() {
        return LipsLeftCorner;
    }

    public void setLipsLeftCorner(int  LipsLeftCorner []) {
        this.LipsLeftCorner[0] = LipsLeftCorner[0];
        this.LipsLeftCorner[1] = LipsLeftCorner[1];
    }
        
    
    public int [] getCenterLeftEye() {
        return CenterLeftEye;
    }

    public void setCenterLeftEye(int  CenterLeftEye []) {
        this.CenterLeftEye[0] = CenterLeftEye[0];
        this.CenterLeftEye[1] = CenterLeftEye[1];
    }
    
    
   
    public String getblur() {
        return blur;
    }

    public void setblur(String  blur) {
        this.blur = blur;
    } 
    
    
    public float getvalue() {
        return value;
    }

    public void setvalue(float  value) {
        this.value = value;
    } 
    
    public int getrotateAngel() {
        return rotateAngel;
    }

    public void setrotateAngel(int  rotateAngel) {
        this.rotateAngel = rotateAngel;
    } 
    
}