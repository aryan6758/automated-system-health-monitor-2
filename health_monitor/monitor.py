import psutil
from .config import load_config
from .alerts import send_alert

class SystemMonitor:
    def __init__(self):
        self.config = load_config()

    def get_cpu_usage(self) -> float:
        """Returns the current CPU usage percentage."""
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self) -> float:
        """Returns the current memory usage percentage."""
        return psutil.virtual_memory().percent

    def get_disk_usage(self) -> float:
        """Returns the current disk usage percentage of the root partition."""
        return psutil.disk_usage('/').percent

    def check_health(self) -> dict:
        """
        Checks all metrics and triggers alerts if thresholds are exceeded.
        Returns a dictionary of current status.
        """
        cpu = self.get_cpu_usage()
        mem = self.get_memory_usage()
        disk = self.get_disk_usage()

        if cpu > self.config["cpu_threshold"]:
            send_alert("CPU", cpu, self.config["cpu_threshold"])

        if mem > self.config["memory_threshold"]:
            send_alert("Memory", mem, self.config["memory_threshold"])

        if disk > self.config["disk_threshold"]:
            send_alert("Disk", disk, self.config["disk_threshold"])

        return {
            "cpu": cpu,
            "memory": mem,
            "disk": disk,
            "status": "Healthy" if (cpu <= self.config["cpu_threshold"] and
                                   mem <= self.config["memory_threshold"] and
                                   disk <= self.config["disk_threshold"]) else "Unhealthy"
        }
