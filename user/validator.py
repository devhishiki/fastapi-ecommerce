from sqlalchemy.orm import Session

from user.models import User


async def verify_email_exist(email: str, db_session: Session):
    return db_session.query(User).filter(User.email == email).first()
