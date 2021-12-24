import config


def create_logs_file(driver):
    server_logs = driver.get_log('server')
    log_messages = list(map(lambda log: log['message'], server_logs))
    amount_logs = len(log_messages)
    logs_file = open(f'svr-{config.FILE_LOG_NAME}.log', 'w')
    for i in range(amount_logs):
        logs_file.write((f"{log_messages[i]}\n"))
    logs_file.close()