import os
from datetime import date, datetime, timedelta
class LogsChecker:
    def __init__(self):
        pass
    def create_timestamp(self):
        day = date.today()
        day = day.strftime("%d%m%Y")
        hour = datetime.now()
        hour = hour.strftime("%H%M%S")
        timestamp = f"{day}_{hour}"
        return timestamp
    def failed_list_from_logs(self, path, string_to_catch):
        scripts_that_failed = []
        i = 0
        for file in os.listdir(path):
            f = os.path.join(path, file)
            file_modification_time = datetime.fromtimestamp(os.path.getmtime(f))
            if file in excluded_files or file_modification_time >= offset:
                continue
            i += 1
            str_found = False
            with open(f) as f:
                for line in f:
                    if string_to_catch in line:
                        str_found = True
                        continue
                if str_found is False:
                    scripts_that_failed.append(file)
        return scripts_that_failed
    def failed_from_email(self):
        pass
    def list_to_txt(self, save_path, list_of_files, file_suffix="check"):
        timestamp = self.create_timestamp()
        failed_count = len(list_of_files)
        with open(
            f"{save_path}{timestamp}_{failed_count}_failed_{file_suffix}.txt", "x"
        ) as f:
            for item in list_of_files:
                f.write(f"{item}\n")
if __name__ == "__main__":
    # path to save
    save_path = "C:\\kodab\\Py\\"
    # logs paths
    proc_path = "H:\\OOH\\HDP\\P1\\R_scripts\\_Logi_Autorun\\R\\"
    exit_path = "H:\\OOH\\HDP\\P1\\R_scripts\\_Logi_Autorun\\WinSCP\\"
    # files to exclude
    excluded_files = ['EurostatDownload_log.txt', 'EurostatDownload_log2.txt']
    # date offset
    offset = datetime.today() - timedelta(days=90)
    logs_checker = LogsChecker()
    list_of_fails_proc = logs_checker.failed_list_from_logs(proc_path, "> proc.time()")
    list_of_fails_exit = logs_checker.failed_list_from_logs(exit_path, "Exit code: 0")
    logs_checker.list_to_txt(save_path, list_of_fails_proc, "proc")
    logs_checker.list_to_txt(save_path, list_of_fails_exit, "exit")