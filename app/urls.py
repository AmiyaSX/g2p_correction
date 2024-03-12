from flask import Blueprint
# from app.views import text_to_audio, grapheme_log_view

import views

interface = Blueprint('interface', __name__)

interface.add_url_rule(
    '/', view_func=views.text_to_audio,
    methods=['GET', 'POST']
)

interface.add_url_rule(
    '/grapheme-log/<int:grapheme_id>',
    view_func=views.grapheme_log_view,
    methods=['GET']
)
