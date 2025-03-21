current_model = None

def get_current_model():
    global current_model
    if current_model is None:
        raise ValueError("Current model is not set")
    return current_model

def set_current_model(model):
    global current_model
    current_model = model