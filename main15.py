from sqlalchemy import Column,Integer,String,create_engine,Row
from sqlalchemy.orm import Session,declarative_base,sessionmaker
from fastapi import FastAPI, Depends, HTTPException
app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"       
engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})
Session_Local = sessionmaker(bind=engine)

Base = declarative_base()
class User(Base):
    __tablename__ = "todos"
    id = Column(Integer,primary_key=True)
    Name = Column(String)
    Standard = Column(String)
    dob = Column(Integer)

Base.metadata.create_all(bind=engine)

def get_db():
    db = Session_Local()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_data")
def create_data(id:int,Name:str,Standard:str,dob:int,db:Session=Depends(get_db)):
    todos = User(id=id,Name=Name,Standard=Standard,dob=dob)
    db.add(todos)
    db.commit()
    db.refresh(todos)
    return {
        "Message" : "todo created",
        "Data" : todos
    }

@app.get("/retrieve_data")
def retrieve(db:Session=Depends(get_db)):
    users = db.query(User).all()
    return {
        "Total" : len(users),
        "data" : users
    }

@app.get("/retri/{user_id}")
def get(user_id=int,db:Session=Depends(get_db)):
    todo = db.query(User).filter(User.id==user_id).first()
    if not todo:
        raise HTTPException(
            status_code = 404,detail = "Todo not found")
    return todo
        
@app.put("/update/{user_id}")
def update(
    user_id: int, 
    Name: str,         
    Standard: str, 
    dob: int,
    db: Session = Depends(get_db)):
    todo = db.query(User).filter(User.id==user_id).first()
    if not todo:
        raise HTTPException(
            status_code = 404,
            detail = "Todo not found"
        )
    todo.Name = Name
    todo.Standard = Standard
    todo.dob = dob
    db.commit()
    db.refresh(todo)
    return {
        "Message" : "Todo is updated Successfully",
        "Data" : todo
}