from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, Enum, JSON
from sqlalchemy.sql import func
from enum import Enum as PyEnum
import enum

from app.core.database import Base


class ProgrammeState(str, enum.Enum):
    DRAFT = "draft"
    APPROVED = "approved"
    IMPLEMENTED = "implemented"


class Methodology(str, enum.Enum):
    CONVENTIONAL = "conventional"
    TASK_TO_TOOL = "task_to_tool"


class FidelityLevel(str, enum.Enum):
    N = "N"
    G = "G"
    R = "R"
    S = "S"


class Programme(Base):
    __tablename__ = "programmes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    aircraft_type = Column(String(100), nullable=False)
    aircraft_variant = Column(String(100))
    methodology = Column(Enum(Methodology), default=Methodology.CONVENTIONAL)
    state = Column(Enum(ProgrammeState), default=ProgrammeState.DRAFT)
    created_at = Column(DateTime, server_default=func.now())


class FSTD(Base):
    __tablename__ = "fstds"

    id = Column(Integer, primary_key=True, index=True)
    identifier = Column(String(100), nullable=False, unique=True)
    manufacturer = Column(String(100))
    device_category = Column(String(50))
    has_esl = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
