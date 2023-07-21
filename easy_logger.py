import datetime

class EasyLogger:
    def __init__(self, log_file):
        self._log_file = log_file
        if not log_file:
            raise FileNotFoundError("Need a file path to continue (your\path\logs.log)")

    def info(self, message):
        self.write_log(message, "INFO")

    def warning(self, message):
        self.write_log(message, "WARNING")

    def error(self, message):
        self.write_log(message, "ERROR")

    def write_log(self, message, level):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_message = f"{timestamp} - {level}: {message}"

        with open(self._log_file, "a") as file:
            file.write(log_message + "\n")

if __name__ == "__main__":
    logger = EasyLogger(log_file=r"your\path\logs.log")

    logger.info("Some very cool info")
    logger.error("Some very bad error")
