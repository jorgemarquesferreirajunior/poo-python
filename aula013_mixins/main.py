from log import LogPrintMixin, LogFileMixin

log = LogPrintMixin()
log.log_error("qualquer coisa")
log.log_success("Que legal")

lf = LogFileMixin()
lf.log_error("qualquer coisa")
lf.log_success("Que legal")
