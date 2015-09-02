from flask import Blueprint

common = Blueprint('common', __name__)


@common.route('/', methods=['GET'])
def index():
    """ Function to return index template page
    """

    return "Hello!"
