import qrcode
from io import BytesIO
from starlette.responses import StreamingResponse

async def generate_qr(link):
    qr_img = qrcode.make(link)

    # Crea un objeto BytesIO para almacenar la imagen del QR
    img_io = BytesIO()
    qr_img.save(img_io, format='PNG')
    img_io.seek(0)

    # Crea una respuesta StreamingResponse con la imagen del QR
    return StreamingResponse(img_io, media_type="image/png",)