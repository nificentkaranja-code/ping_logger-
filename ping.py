import subprocess
import time
from datetime import datetime

target = "google.com"

num_pings = 10

print(f"Pinging{target} {num_pings} times...")
print("-"*40)
with open ("ping_log.txt","a") as log_file:
    for i in range(num_pings):
        result = subprocess.run(
            ["ping","-c","1",target],
            capture_output=True,
            text=True
        )
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if result.returncode == 0:
            output = result.stdout
            for line in output.split("\n"):
                if "time=" in line:
                    latency = line.split("time=")[1].split(" ")[0]
                    message = f"[{now}] Ping {i + 1}: Success - {latency}"
                    print(message)
                    log_file.write(message + "\n")
                    break
        else:
            message = f"[{now}] Ping {i + 1}: Failed"
            print(message)
            log_file.write(message + "\n")
        time.sleep(1)
print("-"*40)
print("Done. Results saved to ping_log.txt")
            



