from rookie_app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    groups = db.relationship('Group', backref=db.backref('user'), cascade='all, delete-orphan')

    def __repr__(self):
        return f"User {self.id} {self.username}"


class Group(db.Model):
    __tablename__ = 'group'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    group_name = db.Column(db.String(64), nullable=False)
    like_or_not = db.Column(db.Boolean(), nullable=True)
    tweets = db.relationship('Tweet', backref=db.backref('group'), cascade='all, delete-orphan')

    def __repr__(self):
        return f"{int(self.like_or_not==True)}"


class Tweet(db.Model):
    __tablename__ = 'tweet'

    id = db.Column(db.Integer(), primary_key=True)
    group_id = db.Column(db.Integer(), db.ForeignKey('group.id', ondelete='CASCADE'))
    text = db.Column(db.Text())
    embedding = db.Column(db.PickleType())
    like_or_not = db.relationship('Group', backref=db.backref('tweet'))

    def __repr__(self):
        return f"{self.like_or_not} "


