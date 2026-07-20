from fastapi import FastAPI, Depends, Header,HTTPException
from jose import jwt, JWTError
from datetime import datetime, timedelta,timezone
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext

app = FastAPI()
SECRET_KEY = "mytoken"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#PASSWORD HASHING SETUP 
pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")

#Oauthsetup
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

#Dummy User DB
fake_user_db = {
    "admin" : {
        "username" : "admin",
        "hashed_password" : pwd_context.hash("1234")

    }
}
#Hashing Password
def hash_password(password:str):
    return pwd_context.hash(password)

#Verify password
def verify_password(plain_password,hash_password):
    return pwd_context.verify(plain_password,hash_password)


def create_token(data:dict):
    To_encode = data.copy()
    expire = datetime.now(timezone.utc)+timedelta(minutes=30)
    To_encode.update({
        "exp" : expire
    })
    token = jwt.encode(To_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends()):
    user = fake_user_db.get(form_data.username)

    if not user or not verify_password(form_data.password,user["hashed_password"]):
        raise HTTPException(
            status_code=400,
            detail = "Invalid Username or password"
        )
    Access_token = create_token({
        "sub" : form_data.username
    })
    return {
        "access_token" : Access_token,
        "token_type" : "bearer"

    }

def verify_token(token:str=Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms = [ALGORITHM])
        username : str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code = 401,
                detail="Invalid or Expired token"
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code = 401,
            detail = "Invalid Token"
        )


@app.get("/secure")
def protected_route(username:str=Depends(verify_token)):
    return{
        "Message" : "Hello you have access to this protected route",
        "user" : username
        }

