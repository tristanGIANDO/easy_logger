**Copyright (c) 2023 tristanGIANDO**

*Permission is hereby granted, free of charge, to any person obtaining a copy*
*of this software and associated documentation files (the "Software"), to deal*
*in the Software without restriction, including without limitation the rights*
*to use, copy, modify, merge, publish, distribute, sublicense, and/or sell*
*copies of the Software, and to permit persons to whom the Software is*
*furnished to do so, subject to the following conditions:*

*The above copyright notice and this permission notice shall be included in all*
*copies or substantial portions of the Software.*

*THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR*
*IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,*
*FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE*
*AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER*
*LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,*
*OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE*
*SOFTWARE.*

# EASY_LOGGER
A very simple logger that uses very few libraries

##
The script is written in **Python 3**.

### INSTALL
Download `easy_logger.py` and add it to your packages.

## INSTRUCTIONS FOR USE
```py
from easy_logger import EasyLogger

if __name__ == "__main__":
    logger = EasyLogger(log_file=r"your\path\logs.log")

    logger.info("Some very cool info")
    logger.error("Some very bad error")
```

## PARAMETERS
Here are all the arguments to fill in before running the script.

|         Parameter           |   Type    |                                                                    Description                                                                                         |
|:---------------------------:|:---------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         log_file            |    str    | The file in which you want to store the logs ( eg : `your\path\logs.log` ). Note that the file doesn't have to exist before the class is initialised, but the folders do.  |
