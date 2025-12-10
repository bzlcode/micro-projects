# Generate a QR Code with Python
import qrcode

website_link = input('Enter the link: ')

my_qr = qrcode.QRCode(version=1, box_size=5, border=5)
my_qr.add_data(website_link)
my_qr.make()

img = my_qr.make_image(fill_color='black', back_color='white')
name=input('Enter the name of the file: ')
img.save(name+'.png')