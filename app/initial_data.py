import logging

from app.db.init_db import init_db
from app.db.session import SessionLocal, engine
from app.models import user

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    init_db(db)  # Create default superuser.


def create() -> None:
    user.Base.metadata.create_all(bind=engine)  # Create tables in database.
    logger.info(f'Creating table: {user.User.__tablename__}.')


def main() -> None:
    logger.info("Creating initial data")
    create()
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
