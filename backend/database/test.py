from database.security import encrypt_password, decrypt_password

password = 'july271914'
salt = '5YA7z'
print(decrypt_password(
    'gAAAAABiJ6udplt-nwvKENVLzaRkrB-SmP-4KaBMBr8t1JoSqeYyqMetxRaAXL_wvFr97bPvfq2s1xidauM_05l93HOspEwDXQ==',
    'XMdQr'
))

