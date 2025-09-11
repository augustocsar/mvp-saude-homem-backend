# app/database.py - CORRIGIR linha 3
from borneo import NoSQLHandle, NoSQLHandleConfig
from borneo.iam import SignatureProvider
from app import config  # ← MUDAR ESTA LINHA
import os

class Database:
    def __init__(self):
        self.handle = None
        self._connect()

    def _connect(self):
        endpoint = config.ORACLE_ENDPOINT
        compartment_id = config.ORACLE_COMPARTMENT_ID

        nosql_config = NoSQLHandleConfig(endpoint)
        nosql_config.set_default_compartment(compartment_id)

        private_key_file = config.ORACLE_PRIVATE_KEY_FILE
        full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', private_key_file)

        print(f"Procurando chave em: {full_path}")

        # Ler o conteúdo do arquivo PEM
        with open(full_path, 'r') as file:
            private_key = file.read()

        provider = SignatureProvider(
            tenant_id=config.ORACLE_TENANT_ID,
            user_id=config.ORACLE_USER_ID,
            fingerprint=config.ORACLE_FINGERPRINT,
            private_key=private_key
        )

        nosql_config.set_authorization_provider(provider)
        self.handle = NoSQLHandle(nosql_config)
        print("Conectado ao Oracle NoSQL!")

    def close(self):
        if self.handle:
            self.handle.close()

db = Database()