from flask import Blueprint, render_template, redirect

url_prefix = '/telebot'

telebot_bp = Blueprint('telebot', __name__, url_prefix=url_prefix)

@telebot_bp.route('/')
def index():
    # redirect to chats page
    return redirect(f'{url_prefix}/chats')

@telebot_bp.route('/chats')
def chats():
    return render_template(f'{url_prefix}/chats.html')