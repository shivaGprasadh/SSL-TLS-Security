
# SSL Scanner Dashboard

A Flask-based web application for scanning and monitoring SSL/TLS configurations of domains.

## Features

- SSL/TLS protocol support detection
- Certificate analysis
- Security vulnerability assessment
- Cipher suite evaluation
- Security scoring and grading
- Web-based dashboard
- Database storage of scan results

## Database Setup

This application supports both SQLite (default) and PostgreSQL databases.

### SQLite Setup (Default)

SQLite is the default database and requires no additional setup. The application will automatically create the database file.

#### Quick Start with SQLite

1. **Initialize the database:**
   ```bash
   python init_db.py
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

The SQLite database file will be created at `instance/sslscan.db`.

#### SQLite Configuration

The application uses SQLite by default with this configuration in `app.py`:
```python
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///sslscan.db")
```

### PostgreSQL Setup (Production)

For production deployments, PostgreSQL is recommended for better performance and concurrent access.

#### 1. Install PostgreSQL

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

**CentOS/RHEL:**
```bash
sudo yum install postgresql-server postgresql-contrib
sudo postgresql-setup initdb
sudo systemctl enable postgresql
sudo systemctl start postgresql
```

**macOS:**
```bash
brew install postgresql
brew services start postgresql
```

#### 2. Create Database and User

Connect to PostgreSQL:
```bash
sudo -u postgres psql
```

Create database and user:
```sql
CREATE DATABASE sslscandb;
CREATE USER sslscanuser WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE sslscandb TO sslscanuser;
\q
```

#### 3. Configure Database URL

Set the `DATABASE_URL` environment variable:

**For development:**
```bash
export DATABASE_URL="postgresql://sslscanuser:your_secure_password@localhost:5432/sslscandb"
```

**For Replit deployment:**
Add to Secrets:
- Key: `DATABASE_URL`
- Value: `postgresql://sslscanuser:your_secure_password@your_postgres_host:5432/sslscandb`

#### 4. Initialize PostgreSQL Database

```bash
python init_db.py
```

#### 5. Run the Application

```bash
python main.py
```

## Installation

### Prerequisites

- Python 3.11+
- sslscan tool
- pip package manager

### System Dependencies

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install sslscan python3 python3-pip
```

**CentOS/RHEL/Fedora:**
```bash
sudo yum update
sudo yum install epel-release
sudo yum install sslscan python3 python3-pip
```

**macOS:**
```bash
brew install sslscan python3
```

### Python Dependencies

Install required Python packages:
```bash
pip install -r requirements.txt
```

### Database Initialization

Initialize the database tables:
```bash
python init_db.py
```

## Running the Application

### Development Mode

```bash
python main.py
```

The application will be available at:
- http://127.0.0.1:5000 (local)
- http://0.0.0.0:5000 (network accessible)

### Production Mode

For production deployment, use a WSGI server like Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `sqlite:///sslscan.db` |
| `SESSION_SECRET` | Flask session secret key | `dev-secret-key-change-in-production` |

## Database Schema

The application uses three main tables:

- **domain**: Stores domain information
- **scan_result**: Stores SSL scan results and security assessments
- **scan_job**: Tracks batch scanning operations

## Troubleshooting

### Database Connection Issues

**SQLite:**
- Check file permissions in the `instance/` directory
- Ensure the application has write access
- Database file is created automatically

**PostgreSQL:**
- Verify `DATABASE_URL` environment variable
- Check PostgreSQL service is running: `sudo systemctl status postgresql`
- Verify user credentials and database existence
- Check network connectivity to database host

### Common Issues

1. **Missing sslscan tool:**
   ```bash
   # Install sslscan using your system package manager
   sudo apt install sslscan  # Ubuntu/Debian
   brew install sslscan      # macOS
   ```

2. **Python dependency issues:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database initialization fails:**
   ```bash
   # Reinitialize the database
   python init_db.py
   ```

4. **Port already in use:**
   ```bash
   # Find process using port 5000
   lsof -i :5000
   # Kill the process if needed
   kill -9 <PID>
   ```

## Development

### Project Structure

```
├── app.py              # Flask application factory
├── main.py             # Application entry point
├── models.py           # Database models
├── routes.py           # URL routes and views
├── ssl_scanner.py      # SSL scanning logic
├── init_db.py          # Database initialization
├── templates/          # HTML templates
├── static/             # CSS, JS, and static assets
└── instance/           # SQLite database location
```

### Adding New Features

1. Define database models in `models.py`
2. Add routes in `routes.py`
3. Create templates in `templates/`
4. Update database schema with `python init_db.py`

## License

This project is open source. Please refer to the license file for details.
