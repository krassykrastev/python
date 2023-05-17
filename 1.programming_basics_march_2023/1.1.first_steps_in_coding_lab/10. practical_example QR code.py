import pyqrcode
import png
from pyqrcode import QRCode

address = 'https://python-book.softuni.bg/chapter-01-first-steps-in-programming.html'
url = pyqrcode.create(address)
url.png('test.png', scale=8)
