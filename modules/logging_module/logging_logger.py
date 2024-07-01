import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="newest.log",
    filemode="w",
    format="%(name)s - %(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("MyApp")
logger.log(100, "this is temporary log")
