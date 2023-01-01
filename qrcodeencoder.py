import qrcode
from datetime import datetime
qr = qrcode.QRCode(
    version=2,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
print("Enter the link to be qred:\n")
x = input()
qr.add_data(x)
qr.make(fit=True)
img =  qr.make_image(fill_color="black", back_color="white")
file_name = "output_"+datetime.now().strftime("%d_%m_%Y_%H_%M_%S")+".png"
img.save(file_name)
