from chalice import Chalice

app = Chalice(app_name='chalice-app')

@app.route('/')
def index():
    return {
        "status": 200
    }

@app.route('/copyProtection')
def copyProtection(event, context):
    return {
        "isBase64Encoded": False,
        "status": 200
    }
