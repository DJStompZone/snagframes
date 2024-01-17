from setuptools import find_packages, setup

setup(
    name="snagframes",
    version="0.1.1",
    packages=find_packages(),
    py_modules=["snagframes"],
    install_requires=["Pillow~=10.0.0", "python-ffmpeg~=2.0.10", "pytest~=7.0.1"],
    platforms=["any"],
    entry_points={
        "console_scripts": [
            "snagframes=snagframes.video_processor:main",
        ],
    },
)
