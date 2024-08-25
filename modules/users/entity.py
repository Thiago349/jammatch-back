import uuid

from alchemy import Base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, String


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "public"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    deleted_at = Column(DateTime(timezone=True), server_default=None)
    description = Column(String)