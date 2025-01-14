import os
import shutil
import logging

logging.basicConfig(
    filename="delete_template_log.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def delete_item_in_directory(item_name, root_path, is_folder=False):
    # Mencari item di seluruh subfolder di dalam root_path
    for root_dir, subdirs, files in os.walk(root_path):
        # Cek apakah item yang dicari ada di dalam subfolder atau folder saat ini
        if is_folder:
            # Cek apakah item adalah folder dan cocok dengan nama yang dicari
            item_path = os.path.join(root_dir, item_name)
            if os.path.isdir(item_path):
                try:
                    # Cek apakah folder kosong atau tidak
                    if not os.listdir(item_path):  # Jika folder kosong
                        os.rmdir(item_path)
                        print(f"[INFO] Folder kosong '{item_path}' berhasil dihapus.")
                        logging.info(f"Folder kosong '{item_path}' berhasil dihapus.")
                    else:
                        # Folder tidak kosong, hapus dengan semua isinya
                        shutil.rmtree(item_path)
                        print(f"[INFO] Folder beserta isinya '{item_path}' berhasil dihapus.")
                        logging.info(f"Folder beserta isinya '{item_path}' berhasil dihapus.")
                except Exception as e:
                    print(f"[ERROR] Terjadi kesalahan saat menghapus folder '{item_path}': {e}")
                    logging.error(f"Terjadi kesalahan saat menghapus folder '{item_path}': {e}")
        else:
            # Cek apakah item adalah file dan cocok dengan nama yang dicari
            item_path = os.path.join(root_dir, item_name)
            if os.path.isfile(item_path):
                try:
                    os.remove(item_path)  # Menghapus file
                    print(f"[INFO] File '{item_path}' berhasil dihapus.")
                    logging.info(f"File '{item_path}' berhasil dihapus.")
                except Exception as e:
                    print(f"[ERROR] Terjadi kesalahan saat menghapus file '{item_path}': {e}")
                    logging.error(f"Terjadi kesalahan saat menghapus file '{item_path}': {e}")

def main():
    print("Pilih opsi untuk menghapus:")
    print("1. Hapus file")
    print("2. Hapus folder")
    print("3. Hapus file dan folder dengan nama yang sama")

    try:
        choice = int(input("\nMasukkan pilihan (1/2/3): ").strip())
        
        if choice not in [1, 2, 3]:
            print("[ERROR] Pilihan tidak valid!")
            return

        root_path = input("Masukkan path induk tempat mencari file/folder: ").strip()
        
        if not os.path.isdir(root_path):
            print(f"[ERROR] Path induk '{root_path}' tidak valid atau bukan folder.")
            logging.error(f"Path induk '{root_path}' tidak valid atau bukan folder.")
            return

        item_name = input("Masukkan nama file/folder yang ingin dihapus: ").strip()

        if choice == 1:
            # Hapus file dengan nama yang sesuai
            delete_item_in_directory(item_name, root_path, is_folder=False)
        elif choice == 2:
            # Hapus folder dengan nama yang sesuai
            delete_item_in_directory(item_name, root_path, is_folder=True)
        elif choice == 3:
            # Hapus file dan folder dengan nama yang sesuai
            delete_item_in_directory(item_name, root_path, is_folder=True)
            delete_item_in_directory(item_name, root_path, is_folder=False)

    except ValueError:
        print("[ERROR] Pilihan tidak valid!")
        logging.error("Input pilihan tidak valid.")

if __name__ == "__main__":
    main()
