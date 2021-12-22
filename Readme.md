# Installasi

Pastikan Python anda versi 3.7 atau lebih.
Lalu, jalankan langkah berikut.
1. Install pipenv
```
pip install pipenv
```
atau
```
conda install pipenv
```
2. Masuk ke pipenv shell (wajib)
```
pipenv shell
```
3. Install semua package (jika sebelumnya belum menginstall)
```
pipenv install --dev
```
4. Untuk menjalankan aplikasi, jalankan
```
flask run
```

## VSCode Support
Untuk menjalankan interpreter dari Python, cukup copas `where python` setelah masuk shell, lalu paste ke lokasi interpreter.

## Error Tensorflow
Jika ada error Tensorflow karena CUDA, bisa dilupakan saja.

## Migration

Apabila `app.db` tidak ada, maka bisa ikuti cara ini.

Jalankan jika tidak ada folder `migrations`
```
flask db init
```

Lalu, jalankan ini untuk memasukkan migration di sini akan menghasilkan `version` di folder `migrations`
```
flask db migrate
```

Jalankan ini untuk memasukkan migration ke db, maka akan tercipta `app.db`
```
flask db upgrade
```

Jika ada error `DLL load failed`, masukkan file sqlite3.dll dan sqlite3.def dari [https://www.sqlite.org/download.html](https://www.sqlite.org/download.html) ke lokasi `pip -V` di Anaconda Prompt. Folder hasilnya misal `C:\ProgramData\Anaconda3\lib\site-packages\pip` masukkan ke `C:\ProgramData\Anaconda3\DLLs`.