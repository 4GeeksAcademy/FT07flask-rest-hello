from flask_sqlalchemy import SQLAlchemy
from typing import List
from datetime import datetime
from sqlalchemy import String, Boolean, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = "users"
  user_id:Mapped[int] = mapped_column(Integer,primary_key=True)
  user_name:Mapped[str] = mapped_column(String(250), nullable=False)
  last_name:Mapped[str] = mapped_column(String(250), nullable=False)
  nickname:Mapped[str] = mapped_column(String(50),unique=True, nullable=False)
  email:Mapped[str] = mapped_column(String(250),unique=True, nullable=False)
  post_id: Mapped[int] = mapped_column(ForeignKey('posts.post_id'),nullable=False)
  create_post: Mapped["Post"] = relationship(
    back_populates="users"
  )
  give_like:Mapped["Like"] = relationship(
    back_populates="author_id"
  )
  create_comment:Mapped["Comment"] = relationship(
    back_populates="written_by"
  )


class Post(db.Model):
  __tablename__ = "posts"
  post_id:Mapped[int]= mapped_column(Integer,primary_key=True)
  users:Mapped[List['User']] = relationship(
    back_populates= "create_post"
  )
  likes:Mapped[List['Like']]= relationship(
    back_populates=""
  )
  
  
class Like (db.Model):
  __tablename__ = "likes"
  like_id:Mapped[int]= mapped_column(Integer,primary_key=True)
  author_id:Mapped[List['User']]= relationship(
    back_populates="give_like"
  )
  post_id:Mapped[int]=mapped_column(ForeignKey('posts.post_id'),nullable=False)

class Comment(db.Model):
  __tablename__ = "comments"
  comment_id:Mapped[int] = mapped_column(Integer,primary_key=True)
  comment_text:Mapped[str] = mapped_column(String(250),nullable=False)
  created_at:Mapped[datetime] = mapped_column(DateTime,default=func.now())
  update_at:Mapped[datetime] = mapped_column(DateTime,default=func.now(),onupdate=func.now())
  written_by:Mapped[List['User']]= relationship(
    back_populates="create_comment"
  )
  post_id:Mapped[int]=mapped_column(ForeignKey('posts.post_id'),nullable=False)

