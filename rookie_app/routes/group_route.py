from flask import Blueprint, request, redirect, url_for, Response
from rookie_app.services import tweepy_api, embedding_api
from rookie_app.models.models import User, Group, Tweet
from rookie_app import db

bp = Blueprint('group', __name__)

@bp.route('/group/')
@bp.route('/group/<int:user_id>/', methods=['GET','POST'])
def select_group(user_id=None):
    if user_id is None:
      return '',400

    selected_group = request.form.getlist('group')
    groups = ['BTS', 'BLACKPINK', 'ITZY', 'MonstaX', 'IU', 'ATEEZ', 'BraveGirls', 'DREAMCATCHER', 'NCT', 'TWICE']
    uns_group = [item for item in groups if item not in selected_group]
    
    # 너무 적거나 많이 선택한 경우 재선택 안내
    if len(selected_group) < 3 or len(selected_group) > 7:
      return redirect(url_for('main.group_index', user_id=user_id, msg_code=5))

    # 해당 유저가 이미 선택한 그룹이 있는 경우, 데이터 삭제 후 재추가(Update)
    f_user = Group.query.filter_by(user_id=user_id).all()
    if f_user is not None:
      for d_user in f_user:
        db.session.delete(d_user)
        db.session.commit()

    # 전체 그룹을 group 테이블에 추가
    for group in selected_group:
      add_s_groups = Group(user_id=user_id, group_name=group, like_or_not=1)
      db.session.add(add_s_groups)
      db.session.commit()
    for group in uns_group:
      add_uns_groups = Group(user_id=user_id, group_name=group, like_or_not=0)
      db.session.add(add_uns_groups)
      db.session.commit()
    
    # Test 데이터로 사용할 루키들도 group 테이블에 추가
    rookies = ['DKB', 'cignature', 'CRAVITY', 'Weeekly', 'TREASURE', 'WEI', 'DRIPPIN', 'STAYC', 'aespa', 'ENHYPEN']
    for group in rookies:
      add_rookies = Group(user_id=user_id, group_name=group, like_or_not=None)
      db.session.add(add_rookies)
      db.session.commit()
    
    # 트윗데이터가 이미 있는 경우, 데이터 삭제 후 재추가(Update)
    skip_api = Tweet.query.all()
    if skip_api is not None:
      for d_data in skip_api:
        db.session.delete(d_data)
        db.session.commit()
    

    # 해당 유저의 아이돌 데이터에 대해 최신 트윗 수집, 임베딩
    u_group = Group.query.filter_by(user_id=user_id).all()
    for group in u_group:
      raw_tweets = tweepy_api.get_tweets(group.group_name)

      for tweet in raw_tweets:
        vecs = embedding_api.get_embeddings([str(tweet.text)])
        add_tweet = Tweet(group_id=group.id, text=tweet.text, embedding=vecs[0])
        db.session.add(add_tweet)
        db.session.commit()
  
    # return 'Successfully Uploaded', 200
    return redirect(url_for('main.recommend_index', user_id=user_id))

    
