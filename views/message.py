class Message:

    def __new__(self, type, text):
        if type not in ["info", "success", "warning", "error"]:
            return None
        new = object.__new__(self)
        return new

    def __init__(self, type, text):
        self.type = type
        self.text = text
