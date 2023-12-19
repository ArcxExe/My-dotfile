import os
import random
import subprocess
import sys

path_wallpaper = "/home/arcx/wallpaper/"
# path to wallpaper /home/{USER}/path/to/wallpaper
path_file = "/home/arcx/.config/hypr/hyprpaper.conf"
# path to hyprpaper /home/{USER}/path/to/hyprpaper


def start():
    # subprocess.Popen(
    #     ["nohup","/usr/bin/hyprpaper","&"],
    #     stdout=subprocess.PIPE,
    #     stderr=subprocess.PIPE,
    #     stdin=subprocess.PIPE,
    # )
    subprocess.Popen(
        ["nohup", "/usr/bin/hyprpaper"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
    )


def write_config(file):
    with open(path_file, "w") as f:
        f.write(
            f"preload = {path_wallpaper}{file} \nwallpaper = VGA-1,{path_wallpaper}{file}"
        )
    # subprocess.Popen(
    #     ["hyprpaper"],
    #     stdout=subprocess.PIPE,
    #     stderr=subprocess.PIPE,
    #     stdin=subprocess.PIPE,
    # )
    start()


def wallpaper_next():
    os.system("pkill hyprpaper")
    with open(path_file, "r") as conf:
        try:
            index_last_wallpaper = os.listdir(path_wallpaper).index(
                conf.readline().strip().split("/")[-1] # Получаем последнее изображение
            )# Получаем индекс из этого изображения
        except ValueError:
            index_last_wallpaper = 0 
    try:
        next_wallpaper = os.listdir(path_wallpaper)[index_last_wallpaper+1]
    except IndexError:
        next_wallpaper = os.listdir(path_wallpaper)[0]


    write_config(next_wallpaper)

def wallpaper_random():
    os.system("pkill hyprpaper")

    random_file = random.choice([f for f in os.listdir(path_wallpaper)])
    write_config(random_file)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        wallpaper_next()
    elif "random" in sys.argv:
        wallpaper_random()
    elif "start" in sys.argv:
        start()

