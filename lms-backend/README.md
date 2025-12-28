
# LMS Backend 

This README is **backend setup**. Follow the steps to run the LMS backend locally.

---

## 1. Install Python

### Check Python

```bash
python --version
```

[Required](Required): **Python 3.13.x**

If the version is different, install the correct version.

### Windows

* Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* ✅ Check **“Add Python to PATH”** during installation


---

### macOS

```bash
brew install python@3.13
```

---

### Arch Linux

```bash
sudo pacman -S python
```

---

## 2. Clone the Repository

```bash
git clone <repo-url>
cd lms-backend
```

---

## 3. Create Virtual Environment

### Create venv

```bash
python -m venv venv
```

### Activate venv

**Windows (PowerShell):**

```powershell
venv\Scripts\Activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

Upgrade pip:

```bash
pip install --upgrade pip
```

---

## 4. Install Requirements

```bash
pip install -r requirements.txt
```

### If you add new packages later

```bash
pip freeze > requirements.txt
```

---

## 5. PostgreSQL Setup

---

### 5.1 Install PostgreSQL

#### Windows

* Download from: [https://www.postgresql.org/download/windows/](https://www.postgresql.org/download/windows/)
* Remember **database password**
* pgAdmin will be installed automatically

---

#### macOS

```bash
brew install postgresql
brew services start postgresql
```

---

#### Arch Linux

```bash
sudo pacman -S postgresql
sudo -iu postgres
initdb --locale=en_US.UTF-8 -D /var/lib/postgres/data
exit
sudo systemctl enable postgresql
sudo systemctl start postgresql
```

---

### 5.2 Create Database & User

Open psql:

```bash
psql -U postgres
```

Run:

```sql
CREATE DATABASE <database name>;
CREATE USER <database user> WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE <database name> TO <database user> ;
\q
```

---

## 6. Environment Variables

Create a `.env` file in backend root:

```env
DEBUG=True
SECRET_KEY=<your-secret-key>

DB_NAME=<database name>
DB_USER=<database user>
DB_PASSWORD=<password>
DB_HOST=localhost
DB_PORT=5432
```

---

## 7. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 8. Create Admin User

```bash
python manage.py createsuperuser
```

---

## 9. Run Development Server

```bash
python manage.py runserver
```
