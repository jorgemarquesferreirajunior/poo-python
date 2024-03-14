# from log import LogPrintMixin, LogFileMixin

# log = LogPrintMixin()
# log.log_error("qualquer coisa")
# log.log_success("Que legal")

# lf = LogFileMixin()
# lf.log_error("qualquer coisa")
# lf.log_success("Que legal")


from eletronico import Smartphone

xiaomi = Smartphone("Xiaomi 10S")
iphone = Smartphone("Iphone 14")

xiaomi.ligar()
iphone.desligar()
