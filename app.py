from datetime import datetime
import requests
from flask import Flask, json, url_for, request, redirect
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Error, engine, ShortURL, shorturl_schema, error_schema
from helpers import randomString


app = Flask('__name__')
app.secret_key = '\x05MNV\x8d\x83@\xdd\x8c}\x087\x8d2I}o\xbe\xdbAs\xd6\xf8s'
app.debug = True
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/u/<string:alias>', methods=['GET'])
def retrieve_url(alias):
    if request.method == 'GET':
        shorturl = session.query(ShortURL).filter_by(alias=alias).first()
        if not shorturl:
           error_id = '004'
           error = json.dumps(error_schema.dump(session.query(Error).filter_by(ERR_ID=error_id).first()).data)
           return error 
        original_url = str(session.query(ShortURL).filter_by(alias=alias).first().original_url)
        return redirect(original_url, code=302)


@app.route('/create', methods=['POST'])
def create_url():
    if request.method == 'POST':
        # Starting timer to count transaction time
        start_time = datetime.now()
        
        # Accessing original_url
        original_url = request.args.get('url')
        r = requests.get(original_url)
        
        # Checking if the URL is a valid URL
        if r.status_code == 200:
            url = session.query(ShortURL).filter_by(original_url=original_url).first()
            
            # Checking if the  URL has already been shortened
            if url:
                error_id = '003'
                error = session.query(Error).filter_by(ERR_ID=error_id).first()
                return_data = error_schema.dump(error).data
                return_data['shortURL'] = url.shortened_url
                
                answer = json.dumps(return_data)
                
                return answer

            # Retrieving CUSTOM_ALIAS
            alias = request.args.get('CUSTOM_ALIAS')

            # Checking if there is CUSTOM_ALIAS
            if alias:

                alias_search = session.query(ShortURL).filter_by(alias=alias).first()
                
                # If alias already exists
                if alias_search:
                    error_id = '001'
                    error = session.query(Error).filter_by(ERR_ID=error_id).first()
                    return_data = json.dumps(dict(error_schema.dump(error).data))

                    return return_data
            
            else:
                alias = randomString(6)
            
            shortened_url = url_for('retrieve_url', alias=alias)
            elapsed_time = datetime.now() - start_time
            elapsed_ms = str(elapsed_time.microseconds / 1000) + 'ms'

            short = ShortURL(alias=alias, original_url=original_url, shortened_url=shortened_url, time_taken=elapsed_ms)
            session.add(short)
            session.commit()
            
            return_data = json.dumps(dict(shorturl_schema.dump(short).data))

            return return_data
        else:
            Response.close()
            error_id = 2
            error = session.query(Error).filter_by(ERR_ID   =error_id).first()
            return_data = json.dumps(dict(error_schema.dump(error).data))
            return return_data

        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
