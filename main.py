from controller.telemetry_controller import start_application
import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def main():
    start_application()


if __name__ == "__main__":
    main()
