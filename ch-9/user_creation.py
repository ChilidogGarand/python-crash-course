import user_info

user_a = user_info.Admin('john', 'brown', 'equity and inclusion')
user_a.privs.show_privileges()
user_a.greet_user()

user_b = user_info.User('frances', 'bartleby', 'legal')
user_b.privs.show_privileges()
user_b.greet_user()