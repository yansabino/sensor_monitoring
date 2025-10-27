from flask import Blueprint

def readings_blueprint(controller):
    bp = Blueprint("readings_bp", __name__)
    bp.add_url_rule('/readings', methods=["POST"], view_func=controller.create_reading)
    return bp