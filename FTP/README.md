# FTP vs SFTP vs FTPS


### **FTP (File Transfer Protocol)**
- **Port:** 21
- **Security:** Not secure (data, including credentials, sent in plaintext)
- **Use case:** Legacy file transfers
- **Encryption:** None by default
- **Authentication:** Username and password


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
