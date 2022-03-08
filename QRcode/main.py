import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Create QRcode
data = "https://camm93.github.io/"
file_path = "D:/MyPortfolio/portfolioqr_code1.png"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="white")
img.save(file_path)

# Reading a QRcode
img = Image.open(file_path)
result = decode(img)
print(result)
