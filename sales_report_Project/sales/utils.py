import uuid

def generate_code():
    code= str(uuid.uuid4()).replace('_','')[:12]
    return code