# FTP vs SFTP vs FTPS


## **FTP (File Transfer Protocol)**
- **Port:** 21
- **Security:** Not secure (data, including credentials, sent in plaintext)
- **Use case:** Legacy file transfers
- **Encryption:** None by default
- **Authentication:** Username and password

```python
from ftplib import FTP

# Connect to FTP server (plain FTP, no encryption)
ftp = FTP('ftp.example.com')

# Login with username and password
ftp.login(user='username', passwd='password')

# Open the file in binary read mode and upload it to the server
with open('HelloWorld.txt', 'rb') as file:
    ftp.storbinary('STOR HelloWorld.txt', file)

ftp.quit()
```

### Comments:
- **`ftplib`** is built into Python's standard library — no need to install anything.
- Use **only** on **trusted internal networks** due to lack of encryption.
- **Alternative**: Use `pyftpdlib` to build FTP servers, but for clients `ftplib` is enough.


<br>



### **SFTP (SSH File Transfer Protocol)**
- **Port:** 22
- **Security:** Secure (transfers over SSH)
- **Use case:** Secure file transfer over untrusted networks
- **Encryption:** Yes (via SSH)
- **Authentication:** Username/password or SSH keys


### **FTPS (FTP Secure / FTP-SSL)**
- **Port:** 21 (explicit) or 990 (implicit)
- **Security:** Secure (adds SSL/TLS to FTP)
- **Use case:** Organizations needing FTP with SSL encryption
- **Encryption:** Yes (via SSL/TLS)
- **Authentication:** Username/password, with optional client certificate


### Summary Table:
| Feature       | FTP       | SFTP                 | FTPS                      |
| ------------- | --------- | -------------------- | ------------------------- |
| Port          | 21        | 22                   | 21 / 990                  |
| Encryption    | None      | SSH-based            | SSL/TLS                   |
| Secure?       | No        | Yes                  | Yes                       |
| Protocol Base | FTP       | SSH                  | FTP + SSL/TLS             |
| Auth Method   | User/pass | User/pass or SSH key | User/pass + optional cert |

