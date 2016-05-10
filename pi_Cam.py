import picamera

class Picture:
  def __init__(self):
    self.camera = picamera.PiCamera()
  
  def take_image(self, image_name):
    self.camera.capture(image_name + '.jpeg')

if __name__=="__main__":
  from pi_Cam import picture
  c = Picture()
  c.take_image("test")
  
