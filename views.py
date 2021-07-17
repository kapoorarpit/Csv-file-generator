from flask import Blueprint

main = Blueprint('main',__name__)

@main.route('/submit_url', method=['POST'])
def submit_url():
    return 'successful', 201