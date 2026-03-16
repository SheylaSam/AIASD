from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.infrastructure.database import Base


class UserModel(Base):
    """SQLAlchemy-Model: users-Tabelle."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)

    documents = relationship("DocumentModel", back_populates="owner")


class DocumentModel(Base):
    """SQLAlchemy-Model: documents-Tabelle."""
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("UserModel", back_populates="documents")
    quizzes = relationship("QuizModel", back_populates="document")


class QuizModel(Base):
    """SQLAlchemy-Model: quizzes-Tabelle."""
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    fragen = Column(JSON, nullable=False, default=list)

    document = relationship("DocumentModel", back_populates="quizzes")


class LernRaumModel(Base):
    """SQLAlchemy-Model: lernraeume-Tabelle."""
    __tablename__ = "lernraeume"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    mitglieder_ids = Column(JSON, nullable=False, default=list)
    document_ids = Column(JSON, nullable=False, default=list)
