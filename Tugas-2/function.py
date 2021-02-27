def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"Telepon : {kontak['telepon']}")
