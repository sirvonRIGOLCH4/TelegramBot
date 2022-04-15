from datetime import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Theme(SqlAlchemyBase):
    __tablename__ = 'theme'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # json
    date_of_creation = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)

  #  tag_id = sqlalchemy.Column(sqlalchemy.Integer,
   #                            sqlalchemy.ForeignKey("tag.id"))
  #  tag = orm.relation("Tag")

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')

    def __repr__(self):
        return f'<theme> {self.title}'
