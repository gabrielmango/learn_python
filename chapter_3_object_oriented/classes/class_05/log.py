class Log:
    def _log(self, message):
        raise NotImplementedError('Implement the log method!')
    
    def log_error(self, message):
        return self._log(f'Error: {message}')
    
    def log_success(self, message):
        return self._log(f'Success: {message}')
    
class LogFileMixin(Log):
    def _log(self, message):
        print(message)

class LogPrintMixin(Log):
    def _log(self, message):
        print(f'{message} ({self.__class__.__name__})')

if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('Test error method.')
    l.log_success('Test sucess method.')
