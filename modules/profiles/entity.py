import uuid

from alchemy import Base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, String, Boolean


class Profile(Base):
    __tablename__ = "profiles"
    __table_args__ = {"schema": "public"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    main_id = Column(UUID(as_uuid=True))
    description = Column(String)
    has_photo = Column(Boolean)
    has_banner = Column(Boolean)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    deleted_at = Column(DateTime(timezone=True), server_default=None)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
