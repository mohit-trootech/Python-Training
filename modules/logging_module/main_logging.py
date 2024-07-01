import logging
import logging.handlers as handlers
from pathlib import Path
from typing import List

# import time


def configure_logger():
    file_handler = _get_file_handler()
    log_handlers: List[logging.Handler] = [logging.StreamHandler(), file_handler]
    logging.basicConfig(
        level="INFO",
        format="[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        handlers=log_handlers,
    )


def _get_file_handler() -> handlers.RotatingFileHandler:
    log_path_str = "logs/my_app.log"
    log_path = Path(log_path_str)
    _rotate_existing_log(log_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    return handlers.RotatingFileHandler(
        log_path,
        maxBytes=512,
        backupCount=5,
        # don't append to existing file, instead create a new
        mode="w",
    )


def _rotate_existing_log(log_path: Path):
    """
    If log file already exists, rotate it out of the way into an 'old' directory
    :param log_path:
    :return:
    """
    if log_path.exists():
        old_log_paths = log_path.parent / "old"
        old_log_paths.mkdir(parents=True, exist_ok=True)
        i = 1
        old_log_name = old_log_paths / (log_path.name + f".{i}")
        while old_log_name.exists():
            i += 1
            old_log_name = old_log_paths / (log_path.name + f".{i}")
        log_path.rename(old_log_name)


# for i in range(5):
#     configure_logger()
#     logger = logging.getLogger(__name__)
#     logger.info("hello world")
#     time.sleep(0.5)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(name)s - %(asctime)s - %(levelname)s - %(message)s",
)
print("Logging Messages Example")
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")


def test():
    logging.error("This is an error message")
    logging.critical("This is a critical message")


# print(logging.__dir__())
logging.fatal("This is an Fatal message")
logging.log(100, "This is Most critical error")
