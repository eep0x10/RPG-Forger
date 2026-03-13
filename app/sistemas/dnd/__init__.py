from flask import Blueprint

bp = Blueprint(
    "dnd",
    __name__,
    url_prefix="/dnd",
    template_folder="templates",
)

from . import routes  # noqa: E402, F401
