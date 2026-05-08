from fastapi import FastAPI

from app.routers import passwords, users



app = FastAPI(title="Password Generator API")

app.include_router(users.router)
app.include_router(passwords.router)


@app.get("/")
def root():
    return {"message": "API is running"}