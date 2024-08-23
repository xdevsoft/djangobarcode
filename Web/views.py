from django.shortcuts import render
from django.http import HttpResponse
from reportlab.graphics.barcode import createBarcodeImageInMemory


def index(request):
    '''
    https://docs.reportlab.com/reportlab/userguide/ch1_intro/
    https://docs.reportlab.com/reportlab/barcode/
    https://flask.palletsprojects.com/

    Barcode Types: 
        EAN8, EAN13, EAN5, ISBN, UPCA, QR, Code128, Code128Auto
        Standard39, Standard93, MSI, Codebar, Code11, FIM, POSTNET
        Extended39, Extended93, I2of5, ECC200DataMatrix

    '''
    
    # you can also review my previous example:
    # https://github.com/xdevsoft/barcodegen
    barcode = createBarcodeImageInMemory(
        'Code128',                  # Refer to barcode types 
        value='123456789012',       # code to be encoded/printed
        width=300, 
        height=60,
        format='png'                # png, gif, tiff
    )

    return HttpResponse(barcode, content_type='image/png')