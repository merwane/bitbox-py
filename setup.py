import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
        name = "bitbox-py",
        version = "0.0.6",
        author = "Merwane Draï",
        author_email = "contact@merwane.me",
        description = "Gabriel Cardona's Bitbox ported to Python",
        long_description = long_description,
        long_description_content_type = "text/markdown",
        url = "https://github.com/merwane/bitbox-py",
        download_url = "https://github.com/merwane/bitbox-py",
        packages = setuptools.find_packages(),
        classifiers = [
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            'Natural Language :: English',
            'Intended Audience :: End Users/Desktop'
            ],
        license="MIT",
        keywords=(
            'bitcoincash',
            'bitbox-sdk',
            'bitcoin',
            'cryptocurrency'
            ),
        install_requires=[
            "requests",
            "cashaddress",
            "bitcash",
            "python-socketio[client]",
            "pywallet"
            ]
        )
