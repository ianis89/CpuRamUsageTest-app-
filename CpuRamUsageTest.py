import os
import psutil
import sys


def main():
    print("CPU usage is {} %".format(get_cpu_usage_pct()))
    print("CPU frequency is {} MHz".format(get_cpu_frequency()))
    print("CPU temperature is {} degC".format(get_cpu_temp()))
    print("RAM usage is {} MB".format(int(get_ram_usage() / 1024 / 1024)))
    print("RAM total is {} MB".format(int(get_ram_total() / 1024 / 1024)))
    print("RAM usage is {} %".format(get_ram_usage_pct()))
    print("Swap usage is {} MB".format(int(get_swap_usage() / 1024 / 1024)))
    print("Swap total is {} MB".format(int(get_swap_total() / 1024 / 1024)))
    print("Swap usage is {} %".format(get_swap_usage_pct()))


def get_cpu_usage_pct():
    return psutil.cpu_percent(interval=0.5)


def get_cpu_frequency():
    return int(psutil.cpu_freq().current)


def get_cpu_temp():
    result = 0.0

    if os.path.isfile("/sys/class/thermal/thermal_zone0/temp"):
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            line = f.readline().strip()
        if line.isdigit():
            result = float(line) / 1000

    return result


def get_ram_usage():
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)


def get_ram_total():
    return int(psutil.virtual_memory().total)


def get_ram_usage_pct():
    return psutil.virtual_memory().percent


def get_swap_usage():
    return int(psutil.swap_memory().used)


def get_swap_total():
    return int(psutil.swap_memory().total)


def get_swap_usage_pct():
    return psutil.swap_memory().percent


filename = open("output file.txt", "w")
sys.stdout = filename
# # print ("Anything printed will go to the output file.txt")


if __name__ == "__main__":
    main()
