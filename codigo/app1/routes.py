from controllers import RegisterControllers, LoginControllers,PhoneControllers

routes = {
"register": "/register", "register_controllers": RegisterControllers.as_view("register_app"),
"login": "/login", "login_controllers": LoginControllers.as_view("login_app"),
"phone":'/phone',"Phone_controllers":PhoneControllers.as_view("phone_app"),
}