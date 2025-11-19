import platform
import subprocess
import argparse
import time
import shutil
import os

def hibernate(force=False, delay=0):
    system = platform.system()

    if delay > 0:
        print(f"Waiting {delay} seconds before hibernation...")
        time.sleep(delay)

    if system == "Windows":
        # /h ignores /t; emulate delay via sleep above.
        cmd = ["shutdown", "/h"]
        if force:
            cmd.append("/f")  # force closing apps
    elif system == "Darwin":
        # macOS: no direct hibernate; put system to sleep.
        cmd = ["pmset", "sleepnow"]
    else:
        # Linux/Unix: try hibernate variants.
        candidates = [
            ["systemctl", "hibernate"],
            ["systemctl", "suspend-then-hibernate"],
            ["pm-hibernate"],
        ]
        cmd = None
        for c in candidates:
            if shutil.which(c[0]):
                cmd = c
                break
        if cmd is None:
            raise RuntimeError("No hibernate command found (systemctl/pm-hibernate).")
        # prepend sudo if not already root
        if os.geteuid() != 0:
            cmd = ["sudo"] + cmd

    print("Executing:", " ".join(cmd))
    subprocess.run(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hibernate (or sleep on macOS) the computer via Python.")
    parser.add_argument("--force", action="store_true", help="Force close applications (Windows only).")
    parser.add_argument("--delay", type=int, default=0, help="Delay seconds before hibernation.")
    args = parser.parse_args()
    hibernate(force=args.force, delay=args.delay)
