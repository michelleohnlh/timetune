import time
import subprocess
from datetime import datetime, timedelta

class TimeTune:
    def __init__(self):
        self.timezone = time.tzname[0]
        self.time_sync_enabled = True

    def sync_system_clock(self):
        """Synchronizes the system clock with an internet time server."""
        if self.time_sync_enabled:
            try:
                print("Synchronizing system clock...")
                subprocess.run(['w32tm', '/resync'], check=True)
                print("System clock synchronized successfully.")
            except subprocess.CalledProcessError:
                print("Error: Unable to synchronize system clock.")
        else:
            print("Time synchronization is disabled.")

    def set_timezone(self, timezone):
        """Sets the system timezone."""
        try:
            print(f"Setting timezone to {timezone}...")
            subprocess.run(['tzutil', '/s', timezone], check=True)
            self.timezone = timezone
            print(f"Timezone set to {timezone}.")
        except subprocess.CalledProcessError:
            print(f"Error: Unable to set timezone to {timezone}.")

    def get_current_time(self):
        """Returns the current system time."""
        current_time = datetime.now()
        print(f"Current system time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
        return current_time

    def add_time_offset(self, hours=0, minutes=0):
        """Simulates time management by adding an offset to the current time."""
        current_time = self.get_current_time()
        offset_time = current_time + timedelta(hours=hours, minutes=minutes)
        print(f"Time after offset: {offset_time.strftime('%Y-%m-%d %H:%M:%S')}")
        return offset_time

    def toggle_time_sync(self, enable):
        """Enables or disables the time synchronization feature."""
        self.time_sync_enabled = enable
        status = "enabled" if enable else "disabled"
        print(f"Time synchronization {status}.")

if __name__ == "__main__":
    timetune = TimeTune()
    timetune.sync_system_clock()
    timetune.set_timezone('UTC')
    timetune.get_current_time()
    timetune.add_time_offset(hours=2)
    timetune.toggle_time_sync(False)