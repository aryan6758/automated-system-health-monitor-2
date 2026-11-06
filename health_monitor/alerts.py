import logging
from .config import load_config

config = load_config()

# Configure logging
logging.basicConfig(
    filename=config["log_file"],
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_alert(metric, value, threshold):
    """
    Handles alerting when a metric exceeds its threshold.
    For simplicity, this implementation logs to a file and prints to console.
    """
    message = f"ALERT: {metric} exceeded threshold! Current: {value}%, Threshold: {threshold}%"
    print(message)
    logging.warning(message)
