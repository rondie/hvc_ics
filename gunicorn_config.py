import os

host = os.getenv("HVC_ICS_HOST", "0.0.0.0")
port = os.getenv("HVC_ICS_PORT", 5000)
workers = os.getenv("HVC_ICS_WORKERS", 4)
threads = os.getenv("HVC_ICS_THREADS", 4)
timeout = os.getenv("HVC_ICS_TIMEOUT", 120)

bind = f"{host}:{port}"
workers = f"{workers}"
threads = f"{threads}"
timeout = f"{timeout}"
