from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
load_dotenv()



db_url=os.getenv("DB_URL")
engine=create_async_engine(db_url,echo=True)
SessionLocal=sessionmaker(engine,class_=AsyncSession,expire_on_commit=False)
Base=declarative_base()

async def get_connection_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.meta.create_all)
