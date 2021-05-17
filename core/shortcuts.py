from flask import abort
from marshmallow.exceptions import ValidationError

from . import status_codes


def get_object_or_404(model, pk):
    obj = model.query.get(pk)
    if not obj:
        abort(status_codes.NOT_FOUND)
    return obj


def get_cleaned_data_or_400(data, schema_class, expected_error=ValidationError):
    try:
        cleaned_data = schema_class().load(data)
    except expected_error:
        abort(status_codes.BAD_REQUEST)
    return cleaned_data
