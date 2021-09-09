import pyqrcode
import png

url = pyqrcode.create('https://docs.google.com/forms/d/e/1FAIpQLScKr3lXqOtP6clCB_89muSAcHkphVmHg4U4AAkD3iZKL_EyIg/viewform?usp=sf_link')
url.png('involvementFest2021.png', scale = 10)
