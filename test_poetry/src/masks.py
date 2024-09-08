import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"../logs/src.masks.log", mode="w")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    logger.info("Маскируем номер карты")
    return f"{card[0:7]}** **** {card[-4:]}"


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    logger.info("Маскируем номер счета")
    return "*" * len(account[13:-4]) + account[-4:]
