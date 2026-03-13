from flask import Blueprint

bp = Blueprint(
    "cthulhu",
    __name__,
    url_prefix="/cthulhu",
    template_folder="templates",
)

from . import routes  # noqa: E402, F401
