import qrcode

# Replace with your real GitHub Pages URL after publishing
URL = "https://ulissedusci.github.io/Speisekarte/"

img = qrcode.make(URL)
img.save("qr_speisekarte.png")
print("QR-Code gespeichert für:", URL)
