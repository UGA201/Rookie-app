from flask import Blueprint, request, redirect, url_for, Response, render_template
from rookie_app.services import tweepy_api, embedding_api
from rookie_app.models import models
from rookie_app.models.models import User, Group, Tweet
from rookie_app import db

bp = Blueprint('user', __name__)


@bp.route('/user/', methods=['POST'])
def add_user():
    username = request.form['username']

    if not username:
      return redirect(url_for('main.user_index', msg_code=1), code=400)
    
    exist = User.query.filter_by(username=username).first()
    if exist is not None:
      return redirect(url_for('main.user_index', msg_code=4), code=400)

    add_user = User(username=username)
    db.session.add(add_user)
    db.session.commit()
    return redirect(url_for('main.user_index', msg_code=0), code=200)
    
    
@bp.route('/user/')
@bp.route('/user/<int:user_id>/')
def delete_user(user_id=None):
    if user_id is None:
      return '',400

    d_user = User.query.filter_by(id=user_id).one_or_none()
    if d_user is None:
      return '',404

    db.session.delete(d_user)
    db.session.commit()
    return redirect(url_for('main.user_index', msg_code=3), code=200)
