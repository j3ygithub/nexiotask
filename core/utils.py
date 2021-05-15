from flask import abort

from . import status_codes


def get_object_or_404(model, pk):
    obj = model.query.get(pk)
    if not obj:
        abort(status_codes.NOT_FOUND)
    return obj
