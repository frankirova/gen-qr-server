from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.router.router import router 

app = FastAPI()

# Configuración CORS
# origins = [
#     "http://localhost:5173",
#     "http://localhost:8000",
# ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Rutas
app.include_router(router)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
