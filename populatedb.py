from sqlalchemy.orm import sessionmaker
from db_setup import Error, engine

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
