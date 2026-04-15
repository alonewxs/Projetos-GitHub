import qrcode
import time

print("Seja bem vindo(a) ao gerador de QR Code")
time.sleep(0.5)

get_qrcode = input("O que você gostaria de transformar em QR CODE? ")
time.sleep(0.2)
nome_qrcode = input("Qual nome do arquivo do QR CODE? ")
time.sleep(0.3)


qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 8,
)


qr.add_data( get_qrcode )
qr.make( fit = True )

img = qr.make_image(
     fill_color = "black", 
     back_color = "white"
)

img.save(f"{nome_qrcode}.png")