from flask import Flask, request
import md5
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('./index.html')

@app.route('/login', methods=['GET','POST'])
def cookie_insertion():
    print request.json
    #redirect_to_index = redirect('/')
    #response = app.make_response(redirect_to_index )
    response.set_cookie('auth',value='values')
    return response

app.run();
