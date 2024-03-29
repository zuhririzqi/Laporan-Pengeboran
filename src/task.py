from tabulate import tabulate

## Fungsi untuk validasi input
#1 Validasi input key BHID
def valid_bhid (bhid):
    """Fungsi untuk memastikan penginputan BHID sesuai dengan format
        
    Parameters:
        pattern (regular expression): format penulisan BHID (2 huruf 4 angka)
        bhid (string): unique key database

    Return:
        bhid yang telah sesuai dengan format
    """
    while True:
        import re
        #Meminta penginputan BHID
        bhid = input('Input BHID: ').upper()
       
        if re.match ((r'[A-Za-z]{2}\d{4}'),bhid) and len(bhid) == 6:
            break
        else:
            print('masukkan kombinasi 2 huruf dilanjutkan 4 angka')
            continue
    return bhid

#2 Validasi input status
def valid_status (status):
    """Fungsi untuk memastikan penginputan STATUS sesuai dengan format
        
    Parameters:
        pattern (regular expression): format RUNNING/STOP 
        status (string): menunjukkan status pengeboran apah masih berjalan atau sudah selesai

    Return:
        status yang telah sesuai dengan format
    """
    while True:
        #Meminta penginputan STATUS
        status = input('Input Status: ').upper()

        if status == 'STOP' or status == 'RUNNING':
            status = status
            break
        else:
            print ('Input status RUNNING/STOP saja')
            continue
    return status


#3 Validasi float
def valid_float (task):
    """Fungsi untuk memastikan penginputan berupa tipe float positif
        
    Parameters:
        nums (float): hasil input berupa float

    Return:
        nums (float)
    """
    while True:
        try:
            # Meminta input angka
            nums = float (input (task))
            # Jika input bernilai negatif
            if nums > 0 and abs(nums)>0:
                break
            else:
                print ('Angka tidak boleh negatif dan 0')
                continue
        # Jika input bukan angka
        except:
            print ('Hanya masukkan angka')
        continue
    return nums

#4 Validasi alnum
def valid_alnum (task):
    """Fungsi untuk memastikan penginputan berupa huruf dan angka saja
        
    Parameters:
        word (string): hasil input berupa gabungan huruf dan angka

    Return:
        word (string)
    """
    while True:
        #Meminta input kata berupa huruf dan angka
        word = input(task).upper()
        #Jika input kata berupa huruf dan angka
        if word.isalnum():
            break
        #Jika input kata bukan berupa huruf dan angka
        else:
            print ('Hanya masukkan angka dan huruf saja')
            continue
    
    return word

#5 Validasi alpha
def valid_alpha (task):
    """Fungsi untuk memastikan penginputan berupa huruf saja
        
    Parameters:
        word (string): hasil input berupa huruf dan spasi

    Return:
        word (string)
    """
    while True:
        #Meminta input kata berupa huruf 
        word = input(task).title()
        #Jika input kata berupa huruf 
        if word.isalpha():
            break
        #Jika input bukan berupa huruf 
        else:
            print ('Hanya masukkan huruf saja')
            continue
    
    return word
        
#5 Validasi input filter
def find_value (table, value):
    """Fungsi untuk memastikan value yang dicari terdapat pada database
        
    Parameters:
        value (string): hasil input berupa value yang ingin dicari 

    Return:
        True/False
    """
    #Pengecekan apakah value yang dicari ada pada database
    for k, v in table.items():
        #Jika value masih berupa dictionary
        if isinstance(v, dict):
            if find_value(v, value):
                return True
        #Jika value bukan dictionary
        elif v == value:
            return True
    return False

#6 Validasi int
def valid_int (task):
    """Fungsi untuk memastikan penginputan berupa tipe int positif
        
    Parameters:
        nums (int): hasil input berupa angka

    Return:
        nums (int)
    """
    while True:
        try:
            #Meminta inputan berupa angka
            nums = int (input (task))
            #Jika angka negatif
            if nums > 0 and abs(nums)>0:
                break
            else:
                print ('Angka tidak boleh negatif dan nol')
                continue
        except:
            #Jika inputan bukan berupa angka
            print ('Hanya masukkan angka')
        continue
    return nums


## Formatting Tabel
def convert_to_table(data, columns, title):
    """Fungsi untuk mengubah database kedalam format tabel

    """
    # Menampilkan judul tabel
    print(title)

    # Mengubah format data menjadi format tabel
    print(tabulate(data, headers=columns, tablefmt="grid"))

## Menampilkan data dalam format tabel
def show (table):
    """Fungsi untuk menampilkan data pengeboran eksplorasi

    Paramaters:
        table (Dictionary): Database pengeboran.
        data (Nested Dictionary): Data data pengeboran eksplorasi
        columns (list): nama kolom data
        title (string): 
    """

    # Menampilkan database pengeboran ekslporasi dengan format tabel
    convert_to_table(
        data= [[outer, *inner.values()] for outer, inner in table.items()],
        columns=['BHID','Mesin', 'Lokasi', 'Kemajuan','Status','Kedalaman Akhir'],
        title='\nLaporan Pengeboran Eksplorasi\n'
    )


#Fungsi Utama
#1. Fungsi untuk menyajikan tabel
def show_choice (table):
    """Fungsi untuk memberikan pilihan pada data yang ingin disajikan

    Paramaters:
        choose (int): input pilihan penyajian data
    """
    while True:
        print(''' 
-------------------------------------
Pilih data yang ingin anda tampilkan:
1. Laporan Pengeboran Keseluruhan
2. Laporan Pengeboran Sebagian
3. Menu Utama 
-------------------------------------
    '''  )
        #Meminta input pilihan
        choose = valid_int('Masukkan pilihan anda: ')
        #Jika ingin melihat keseluruhan data (1.1)
        if choose == 1:
            show_all(table)
        #Jika ingin melihat data yang sudah terfilter (1.2)
        elif choose == 2:
            show_filtered(table)
        #Jika ingin kembali ke menu utama
        elif choose == 3:
            main_menu()
        #Jika pilihan selain opsi yang tersedia
        else:
            print ('Pilihan anda tidak tersedia masukan (1-3): ')
            continue


#1.1 Menampilkan keseluruhan data
def show_all (table):
    """Fungsi untuk menampilkan keseluruhan data pengeboran
    """
    while True:
        if len(table)>0:
            # Menampilkan seluruh data pada database
            show(table)
            break
        else:
            print ('Database kosong, ingin menambahkan data?')
            while True:
                #Konfirmasi apakah ingin berpindah ke menu menambahkan data
                comfirm = valid_alpha ('Iya/Tidak: ').capitalize()
                #Jika ingin menambah data
                if comfirm == 'Iya':
                    create_choice(table)
                #Jika tetap ingin kembali ke menu utama
                elif comfirm == 'Tidak':
                    show_choice(table)
                else:
                    print ('Pilihan tidak tersedia, hanya masukkan Iya/Tidak')
                    continue 

#1.2 Menampilkan tabel sesuai dengan kondisi yang dipilih
def show_filtered(table):
    ''' Menampilkan nilai yang telah difilter berdasarkan kondisi tertentu
       
    Parameters:
        input_case (int) = pemilihan kondisi untuk filtering
        filtered_table (dictionary) = database yang sudah terfilter
    '''
    while True:
        print (''' 
Data yang ingin di tampilkan:
1. BHID
2. Mesin
3. Lokasi
4. Status
5. Kembali ke menu tampilkan
-----------------------------
        ''')
        
        #Meminta inputan kondisi untuk filtering
        input_case = valid_int('Masukkan pilihan anda: ')
        # Jika memilih berdasarkan BHID
        if input_case == 1:
            show_all(table)
            while True:
                #Meminta input BHID yang ingin ditampilkan
                input_bhid = valid_bhid('bhid')
                #Jika BHID tersedia
                if input_bhid in table.keys():
                    filtered_table = table.copy()
                    filtered_table = dict(filter(lambda item: item[0] == input_bhid, filtered_table.items()))
                    break
                #Jika BHID tidak ada pada database
                else:
                    print ('BHID yang anda cari tidak tersedia!')
                    show_filtered(table)
        #Jika memilih berdasarkan nama mesin
        elif input_case == 2:
            show_all(table)
            while True:
                #Meminta input nama mesin
                input_mesin = valid_alnum ('Masukkan nama mesin: ')
                #Jika mesin tersedia
                if find_value (table,input_mesin):
                    filtered_table = table.copy()
                    filtered_table = dict(filter(lambda item: item[1]['Mesin'] == input_mesin, filtered_table.items()))
                    break
                #Jika mesin tidak tersedia
                else:
                    print ('Mesin yang anda cari tidak tersedia!')
                    show_filtered(table)
        #Jika memilih berdasarkan lokasi pengeboran
        elif input_case == 3:
            show_all(table)
            while True:
                #Meminta input berupa lokasi yang dicari
                input_lokasi = valid_alpha('Input Lokasi yang ingin dicari: ')
                #Jika lokasi tersedia
                if find_value (table,input_lokasi):
                    filtered_table = table.copy()
                    filtered_table = dict(filter(lambda item: item[1]['Lokasi'] == input_lokasi, filtered_table.items()))
                    break
                #Jika lokasi tidak tersedia
                else:
                    print ('Lokasi yang anda cari tidak tersedia')
                    show_filtered(table)
        elif input_case == 4:
            show_all(table)
            while True:
                #Meminta input berupa status yang dicari
                input_status = valid_status('status')
                #Jika status yang dicari tersedia
                if find_value (table,input_status):
                    filtered_table = table.copy()
                    filtered_table= dict(filter(lambda item: item[1]['Status'] == input_status, filtered_table.items()))
                    break
                #Jika status tidak tersedia
                else:
                    print ('Status yang anda cari tidak tersedia')
                    show_filtered(table)
        #Kembali pada fungsi pilihan penyajian
        elif input_case == 5:
            show_choice(table)
        #Jika input kondisi filtering tidak tersedia
        else:
            print ('Pilihan anda tidak tersedia pilih 1-5')
            show_filtered(table)
        show (filtered_table)

   
    
#2. Fungsi untuk menambahkan data baru pada database
def create_choice (table):
    """Fungsi untuk memberi pilihan penambahan data

    Paramaters:
        choose (int): input pilihan penambahan data
    """
    while True:
        print(''' 
----------------------------------------
Apakah anda ingin menambahkan data baru?
1. Tambah data baru
2. Kembali ke menu utama
----------------------------------------
            '''  )
        #Input pilihan penambahan data
        choose = valid_int('Masukkan pilihan anda: ')
        #Jika ingin menambah data
        if choose == 1:
            create (table)
        #Jika ingin kembali ke menu utama
        elif choose == 2:
            main_menu()
        #Jika pilihan tidak tersedia
        else:
            print ('Pilihan anda tidak tersedia masukan (1/2): ')
            continue

#2.1 Penambahan data baru pada database
def create (table):
    """
    Fungsi untuk melakukan penambahan data pada database

    """
    while True:
        show (table)
        print ('Masukkan data yang ingin ditambahan!: ')
        # Meminta inputan bhid
        bhid = valid_bhid('bhid')
        # Jika bhid sudah ada dalam database
        if bhid in table.keys():
            print ('BHID sudah ada, ingin ke menu perbarui data?')
            while True:
                comfirm = valid_alpha ('Iya/Tidak: ').capitalize()
                #Jika ingin merubah data yang sudah ada
                if comfirm == 'Iya':
                    update_choice(table)
                #Jika tetap ingin pada menu tambah data
                elif comfirm == 'Tidak':
                    create_choice(table)
                else:
                    print ('Pilihan tidak tersedia, hanya masukkan Iya/Tidak')
                    continue
        # Jika bhid belum ada dalam database
        else:
            # Input data-data baru
            mesin = valid_alnum ('Masukkan nama mesin: ')
            lokasi = valid_alpha ('Masukkan lokasi: ')
            kemajuan = valid_float('Masukkan kemajuan: ')
            status = valid_status ('Masukkan status: ')
            kedalaman_akhir = 0

            if status =='STOP':
                kedalaman_akhir= kemajuan
            else:
                kedalaman_akhir

            temp_table = table.copy()
            temp_table.update({bhid:{
                    'Mesin':mesin,
                    'Lokasi':lokasi,
                    'Kemajuan': kemajuan,
                    'Status':status,
                    'Kedalaman Akhir':kedalaman_akhir
                }})
            show(temp_table)
            print ('Apakah anda ingin menyimpan data yang baru ditambahkan? ')
            while True:
                #Konfirmasi apakah ingin menyimpan update
                comfirm = valid_alpha ('Iya/Tidak: ').capitalize()
                #Jika ingin menambah data
                if comfirm == 'Iya':
                    table.update({bhid:{
                        'Mesin':mesin,
                        'Lokasi':lokasi,
                        'Kemajuan': kemajuan,
                        'Status':status,
                        'Kedalaman Akhir':kedalaman_akhir
                    }})
                    print('Data berhasil ditambahkan!')
                    create_choice(table)
                #Jika tetap ingin kembali ke menu create
                elif comfirm == 'Tidak':
                    print('Data tidak berhasil ditambahkan!')
                    create_choice(table)
                else:
                    print ('Pilihan tidak tersedia, hanya masukkan Iya/Tidak')
                    continue 
           
  
#3. Pilihan untuk merubah data yang telah tersedia
def update_choice(table):
    """Fungsi untuk memilih data yang akan diperbaharui

    Parameters:
    choose (int) = pilihan menu untuk melakukan perubahan data

    """

    while True:
        print(''' 
----------------------------------
Pilih data yang ingin anda ubah:
1. Laporan Pengeboran Keseluruhan
2. Laporan Pengeboran Sebagian
3. Kembali ke menu utama
----------------------------------
            '''  )
        # Meminta inputan pilihan untuk merubah data
        choose = valid_int ('Masukkan pilihan anda: ')
        # Jika ingin mengubah keseluruhan data
        if choose == 1:
            update_all(table)
        # Jika ingin mengubah data berdasarkan key tertentu
        elif choose == 2:
            update_pars(table)
        #Jika ingin kembali ke menu utama
        elif choose == 3:
            main_menu()
        #Jika pilihan tidak tersedia
        else:
            print ('Pilihan anda tidak tersedia masukan (1-3): ')
            continue

#3.1 Fungsi untuk merubah data keseluruhan
def update_all (table):
    """Fungsi untuk memilih data yang akan 
    diperbaharui secara keseluruhan

    """
    while True:
        if len(table)>0:
            while True:
                show_all (table)
                #Meminta inputan bhid
                bhid = valid_bhid ('bhid')
                #Jika bhid ada dalam database
                if bhid in table.keys():
                    # Meminta inputan data update
                    mesin = valid_alnum ('Masukkan nama mesin: ')
                    lokasi = valid_alpha ('Masukkan lokasi: ')
                    kemajuan = valid_float('Masukkan Kemajuan: ')
                    status = valid_status ('Masukkan Status: ')
                    kedalaman_akhir = 0

                    if status =='STOP':
                        kedalaman_akhir= kemajuan
                    else:
                        kedalaman_akhir
                    #Menyimpan pada tabel sementara
                    temp_table = table.copy()
                    temp_table.update({bhid:{
                            'Mesin':mesin,
                            'Lokasi':lokasi,
                            'Kemajuan': kemajuan,
                            'Status':status,
                            'Kedalaman Akhir':kedalaman_akhir
                        }})
                    show(temp_table)
                    #Konfirmasi apakah ingin menyimpan perubahan
                    print ('Apakah anda ingin menyimpan perubahan data? ')
                    while True:
                        comfirm = valid_alpha ('Iya/Tidak: ').capitalize()
                        #Jika ingin menambah data
                        if comfirm == 'Iya':
                            table.update({bhid:{
                                'Mesin':mesin,
                                'Lokasi':lokasi,
                                'Kemajuan': kemajuan,
                                'Status':status,
                                'Kedalaman Akhir':kedalaman_akhir
                            }})
                            print ('Data berhasil diperbaharui!')
                            update_choice(table)
                        #Jika tetap ingin kembali ke menu update
                        elif comfirm == 'Tidak':
                            print ('Data tidak berhasil diperbaharui!')
                            update_choice(table)
                        else:
                            print ('Pilihan tidak tersedia, hanya masukkan Iya/Tidak')
                            continue 
                #Jika bhid tidak tersedia dalam database
                else:
                    print ('''BHID tidak ada, apakah ingin menambah data?''')
                    while True:
                        #Konfirmasi apakah ingin berpindah pada menu penambahan data
                        comfirm = valid_alpha ('Iya/Tidak: ').capitalize()
                        #Jika ingin menambah data baru
                        if comfirm == 'Iya':
                            create_choice(table)
                        #Jika tetap ingin pada menu ubah data
                        elif comfirm == 'Tidak':
                            update_choice(table)
                        else:
                            print ('Pilihan tidak tersedia, hanya masukkan Iya/Tidak')
                            continue
        #Jika database kosong
        else:
            print ('Database kosong, ingin menambahkan data?')
            while True:
                #Konfirmasi apakah ingin berpindah ke menu menambahkan data
                comfirm = valid_alpha ('Iya/Tidak: ').capitalize()
                #Jika ingin menambah data
                if comfirm == 'Iya':
                    create_choice(table)
                #Jika tetap ingin kembali ke menu update
                elif comfirm == 'Tidak':
                    update_choice(table)
                else:
                    print ('Pilihan tidak tersedia, hanya masukkan Iya/Tidak')
                    continue 


#3.2 Fungsi untuk merubah data sebagian
def update_pars (table):
    """Fungsi untuk memilih data yang akan 
    diperbaharui berdasarkan key yang dipilih
        
    """
    while True:
        if len(table)>0:
            while True:
                show (table)
                print (''' 
--------------------------
Data yang ingin di ubah:
1. Mesin
2. Lokasi
3. Kemajuan
4. Status
5. Kembali ke menu update
--------------------------
                ''')
                #Meminta input key yang akan diubah
                input_case = valid_int('Masukkan pilihan anda: ')
                if input_case in range(1,5):
                    while True:
                        #Meminta input BHID
                        bhid = valid_bhid ('bhid')
                        #Jika bhid ada dalam database
                        if bhid in table.keys():
                            #Jika ingin mengubah mesin
                            if input_case == 1:
                                mesin = valid_alnum('Input nama mesin: ')
                                while True:
                                    confirm = valid_alpha('Apakah anda ingin menyimpan data? (Iya/Tidak)').capitalize()
                                    if confirm == 'Iya':
                                        table[bhid]['Mesin']= mesin
                                        print ('Data sudah berhasil diperbaharui!')
                                        show (table)
                                        update_choice(table)
                                    elif confirm == 'Tidak':
                                        print('Data tidak diperbaharui')
                                        update_choice(table)
                                    else:
                                        print('Hanya masukkan Iya/Tidak!')
                                        continue
                            #Jika ingin mengubah lokasi
                            elif input_case == 2:
                                lokasi = valid_alpha('Input nama lokasi: ')
                                while True:
                                    confirm = valid_alpha('Apakah anda ingin menyimpan data? (Iya/Tidak)').capitalize()
                                    if confirm == 'Iya':
                                        table[bhid]['Lokasi']= lokasi
                                        print ('Data sudah berhasil diperbaharui!')
                                        show (table)
                                        update_choice(table)
                                    elif confirm == 'Tidak':
                                        print('Data tidak diperbaharui')
                                        update_choice(table)
                                    else:
                                        print('Hanya masukkan Iya/Tidak!')
                                        continue
                            #Jika ingin mengubah Kemajuan
                            elif input_case == 3:
                                x = table[bhid]['Status']
                                if x == 'STOP':
                                    kemajuan = valid_float('Masukkan kemajuan: ')
                                    while True:
                                        confirm = valid_alpha('Apakah anda ingin menyimpan data? (Iya/Tidak)').capitalize()
                                        if confirm == 'Iya':
                                            table[bhid]['Kemajuan']= kemajuan
                                            table[bhid]['Kedalaman Akhir']= kemajuan
                                            print ('Data sudah berhasil diperbaharui!')
                                            show (table)
                                            update_choice(table)
                                        elif confirm == 'Tidak':
                                            print('Data tidak diperbaharui')
                                            update_choice(table)
                                        else:
                                            print('Hanya masukkan Iya/Tidak!')
                                            continue  
                                else:
                                    kemajuan = valid_float('Masukkan kemajuan: ')
                                    while True:
                                        confirm = valid_alpha('Apakah anda ingin menyimpan data? (Iya/Tidak)').capitalize()
                                        if confirm == 'Iya':
                                            table[bhid]['Kemajuan']= kemajuan
                                            table[bhid]['Kedalaman Akhir']= 0
                                            print ('Data sudah berhasil diperbaharui!')
                                            show (table)
                                            update_choice(table)
                                        elif confirm == 'Tidak':
                                            print('Data tidak diperbaharui')
                                            update_choice(table)
                                        else:
                                            print('Hanya masukkan Iya/Tidak!')
                                            continue  
                            #Jika ingin mengubah status
                            elif input_case == 4:
                                kemajuan = valid_float('Masukkan kemajuan: ')
                                status = valid_status('status')
                                kedalaman_akhir = 0
                                while True:
                                    confirm = valid_alpha('Apakah anda ingin menyimpan data? (Iya/Tidak)').capitalize()
                                    if confirm == 'Iya':
                                        table[bhid]['Kemajuan']= kemajuan
                                        table[bhid]['Status']= status

                                        if status =='STOP':
                                            kedalaman_akhir = kemajuan
                                        else:
                                            kedalaman_akhir

                                        table[bhid]['Kedalaman Akhir']=kedalaman_akhir
                                        print ('Data sudah berhasil diperbaharui!')
                                        show (table)
                                        update_choice(table)
                                    elif confirm == 'Tidak':
                                            print('Data tidak diperbaharui')
                                            update_choice(table)
                                    else:
                                        print('Hanya masukkan Iya/Tidak!')
                                        continue  
                        #Jika BHID tidak ada dalam database
                        else:
                            print ('''BHID tidak ada, apakah ingin menambah data?''')
                            while True:
                                #Konfirmasi apakah ingin berpindah pada menu penambahan data
                                comfirm = valid_alpha ('Iya/Tidak: ').capitalize()
                                #Jika ingin menambah data baru
                                if comfirm == 'Iya':
                                    create_choice(table)
                                #Jika tetap ingin pada menu ubah data
                                elif comfirm == 'Tidak':
                                    update_pars(table)
                                else:
                                    print ('Pilihan tidak tersedia, hanya masukkan Iya/Tidak')
                                    continue
                # Jika ingin kembali ke menu ubah data         
                elif input_case == 5:
                    update_choice(table)
                # Jika pilihan tidak tersedia
                else:
                    print ('pilihan anda tidak tersedia')
                    continue
        else:
            print ('Database kosong, ingin menambahkan data?')
            while True:
                #Konfirmasi apakah ingin berpindah ke menu menambahkan data
                comfirm = valid_alpha ('Iya/Tidak: ').capitalize()
                #Jika ingin menambah data
                if comfirm == 'Iya':
                    create_choice(table)
                #Jika tetap ingin kembali ke menu update
                elif comfirm == 'Tidak':
                    update_choice(table)
                else:
                    print ('Pilihan tidak tersedia, hanya masukkan Iya/Tidak')
                    continue 

        
    
#4. Fungsi menghapus item pada tabel
def delete_choice (table):
    """Fungsi untuk memilih data yang akan 
    dihapus dari database

    choose (int): Input pilihan hapus data
        
    """
    
    while True:
        print(''' 
---------------------------------
Apakah anda ingin menghapus data?
1. Hapus data
2. Kembali ke menu utama
---------------------------------
            '''  )
        # Meminta inputan kepada user
        choose = valid_int('Masukkan pilihan anda: ')
        # Jika ingin menghapus data
        if choose == 1:
            delete(table)
        # Jika ingin kembali ke menu utama
        elif choose == 2:
            main_menu()
        #Jika pilihan tidak tersedia
        else:
            print ('Pilihan anda tidak tersedia masukan (1/2): ')
            continue



def delete (table):
    """
    Fungsi untuk menghapus data dari database
        
    """
    while True:
        if len(table)>0:
            while True:
                show (table)
                #Meminta input bhid yang ingin dihapus
                bhid = valid_bhid('bhid')
                #Jika bhid tersedia dalam database
                if bhid in table.keys():
                    print('Anda yakin ingin menghapus data?')
                    comfirm = valid_alpha ('Iya/Tidak: ').capitalize()
                    if comfirm == 'Iya':
                        table.pop(bhid)
                        print ('Data sudah berhasil terhapus!)')
                        show(table)
                        delete_choice(table)
                    elif comfirm == 'Tidak':
                        print ('Data tidak berhasil terhapus!)')
                        delete_choice(table)
                    else:
                        print ('Pilihan tidak tersedia, hanya masukkan Iya/Tidak')
                        continue 
                #Jika bhid tidak tersedia dalam database
                else:
                    print ('BHID tidak ditemukan')
                    delete_choice(table)
        else:
            print ('Database kosong, ingin menambahkan data?')
            while True:
                #Konfirmasi apakah ingin berpindah kenu menambahkan data
                comfirm = valid_alpha ('Iya/Tidak: ').capitalize()
                #Jika ingin menambah data
                if comfirm == 'Iya':
                    create_choice(table)
                #Jika tetap ingin kembali ke menu update
                elif comfirm == 'Tidak':
                    delete_choice(table)
                else:
                    print ('Pilihan tidak tersedia, hanya masukkan Iya/Tidak')
                    continue 
      
                
        
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
'SF0001' : {'Mesin':'JACKRO01',
            'Lokasi':'Surface',
            'Kemajuan': 15, 
            'Status':'RUNNING',
            'Kedalaman Akhir':0
            }
}

def main_menu():
    import dailyreport
    dailyreport.main()