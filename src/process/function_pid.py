import psutil


def get_list_proc():
    proc_list = []
    for proc in psutil.process_iter():
        try:
            proc_info = proc.as_dict(attrs=["pid", "name", "username"])
            proc_info["vms"] = proc.memory_info().vms / (1024 * 1024)

            proc_list.append(proc_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    pid_list = sorted(proc_list, key=lambda proc_obj: proc_obj["vms"], reverse=True)

    return pid_list


def get_pid():
    list_process_name = []
    for proc in psutil.process_iter():
        proc_dict = proc.as_dict(attrs=["pid", "name", "cpu_percent"])
        list_process_name.append(proc_dict)

    for i in list_process_name:
        print(i)

    print("\n* * * Top 5 process with highest memory usage * * *\n")
    run_proc_list = get_list_proc()
    for i in run_proc_list[:5]:
        print(i)


# for msg in get_list_proc():
#     print(str(msg))
