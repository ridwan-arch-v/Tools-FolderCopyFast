import os
import shutil
import logging

logging.basicConfig(
    filename="copy_template_log.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def copy_template_to_folders(template_path, root_folder):
    if not os.path.exists(template_path):
        logging.error(f"Template folder '{template_path}' tidak ditemukan.")
        print(f"ERROR: Template folder '{template_path}' tidak ditemukan.")
        return
    
    if not os.path.isdir(root_folder):
        logging.error(f"Root folder '{root_folder}' tidak ditemukan atau bukan folder.")
        print(f"ERROR: Root folder '{root_folder}' tidak ditemukan atau bukan folder.")
        return

    template_name = os.path.basename(template_path)
    print(f"\n{template_name} akan dicopy ke seluruh folder yang ada di dalam folder {os.path.basename(root_folder)}")

    for root_dir, subdirs, files in os.walk(root_folder):
        for subdir in subdirs:
            destination_folder = os.path.join(root_dir, subdir)
            dest_path = os.path.join(destination_folder, template_name)
            
            print(f"\nMenyalin {template_name} ke folder {destination_folder}...")
            logging.info(f"Menyalin {template_name} ke folder {destination_folder}...")
            
            if not os.path.exists(dest_path):
                try:
                    if os.path.isdir(template_path):
                        shutil.copytree(template_path, dest_path)
                    else:
                        shutil.copy(template_path, dest_path)
                    
                    print(f"[INFO] Template berhasil disalin ke: {dest_path}")
                    logging.info(f"Template berhasil disalin ke: {dest_path}")
                except Exception as e:
                    print(f"[ERROR] Terjadi kesalahan saat menyalin ke {dest_path}: {e}")
                    logging.error(f"Terjadi kesalahan saat menyalin ke {dest_path}: {e}")
            else:
                print(f"[WARNING] Folder {dest_path} sudah ada, tidak perlu disalin.")
                logging.warning(f"Folder {dest_path} sudah ada, tidak perlu disalin.")

def main():
    template_folder = input("Masukkan path folder template yang ingin disalin: ").strip()
    root_folder = input("Masukkan path folder induk tempat folder-template akan disalin: ").strip()

    print(f"\nPerhatian: Folder {os.path.basename(template_folder)} akan disalin ke semua subfolder yang ada di dalam {os.path.basename(root_folder)}")

    proceed = input("\nApakah Anda ingin melanjutkan? (y/n): ").strip().lower()
    if proceed != 'y':
        print("Proses dibatalkan.")
        logging.info("Proses dibatalkan oleh pengguna.")
        return

    copy_template_to_folders(template_folder, root_folder)
    print("\nProses selesai. Cek file log untuk detail lebih lanjut.")

if __name__ == "__main__":
    main()
