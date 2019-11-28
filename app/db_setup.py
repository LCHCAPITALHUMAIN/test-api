# -*- coding: utf-8 -*-

import databases
from loguru import logger
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

from settings import SQLALCHEMY_DATABASE_URI

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, poolclass=QueuePool, max_overflow=10, pool_size=100
)
metadata = MetaData()
database = databases.Database(SQLALCHEMY_DATABASE_URI)


def create_db():
    metadata.create_all(engine)
    logger.info("Create: {info}", info="Creating tables")


async def connect_db():
    await database.connect()
    logger.info("Create: {info}", info="connecting to database")


async def disconnect_db():
    await database.disconnect()
    logger.info("Create: {info}", info="disconnecting database")


users = Table(
    "users",
    metadata,
    # Column('Id', Integer, primary_key=True),
    Column("userId", String(length=100), primary_key=True),
    Column("user_name", String(length=50), unique=True, nullable=False),
    Column("firstName", String(length=150)),
    Column("lastName", String(length=150)),
    Column("title", String(length=200)),
    Column("company", String(length=200)),
    Column("address", String(length=300)),
    Column("city", String(length=200)),
    Column("country", String(length=200)),
    Column("postal", String(length=50)),
    Column("email", String(length=200)),
    Column("website", String(length=150)),
    Column("password", String(length=50)),
    Column("description", String(length=2000)),
    Column("dateCreate", DateTime()),
    Column("isActive", Boolean(), default=True),
    Column("isSuperuser", Boolean(), default=True),
)


todos = Table(
    "todos",
    metadata,
    Column("todoId", String, primary_key=True),
    Column("title", String(length=100)),
    Column("description", String(length=500)),
    Column("isComplete", Boolean()),
    Column("dateDue", Date()),
    Column("dateCreate", DateTime()),
    Column("dateUpdate", DateTime()),
    Column("dateComplete", DateTime()),
    Column("userId", String(length=100)),
)
# Foreign key Column('userId', None, ForeignKey('users.userId')),
