'''Task 5: Mini Login Validation users = [ {"username": "admin", "password": "1234"}, {"username": "john", "password": "abcd"} ] Requirements: Get username and password from user.
Check credentials. Display: Login Successful Invalid Username Invalid Password'''



users = [ {"username": "admin", "password": "1234"},
          {"username": "john", "password": "abcd"} ]
username=input("enter the username : ")
password=input("enter the password : ")

d=False
for user in users:
    if user["username"].lower()== username.lower() and user["password"].lower()==password.lower():
        print("Login Successful")
        d=True
        break
if not d:
    print("Invalid Username Invalid Password")
    
