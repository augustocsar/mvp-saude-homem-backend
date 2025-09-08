from dotenv import load_dotenv
import os
from pathlib import Path

# Carrega as variáveis do .env para os.environ
load_dotenv(Path(__file__).resolve().parent.parent / '.env')

BASE_DIR = Path(__file__).resolve().parent

ORACLE_ENDPOINT = os.environ.get('ORACLE_ENDPOINT')
ORACLE_COMPARTMENT_ID = os.environ.get('ORACLE_COMPARTMENT_ID')
ORACLE_TENANT_ID = os.environ.get('ORACLE_TENANT_ID')
ORACLE_USER_ID = os.environ.get('ORACLE_USER_ID')
ORACLE_FINGERPRINT = os.environ.get('ORACLE_FINGERPRINT')
ORACLE_PRIVATE_KEY_FILE = os.environ.get('ORACLE_PRIVATE_KEY_FILE')