class diagnose(object):
    def __init__(self):
        self._errors = {}

    def add_error(self, module, error):
        try:
            self._errors[module].append(error)
        except KeyError:
            self._errors[module] = []
            self._errors[module].append(error)

    def get_errors(self, module="*"):
        if module == "*" and len(self._errors) > 0:
            return self._errors
        else:
            try:
                return {module: self._errors[module]}
            except KeyError:
                return None
            
