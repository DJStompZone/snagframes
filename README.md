# SnagFrames

SnagFrames is a Python tool for extracting frames from a video file at a specific second.

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/djstompzone/snagframes.git
cd snagframes
```

Run the setup script to create a virtual environment and install dependencies:

```bash
python install.py
```

Activate the virtual environment:

- Windows:
    Powershell:
    ```ps1
    ./.venv/Scripts/activate.ps1
    ```
    CMD.exe:
    ```cmd
    .venv\Scripts\activate.bat
    ```

- Linux / Mac OS:
    ```bash
    source ./.venv/bin/activate
    ```


## Usage

To extract frames from a video, use the following command:

```
python -m snagframes.video_processor --video /path/to/target/video.mp4 --time 420 --out-dir /path/to/output/directory
```

## Development

To run tests, use the following command:

```
pytest
```

## Packaging

To build a Docker image, run the build script:

```
python build_script.py
```

Alternatively, to create a standalone executable, uncomment the PyInstaller line in the build script and run it.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.