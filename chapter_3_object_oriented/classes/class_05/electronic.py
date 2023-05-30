from log import LogFileMixin

class Electronic:
    def __init__(self, name):
        self._name = name
        self._connected = False

    def to_connect(self):
        if not self._connected:
            self._connected = True
    
    def to_disconnect(self):
        if self._connected:
            self._connected = False

class Smartphone(Electronic, LogFileMixin):
    def to_connect(self):
        super().to_connect()

        if self._connected:
            message = f'{self._name} is connected.'
            self.log_success(message)

    def to_disconnect(self):
        super().to_disconnect()

        if not self._connected:
            message = f'{self._name} is disconnect.'
            self.log_error(message)