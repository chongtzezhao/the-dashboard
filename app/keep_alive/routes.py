from flask import Blueprint

keep_alive_bp = Blueprint('keep_alive', __name__)

@keep_alive_bp.route('/keep_alive')
def keep_alive():
    return "Bot is alive!", 200