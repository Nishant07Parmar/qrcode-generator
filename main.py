import qrcode

url = input("Enter the URL to generate QR code: ")
img = qrcode.make(url)
img.save("project_qr.png")
print("QR code generated and saved as project_qr.png")
