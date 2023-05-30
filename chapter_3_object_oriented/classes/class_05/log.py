from pathlib import Path

LOG_PATH = Path(__file__).parent

LOG_FILE = f'{LOG_PATH}\log.txt'

class Log:
    def _log(self, message):
        raise NotImplementedError('Implement the log method!')
    
    def log_error(self, message):
        return self._log(f'Error: {message}')
    
    def log_success(self, message):
        return self._log(f'Success: {message}')
    
class LogFileMixin(Log):
    def _log(self, message):
        formatted_message = f'{message} ({self.__class__.__name__})'
        print('Saving to log: ', formatted_message)
        with open(LOG_FILE, 'a') as file:
            file.write(formatted_message)
            file.write('\n')

class LogPrintMixin(Log):
    def _log(self, message):
        print(f'{message} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Test error')
    lp.log_success('Test success')
    lf = LogFileMixin()
    lf.log_error('Test error')
    lf.log_success('Test success')
