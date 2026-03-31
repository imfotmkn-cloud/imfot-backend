from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

# Routes import
from routes import auth, dashboard, tasks

# Create app
app = FastAPI(
    title="IMFOT OS API",
    version="1.0.0"
)

# API router
api_router = APIRouter(prefix="/api")

# Root API
@api_router.get("/")
def root():
    return {"message": "IMFOT OS Running 🚀"}

# Include routes
api_router.include_router(auth.router)
api_router.include_router(dashboard.router)
api_router.include_router(tasks.router)

# Add router to app
app.include_router(api_router)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
