#!/usr/bin/env python
#-*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///webexam/sqlite.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    '''init the database and create empty database
    if the database and the table exist,it will throw exception
    '''

    import webexam.models
    Base.metadata.create_all(bind=engine)