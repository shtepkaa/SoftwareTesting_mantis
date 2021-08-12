def test_signup_new_account(app):
    username = "user1"
    # username = app.generator.random_name_of_project("start", 7)
    password = "test"
    # email = username + "@localhost"
    app.james.ensure_user_exists(username, password)
    # app.signup.new_user(username, email, password)
    # assert app.soap.can_login(username, password)