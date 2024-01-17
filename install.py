import subprocess
import sys
import venv

def setup_environment():
    # Create a virtual environment
    venv.create('.venv', with_pip=True)

    # Activate the virtual environment
    if sys.platform == 'win32':
        activate_script = '.venv\\Scripts\\activate.bat'
    else:
        activate_script = '.venv/bin/activate'

    # Install dependencies
    subprocess.run([activate_script, '&&', 'pip', 'install', '-r', 'requirements.txt'], shell=True)

if __name__ == '__main__':
    setup_environment()