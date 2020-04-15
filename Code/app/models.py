from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return Users.get_user(user_id)

class Users(UserMixin):
	def __init__(self,uid,uname,password,type):
		self.userid = uid
		self.username = uname
		self.password = password
		self.type = type

	def get_id(self):
		return (self.username)

	@staticmethod
	def get_user(username):
		cur = db.connection.cursor()
		cur.execute(''' SELECT * FROM Users WHERE Usersname='{}' '''.format(username))
		r1 = cur.fetchone()
		if r1:
			if(r1['Type']=='c'):
				a='Cust_id'
				b='Customer'
			if(r1['Type']=='s'):
				a='Seller_id'
				b='Seller'
			cur.execute(''' SELECT {} AS id FROM {} WHERE Usersname='{}' '''.format(a,b,username))
			r2 = cur.fetchone()
			user = Users(r2['id'],r1['Usersname'],r1['Password'],r1['Type'])
			return user
		return None