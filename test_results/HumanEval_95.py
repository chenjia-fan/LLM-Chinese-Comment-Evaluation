def check_dict_case(dict):
    if not dict:
        return False
    
    keys = list(dict.keys())
    
    if not all(isinstance(key, str) for key in keys):
        return False
    
    if all(key.islower() for key in keys):
        return True
    
    if all(key.isupper() for key in keys):
        return True
    
    return False