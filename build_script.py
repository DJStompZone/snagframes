import subprocess
import sys

def build():
    # Build the Docker image
    subprocess.run(['docker', 'build', '-t', 'snagframes', '.'], check=True)

    # Alternatively, build the standalone executable with PyInstaller
    # subprocess.run(['pyinstaller', '--onefile', 'snagframes/cli.py'], check=True)

if __name__ == '__main__':
    build()