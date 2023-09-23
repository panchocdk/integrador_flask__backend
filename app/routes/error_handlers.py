from flask import Blueprint
from ..models.exceptions import SourceNotFound, InvalidDataError

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(SourceNotFound)
def handle_source_not_found(error):
    return error.get_response()

@errors.app_errorhandler(InvalidDataError)
def handle_validate_data(error):
    return error.get_response()