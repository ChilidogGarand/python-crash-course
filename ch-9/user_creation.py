import user_info
# Split into two different modules for exercise 9-12
import user_privs

#user_a = user_info.Admin('john', 'brown', 'equity and inclusion')
#user_a.privs.show_privileges()
#user_a.greet_user()

#user_b = user_info.User('frances', 'bartleby', 'legal')
#user_b.privs.show_privileges()
#user_b.greet_user()

user_a = user_privs.Admin('john', 'brown', 'equity and inclusion')
user_a.privs.show_privileges()