from fastapi.responses import FileResponse
import os
async def download_qr(filename: str):
    # Directorio en el que se almacenan los códigos QR generados
    qr_directory = "directorio_de_codigos_qr"

    # Ruta completa al archivo de código QR
    file_path = os.path.join(qr_directory, filename)

    # Verifica si el archivo existe
    if os.path.exists(file_path):
        # Utiliza FileResponse para devolver el archivo para su descarga
        return FileResponse(file_path, headers={"Content-Disposition": f"attachment; filename={filename}"})
    else:
        # Devuelve una respuesta 404 si el archivo no se encuentra
        return {"error": "El archivo no se encontró"}, 404