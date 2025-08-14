


### 2️⃣ **Investigador de Servidores Profissional**
Ferramenta para análise completa de servidores/dominios:
- **Descobre o IP** de qualquer domínio.
- **Verifica status HTTP** (200, 301, 404, 500, etc.).
- **Exibe cabeçalhos HTTP** completos.
- **Identifica tecnologias do servidor** (Apache, Nginx, PHP, ASP.NET, etc.).
- **Executa WHOIS** para informações do proprietário.
- **Faz varredura de portas** principais com **Nmap**.
- **Salva relatório** completo em `.txt`.

---

## 🛠️ Requisitos

Antes de executar as ferramentas, instale os pacotes necessários no **Termux**:

```bash
pkg update && pkg upgrade -y
pkg install python git nmap -y
pip install -r requirements.txt


---

📂 Estrutura do Repositório

├── investigator/
│   ├── investigator.py
│   ├── requirements.txt
|     |-------README.md


---

🚀 Como Usar


🌐 Investigador de Servidores

cd investigator
python investigator.py

Informe o domínio ou IP do servidor.

O script realiza as verificações e salva um relatório com os resultados.



---

📊 Exemplo de Saída (Investigador de Servidores)

[+] Dominio: example.com
[+] IP: 93.184.216.34
[+] Status HTTP: 200 OK
[+] Tecnologias: Apache 2.4.54, PHP 8.1
[+] Portas Abertas:
    80/tcp - HTTP
    443/tcp - HTTPS
[+] WHOIS: Registrado por Example Registrar, expira em 2030


---

📄 Licença

Este projeto está licenciado sob a MIT License.
Você pode usar, modificar e distribuir livremente, desde que mantenha os créditos.


---

📢 Aviso Legal

⚠️ Este projeto é destinado a fins educacionais e de testes autorizados.
O uso indevido para invadir, espionar ou comprometer redes sem permissão é ilegal e pode resultar em sanções criminais.
O autor não se responsabiliza por uso indevido.


---

🤝 Contribuindo

Se quiser melhorar este projeto:

1. Faça um fork do repositório.


2. Crie uma branch para suas modificações.


3. Envie um pull request.




---

📬 Contato
Nome do criador do projeto: igor
📧 Email: legendmaster955t@gmail.com
🐙 GitHub: HLSV

---
