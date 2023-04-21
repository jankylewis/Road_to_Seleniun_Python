import logging as log


# this utility will log information of test scripts to console

class LogGenerating:

    @staticmethod
    def log_generating():
        log.basicConfig(filename=".\\logs\\automation.log",
                        format="%(asctime)s: %(levelname)s: %(message)s",
                        datefmt="%m%d%Y %I:%M:%S %p")
        logger = log.getLogger()
        logger.setLevel(log.INFO)
        return logger
