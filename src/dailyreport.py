from tabulate import tabulate
import task
import sys
import os

laporan_pengeboran ={
    'UG0001' : {'Mesin':'CS1000',
                'Lokasi':'Underground', 
                'Kemajuan': 30.5, 
                'Status':'STOP',
                'Kedalaman Akhir':30.5
                },
    'UG0002' : {'Mesin':'CS1000',
                'Lokasi':'Underground', 
                'Kemajuan': 12, 
                'Status':'RUNNING',
                'Kedalaman Akhir':0
                },
    'SF0001' : {'Mesin':'CS2000',
                'Lokasi':'Surface',
                'Kemajuan': 15, 
                'Status':'RUNNING',
                'Kedalaman Akhir':0
                }
}

def clear_screen():
    """
    A function to clean the user interface
    """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')


def main():
    global laporan_pengeboran
    
    clear_screen()
    
    print (
    '''Laporan Pengeboran Eksplorasi
    Pilih menu yang ingin anda jalankan:
    1. Menampilkan Data 
    2. Menambah Data 
    3. Mengubah Data
    4. Menghapus Data
    5. Keluar
         '''
    )
    while True:
        choice =task.valid_int('Masukkan pilihan anda: ')
        if choice == 1:
            task.show_choice(laporan_pengeboran)
        elif choice == 2:
            task.create_choice(laporan_pengeboran)
        elif choice == 3:
            task.update_choice(laporan_pengeboran)
        elif choice == 4:
            task.delete_choice(laporan_pengeboran)
        elif choice == 5:
            sys.exit()
        else:
            print ('Pilihan anda tidak tersedia masukan (1-5): ')
            continue
       
        

main ()
