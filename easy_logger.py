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

class CustomLogger:
    def __init__(self, log_file: str) -> None:
        """
         Initialize the logger and log the file. This is called by __init__
         and should not be called directly

         Args:
            log_file: Path to the log
        """
        self._log_file = log_file
        if not log_file:
            raise FileNotFoundError(
                "Need a file path to continue (your/path/logs.log)"
            )

    def _write_log(self, message: str, level: str) -> None:
        """
         Write a log message to the log file. This is a convenience method for
         use in unit tests.

         Args:
            message: The message to write to the log file.
            level: The level of the message to write ( INFO WARN ERROR etc
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_message = f"{timestamp} - {level}: {message}"

        with open(self._log_file, "a") as file:
            file.write(log_message + "\n")

    def info(self, message: str) -> None:
        """
         Write a message to the log.
         This is a convenience method for _write_log ( message " INFO " )

         Args:
            message: The message to write
        """
        self._write_log(message, "INFO")

    def warning(self, message: str) -> None:
        """
         Write a warning message to the log.
         This is a convenience method for _write_log ( message " WARNING " )

         Args:
            message: The message to write
        """
        self._write_log(message, "WARNING")

    def error(self, message: str) -> None:
        """
         Write an error message to the log.
         This is a convenience method for _write_log with the ERROR level.

         Args:
            message: The message to write to the log ( string
        """
        self._write_log(message, "ERROR")


if __name__ == "__main__":
    logger = CustomLogger(log_file="your/path/logs.log")

    logger.info("Some very cool info")
    logger.error("Some very bad error")
