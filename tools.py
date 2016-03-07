from datetime import datetime

class timer:
    start_time = ''
    def start(self):
        self.start_time = datetime.now()

    def end(self):
        end_timer = datetime.now()
        return (end_timer - self.start_time).total_seconds()
