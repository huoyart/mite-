import os
import shutil
import keyboard
import time

def get_next_folder_name(base_path, base_name):
    """
    获取备份文件夹的下一个可用名称。
    """
    index = 1
    folder_name = base_name
    while os.path.exists(os.path.join(base_path, folder_name)):
        index += 1
        folder_name = f"{base_name[:-2]}{index:02d}"
    return folder_name


def copy_folder():
    source_folder = os.path.join(os.getcwd(), '争取不饿死')
    backup_base_path = os.path.join(os.getcwd(), 'backup')

    if not os.path.exists(source_folder):
        print("源文件夹不存在:", source_folder)
        return

    try:
        # 确保 backup 目录存在
        os.makedirs(backup_base_path, exist_ok=True)
        now = time.localtime()
        # 生成目标文件夹名称
        target_folder_name = get_next_folder_name(backup_base_path, "争取不饿死")
        target_folder = os.path.join(backup_base_path, target_folder_name)

        # 复制文件夹
        shutil.copytree(source_folder, target_folder)
        print(time.strftime("%H:%M:%S", now)+f"已成功复制文件夹到: {target_folder}")

    except Exception as e:
        print("复制文件夹时出错:", e)


def main():
    print("按下 F9 键即可复制文件夹...")
    keyboard.add_hotkey("F9", copy_folder)

    # 保持脚本运行
    keyboard.wait("F10")  # 按下 ESC 键退出


if __name__ == "__main__":
    main()
