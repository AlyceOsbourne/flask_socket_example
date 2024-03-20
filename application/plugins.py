import flask_login, flask_sqlalchemy, flask_socketio, flask_bcrypt

login_manager = flask_login.LoginManager()
db = flask_sqlalchemy.SQLAlchemy()
socketio = flask_socketio.SocketIO()
bcrypt = flask_bcrypt.Bcrypt()

login_user = flask_login.login_user
logout_user = flask_login.logout_user
current_user = flask_login.current_user
login_required = flask_login.login_required

on = socketio.on
emit = socketio.emit
send = socketio.send

class User(flask_login.UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    
    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        
    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
        
    @login_manager.user_loader
    @classmethod
    def load_user(cls, user_id):
        return cls.query.get(user_id)

def init_app(app):
    for extension in [login_manager, db, socketio, bcrypt]:
        extension.init_app(app)
        
    with app.app_context():
        db.create_all()
        db.session.commit()
        
        if not User.query.filter_by(username='admin').first():
            user = User(username='admin', password='admin')
            db.session.add(user)
            db.session.commit()
            
        return app

