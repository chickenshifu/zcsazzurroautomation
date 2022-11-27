from httphandler import HttpHandler


httpHandler = HttpHandler()

try:
    httpHandler.init_session()

    httpHandler.login()

    httpHandler.get_user_id()

    httpHandler.get_plant_list()

    httpHandler.get_plant_info()
    
except Exception as e:
    print(f'Something went wrong. \n {e}')