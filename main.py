import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer


http_bearer = HTTPBearer(auto_error=False)


app = FastAPI(dependencies=[Depends(http_bearer)])





if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
