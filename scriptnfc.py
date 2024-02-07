import nfc
import webbrowser
def on_connect(tag):
    if isinstance(tag, nfc.ndef.NDEF):
        for record in tag:
            if isinstance(record, nfc.ndef.TextRecord):
                url = record.text

                webbrowser.open(url)
                print(f"Se abrio la URL: {url}")
                break

clf = nfc.ContactlessFrontend()
try:
    clf.open('usb:072F:2200') #Reemplaza por la direccion del lector
    clf.connect(rdwr={'on-connect': on_connect})
finally:
    clf.close()

#instalar python, ide, drivers lector
#instalar pip install nfcpy
#lsusb para corroborar direccion de lector