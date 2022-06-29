import logging

class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename=".\\Logs\\automation.log",
        #                     format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # logger=logging.getLogger()
        # logger.setLevel(logging.INFO)

        log = logging.getLogger()
        fh = logging.FileHandler(".\\Logs\\automation.log")
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter("[%(asctime)s:%(msecs)03d %(levelname)s]" + " %(message)s", datefmt="%d-%m-%Y-%H:%M:%S")
        fh.setFormatter(formatter)
        log.addHandler(fh)

        # ch = logging.StreamHandler()
        # ch.setLevel(logging.DEBUG)
        # ch.setFormatter(formatter)
        # log.addHandler(ch)

        return log