import uuid

def make_uuid():
    uid = str(uuid.uuid4())
    return uid

class User() :
    uid = ''
    def __init__(self):
        self.uid = make_uuid()
