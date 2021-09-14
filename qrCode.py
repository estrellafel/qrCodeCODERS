import pyqrcode
import png

url = pyqrcode.create('https://docs.google.com/forms/d/1X8HJcUJfFMgQxCVehBnouqHy9AbHf0urFbAFLmFxHPU/edit')
url.png('LASOinvolvementFest2021.png', scale = 10)
