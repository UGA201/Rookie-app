from rookie_app.services.embedding_api import en
from sklearn.ensemble import RandomForestClassifier
from rookie_app.models.models import User, Group, Tweet
from rookie_app import db
import numpy as np

def msg_processor(msg_code):
    '''
    msg_processor returns a msg object with 'msg', 'type'
    where 'msg' corresponds to the message user sees
    and 'type' is the color of the alert element

    codes:
        - 0 : Successfully added to database
        - 1 : User does not exist
        - 2 : Unable to retrieve tweets
        - 3 : Successfully deleted user
        - 4 : Username already exists
        - 5 : Select groups again
        - 6 : No result yet
    '''

    msg_code = int(msg_code)

    msg_list = [
        (
            'Successfully added to database',
            'success'
        ),
        (
            'User does not exist',
            'warning'
        ),
        (
            'Unable to retrieve tweets',
            'warning'
        ),
        (
            'Successfully deleted user',
            'info'
        ),
        (
            '''
            Username is already exist.
            If you want to update your selection data, 
            please use \'Find Rookies\' button.
            ''',
            'warning'
        ),
        (
            'Please select 3 to 7 groups',
            'warning'
        ),
        (
            'No result yet',
            'info'
        )
    ]

    return {
        'msg':msg_list[msg_code][0],
        'type':msg_list[msg_code][1]
    }

def recommend_processor(user_id):
    u_id = user_id
    train_X_list = [r.embedding for r in db.session.query(
        Tweet
        ).outerjoin(Group, Tweet.group_id==Group.id
        ).filter(
            Group.user_id == u_id
            ).filter(
                Group.like_or_not != None
        )]

    test_X_list = [r.embedding for r in db.session.query(
        Tweet
        ).outerjoin(Group, Tweet.group_id==Group.id
        ).filter(
            Group.user_id == u_id
            ).filter(
                Group.like_or_not == None
        )]

    train_y_list = [r.like_or_not for r in db.session.query(
        Tweet
        ).outerjoin(Group, Tweet.group_id==Group.id
        ).filter(
            Group.user_id==u_id
            ).filter(
                Group.like_or_not != None
        )]

    
    train_X = np.array(train_X_list)
    test_X = np.array(test_X_list)
    
    train_y = str(train_y_list)
    train_y = eval(train_y)
    train_y = np.array(train_y)

    classifier = RandomForestClassifier()
    classifier.fit(train_X, train_y)

    y_pred = classifier.predict(test_X)


    keys_id_list = [r.group_id for r in db.session.query(
        Tweet
        ).outerjoin(Group, Tweet.group_id==Group.id
        ).filter(
            Group.user_id == u_id
            ).filter(
                Group.like_or_not == None
        )]

    keys_list =[]
    for k in keys_id_list:
        k_group = Group.query.filter_by(id=k).first()
        keys_list.append(k_group.group_name)

    rookies = ['DKB', 'cignature', 'CRAVITY', 'Weeekly', 'TREASURE', 'WEI', 'DRIPPIN', 'STAYC', 'aespa', 'ENHYPEN']
    dct = {}
    for a in rookies:
        dct[a]=[]

    for i in range(len(keys_list)):
        dct[keys_list[i]].append(y_pred[i])

    mx = 0
    for r in rookies:
        if mx < sum(dct[r]):
            mx = sum(dct[r])
            rmax = r
    if mx == 0:
        rmax = rookies[np.random.randint(0,len(rookies))]
    return str(rmax)
