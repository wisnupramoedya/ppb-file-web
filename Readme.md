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
python app.py
```

## VSCode Support
Untuk menjalankan interpreter dari Python, cukup copas `where python` setelah masuk shell, lalu paste ke lokasi interpreter.

## Error Tensorflow
Jika ada error Tensorflow karena CUDA, bisa dilupakan saja.