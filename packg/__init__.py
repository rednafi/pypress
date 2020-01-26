# Demo of a logger in __init_.py
import logging

logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("packg/debug.log"), logging.StreamHandler()],
)
