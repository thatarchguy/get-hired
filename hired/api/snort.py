from flask import jsonify, request, Blueprint
from hired import db, models

snort_api = Blueprint('snort_api', __name__, url_prefix='/api/v1/snort')


@snort_api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])


@snort_api.errorhandler(400)
def bad_request_error(e):
    return bad_request('invalid request')


@snort_api.errorhandler(404)
def not_found_error(e):
    return not_found('item not found')


@snort_api.route("/rules/", methods=["POST"])
def snort_add_rule():
    pass


@snort_api.route("/rules/<int:rule_id>", methods=["GET"])
@snort_api.route("/rules/", methods=["GET"])
def snort_get_rule(rule_id=None):
    pass
