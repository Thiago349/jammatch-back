import uuid

from alchemy import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String


class Role(Base):
    __tablename__ = "roles"
    __table_args__ = {"schema": "public"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    label = Column(String, nullable=False)
    profile_type = Column(String, nullable=False)
