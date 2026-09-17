import qrcode 



def qr_creation(url: str):
    img = qrcode.make(url)
    img.save("generated_qr.png")
    print("QR is generated")
    return 


url = input("Paste your url: ")
qr_creation(url)
