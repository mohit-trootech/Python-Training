"""
logger exercise to log the data of user signup signin
"""

import logging


def create_log(user, log_message):
    logging.basicConfig(
        level=logging.INFO,
        filename=f"logs/{user}.log",
        filemode="a",
        format="%(name)s - %(asctime)s - %(levelname)s - %(message)s",
    )
    logger = logging.getLogger(f"{user.capitalize()} Logger Details")
    logger.log(logging.INFO, log_message)


option = int(input("Press 1 for Signup & 2 for Signin"))
if option == 1:
    username = input("Enter Username: ")
    print(create_log(username.strip(), "User SignedUp Successfully"))
if option == 2:
    username = input("Enter Username: ")
    print(create_log(username.strip(), "User Signed Successfully"))
