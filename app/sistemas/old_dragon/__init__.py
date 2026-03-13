from flask import Blueprint

bp = Blueprint(
    "old_dragon",
    __name__,
    url_prefix="/old-dragon",
    template_folder="templates",
)

from . import routes  # noqa: E402, F401
