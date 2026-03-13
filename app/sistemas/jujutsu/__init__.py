from flask import Blueprint

bp = Blueprint(
    "jujutsu",
    __name__,
    url_prefix="/jujutsu",
    template_folder="templates",
)

from . import routes  # noqa: E402, F401
