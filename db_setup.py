from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from marshmallow_sqlalchemy import ModelSchema

Base = declarative_base()


# DB Structure Definition
class ShortURL(Base):
    """ 
    This class contains the fields for shortURL model.
    """

    __tablename__ = 'shorturl'

    id = Column(Integer, primary_key=True)

    alias = Column(String)
    original_url = Column(String)
    shortened_url = Column(String)
    time_taken = Column(String)


class ShortURLSchema(ModelSchema):
    """
    This class contains the Schema for shortURL models
    It'll help in the decoding of the DB info to JSON
    """

    class Meta:
        model = ShortURL


class Error(Base):
    """
    This class contains the field for Error model
    It'll be used to map all the errors
    """

    __tablename__ = 'error'
    id = Column(Integer, primary_key=True)
    ERR_ID = Column(String)

    description = Column(String)

class ErrorSchema(ModelSchema):
    """
    This class contains the Schema for Errors models
    It'll help in the decoding of the DB info to JSON
    """
    
    class Meta:
        model = Error
        exclude = ('id',)


shorturl_schema = ShortURLSchema()
error_schema = ErrorSchema()
engine = create_engine('postgresql://postgres:postgres@localhost:5432/shortenerapi')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#Error Mapping
description_one = 'CUSTOM ALIAS ALREADY EXISTIS'
error_one = Error(ERR_ID='001', description=description_one)

description_two = 'URL DOES NOT EXISTIS'
error_two = Error(ERR_ID='002', description=description_two)

description_three = 'URL IS ALREADY SHORTENED'
error_three = Error(ERR_ID='003', description=description_three)

description_four = 'SHORTENED URL NOT FOUND'
error_four = Error(ERR_ID='004', description=description_four)

session.add(error_one)
session.add(error_two)
session.add(error_three)
session.add(error_four)
session.commit()




