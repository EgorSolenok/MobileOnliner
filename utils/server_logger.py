import config
import os
from datetime import datetime


class ServerLogger:
    __logs_path = os.path.abspath(os.path.join(os.getcwd(), 'logs', ''))
    __logs_storage = os.path.join(__logs_path, "")
    __log_name = (str(datetime.now())[2:16]).replace(':', '').replace(' ', '')

    def get_logs(driver):
        server_logs = driver.get_log('server')
        log_messages = list(map(lambda log: log['message'], server_logs))
        amount_logs = len(log_messages)
        logs_file = open(f'{ServerLogger.__logs_storage}srv-{ServerLogger.__log_name}.log', 'w')
        for i in range(amount_logs):
            logs_file.write((f"{log_messages[i]}\n"))
        logs_file.close()
