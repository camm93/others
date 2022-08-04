import logging as log


log.basicConfig(level=log.DEBUG,
                format="%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s",
                datefmt="%I:%M:%S %p",
                handlers=[
                    log.FileHandler('../crud.log'),
                    log.StreamHandler()
                ])


if __name__ == "__main__":
    # Testing logger
    log.debug('Debug level message')
    log.info('Info level message')
    log.warning('Warning level message')
    log.error('Error level message')
    log.critical('Critical level message')
