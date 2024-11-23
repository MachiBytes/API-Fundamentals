# Instructions
This file contains the basic instructions on how to setup for success for the API Fundamentals Workshop.

### Required Software
1. Install any code editor of your choice for working with Python.
    - [Visual Studio Code](https://code.visualstudio.com) (Preferred)
    - [Sublime Text Editor](https://www.sublimetext.com)
    - [PyCharm](https://www.jetbrains.com/pycharm/)
2. Install [Python 3.12](https://www.python.org/downloads/release/python-3126/).
    - For Windows: Click [here](https://www.canva.com/design/DAGXNNZak2s/4VCE8Ecoh17LafDZ_bw1eg/edit?utm_content=DAGXNNZak2s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) for a detailed Python installation or install using Microsoft Store. Verify installation by typing `python -V` in Windows PowerShell.
4. Install a software for testing API Endpoints
    - [Bruno](https://www.usebruno.com) (Preferred)
    - [Postman](https://www.postman.com)
    - [Insomnia](https://insomnia.rest)

### Setup working environment
- This section assumes that you are using the preffered softwares (Visual Studio Code and Bruno)
1. Open VS Code and install the "SQLite Explorer" extension.
2. Create a virtual environment with Python by entering `python -m venv venv` using the corresponding terminal of your OS (Windows - Powershell, MacOS/Linux - Terminal).
3. Activate the virtual environment using `./venv/Scripts/activate` (Windows) or `source venv/bin/activate` (MacOS/Linux).
    - For Windows: If you are receiving an error containing "cannot be loaded because running scripts is disabled on this system," enter `Set-ExecutionPolicy Unrestricted -Scope Process` first.
5. Install FastAPI module in Python using `pip install "fastapi[standard]"`
    - Make sure to surround `fastapi[standard]` with double quotation marks to ensure that it works on your terminal.
6. Install Peewee module in Python using `pip install peewee`
