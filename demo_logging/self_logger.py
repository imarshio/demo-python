import logging
logging.basicConfig(level=logging.INFO)
logging.info("logging info")
logging.warning("logging warn")
logging.error("logging error")


logger = logging.getLogger(__name__)
logger.info("logger info")
logger.warning("logger warn")
logger.error("logger error")