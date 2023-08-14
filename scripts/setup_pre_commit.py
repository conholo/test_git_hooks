import subprocess

def run_command(cmd):
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Failed to run command: {cmd}")
        exit(1)

def main():
    # Install pre-commit via pip
    print("Installing pre-commit...")
    run_command("pip install pre-commit")
    # Install the pre-commit hooks
    print("Installing pre-commit hooks...")
    run_command("pre-commit install")
    print("Pre-commit setup completed successfully.")

if __name__ == "__main__":
    main()
