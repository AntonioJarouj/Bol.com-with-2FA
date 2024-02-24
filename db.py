# productie database
def connect_to_database():
    return {
        "host" : "database",
        "port" : "3306",
        "database" : "user",
        "user" : "secure-logix-web",
        "password": "12345678910"        
    }

# voor testen:    
# def connect_to_database():
#     return {
#         "host" : "localhost",
#         "port" : "3306",
#         "database" : "test_user",
#         "user" : "testuser",
#         "password": "password"        
#     }