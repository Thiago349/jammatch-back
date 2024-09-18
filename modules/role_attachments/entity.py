import uuid

from alchemy import Base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime


class RoleAttachment(Base):
    __tablename__ = "role-attachments"
    __table_args__ = {"schema": "public"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    profile_id = Column(UUID(as_uuid=True), nullable=False)
    role_id = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    deleted_at = Column(DateTime(timezone=True), server_default=None)
