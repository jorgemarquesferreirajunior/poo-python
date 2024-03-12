# Abstracao
# Log


class Log:
    def _log(self, msg):
        raise NotImplementedError("Implemente o metodo log")

    def log_error(self, msg):
        return self._log(f"Error: {msg}")

    def log_success(self, msg):
        return self._log(f"Success: {msg}")


class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")


if __name__ == "__main__":
    log = LogPrintMixin()
    log.log_error("qualquer coisa")
    log.log_success("Que legal")
