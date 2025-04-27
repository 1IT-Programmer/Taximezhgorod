from sqlalchemy.orm import Session
from .models import User, Trip
from .schemas import UserCreate, TripCreate

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password, full_name=user.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_trip(db: Session, trip: TripCreate, user_id: int):
    db_trip = Trip(**trip.dict(), owner_id=user_id)
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip
