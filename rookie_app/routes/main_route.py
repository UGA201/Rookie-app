from flask import Blueprint, render_template, request, redirect, url_for
from rookie_app.utils import main_funcs
from rookie_app.models.models import User, Group, Tweet
from rookie_app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/recommended/')
@bp.route('/recommended/<int:user_id>')
def recommend_index(user_id):
    
    f_user = User.query.filter_by(id=user_id).first()
    username = f_user.username
    rookie_name = main_funcs.recommend_processor(user_id=user_id)

    f_user.latest_result = rookie_name
    db.session.merge(f_user)
    db.session.commit()

    return render_template('recommend.html', username=username, rookie_name=rookie_name), 200


@bp.route('/user/')
def user_index():
    """
    user_list 에 유저들을 담아 템플렛 파일에 넘김
    """

    msg_code = request.args.get('msg_code', None)
    
    alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None

    user_list = User.query.order_by(User.id.desc())

    return render_template('user.html', alert_msg=alert_msg, user_list=user_list)


@bp.route('/group/<int:user_id>/')
def group_index(user_id):
    '''
    user가 선호하는 10개 그룹 중 3~7개를 선택하도록 함
    '''
    msg_code = request.args.get('msg_code', None)
    
    alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None

    return render_template('group.html', alert_msg=alert_msg, user_id=user_id),200


@bp.route('/recommend/latest/')
@bp.route('/recommend/latest/<int:user_id>/', methods=["GET"])
def recommend_latest(user_id):
    
    f_user = User.query.filter_by(id=user_id).first()
    
    if f_user.latest_result is None:
        msg_code = request.args.get('msg_code', None)
        alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None
        return redirect(url_for('main.user_index', msg_code=6))
    
    username = f_user.username
    rookie_name = f_user.latest_result

    return render_template('recommend.html', username=username, rookie_name=rookie_name), 200