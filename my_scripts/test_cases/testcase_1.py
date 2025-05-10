from actions_tc1 import register_new_user
from actions_tc1 import register_existed_user
from actions_tc1 import login

# my_email = 'alexey@gmail.com'
# my_email = 'alexey.gnet@gmail.com'
my_email = 'hanna4@gmail.com'
my_password = 'qwerty1234Vag007!'

register_new_user(my_email, my_password)
register_existed_user(my_email, my_password)
login(my_email, my_password)

print('testing is completed')






