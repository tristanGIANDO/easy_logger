"""
Copyright (c) 2023 tristanGIANDO

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
