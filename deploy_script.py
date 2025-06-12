import os
import shutil
import subprocess
import sys

ENV_VARS = {
    # Example environment variables. Update as needed.
    "EXAMPLE_VAR": os.getenv("EXAMPLE_VAR", "value"),
}


def run(command: str) -> None:
    """Run a shell command with error checking."""
    print(f"Running: {command}")
    subprocess.run(command, shell=True, check=True)


def main() -> None:
    """Deploy a Railway project with Redis."""
    if shutil.which("railway") is None:
        print(
            "Railway CLI not found. Install it from https://docs.railway.app/cli before running this script."
        )
        sys.exit(1)

    # Initialize project
    run("railway init")

    # Add Redis plugin
    run("railway add redis")

    # Set environment variables
    for key, value in ENV_VARS.items():
        if value is not None:
            run(f"railway variables set {key} {value}")

    # Deploy
    run("railway up")


if __name__ == "__main__":
    main()
