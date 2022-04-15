from datetime import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Comment(SqlAlchemyBase):
    __tablename__ = 'comment'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # json
    date_of_creation = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)

    main_theme_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("theme.id"))
    main_theme = orm.relation('Theme')

   # tag_id = sqlalchemy.Column(sqlalchemy.Integer,
   #                            sqlalchemy.ForeignKey("tag.id"))
   # tag = orm.relation("Tag")

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')