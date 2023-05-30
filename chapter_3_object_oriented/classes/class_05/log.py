class Log:
    def log(self, msg):
        raise NotImplementedError('Implement the log method!')
    
class LogFileMixin(Log):
    def log(self, msg):
        print(msg)

if __name__ == '__main__':
    l = LogFileMixin()
    l.log('Test method.')