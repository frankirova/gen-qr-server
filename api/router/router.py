from fastapi import APIRouter
from fastapi.responses import FileResponse

from api.services.qrGen import generate_qr
from urllib.parse import unquote




router = APIRouter()

@router.get("/api/qr/{link:path}")
async def getQr(link):
    print(link)
    decoded_link = unquote(link)
    qr_image = await generate_qr(decoded_link)
    return qr_image

# @router.get('/download')
# async def download_qr(qr_image):
#     print(qr_image)
#     temp_file = f"/tmp/qrcode.png"
#     qr_image.save(temp_file)
#     return FileResponse(temp_file, headers={"Content-Disposition": "attachment; filename=qrcode.png"})