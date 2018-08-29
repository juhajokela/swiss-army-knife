class Maybe(object):

    def __init__(self, value):
        self.value = value

    def then(self, function):
        if self.value is None:
            return self
        return Maybe(function(self.value))

    def __str__(self):
        return 'Maybe({})'.format(str(self.value))

    def __repr__(self):
        return 'Maybe({})'.format(repr(self.value))
