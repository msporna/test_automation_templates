import logging


class Logger:

    def log_info(info_msg):
        logging.info(info_msg)

    def log_warning(warning_msg):
        logging.warning(warning_msg)

    def log_error(error_msg):
        logging.error(error_msg)