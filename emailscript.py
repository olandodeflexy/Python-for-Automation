def define_new_email(email, old_domain, new_domain):
    if "@" + old_domain in email:
         index = email.index("@" + old_domain)
         new_email = email[:index] + "@" + new_domain
         return new_email
    return email

 

print(define_new_email("olandodeflexy@yahoo.com", "yahoo.com", "gmail.com"))
print(define_new_email("olandodeflexy@yahoo.com", "yahoo.com", "hotmail.com"))
