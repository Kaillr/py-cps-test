[![Latest Release](https://img.shields.io/github/v/release/Kaillr/py-cps-test)](https://github.com/Kaillr/py-cps-test/releases/latest)
[![CodeFactor](https://www.codefactor.io/repository/github/kaillr/py-cps-test/badge)](https://www.codefactor.io/repository/github/kaillr/py-cps-test)

# py-cps-test

A simple Python tool to calculate real-time typing speed in terms of characters per second (CPS), words per minute (WPM), and beats per minute (BPM) based on user key inputs.


## Features
- Calculates **CPS** (Characters Per Second)
- Calculates **WPM** (Words Per Minute)
- Calculates **BPM** (Beats Per Minute)
- Allows for testing with customizable time windows

## How to Use

### Option 1: Running the Executable (`.exe`)
If you prefer not to install Python or dependencies, you can simply run the provided `.exe` file:

1. Download the `.exe` file from the [latest release](https://github.com/Kaillr/py-cps-test/releases/latest).
2. Double-click to run it — no Python installation required

### Option 2: Running the Python Script (`.py`)

If you’d like to run the Python script directly, follow these steps:

1. Make sure you have [Python](https://www.python.org/downloads/) installed on your system.
2. Download or clone this repository to your local machine.
3. Install the required dependencies by running the following command:

    ```bash
    pip install pynput
    ```

4. Run the script:

    ```bash
    python cps-test.py
    ```

5. Follow the on-screen prompts to start the test and begin typing.


## Prerequisites for running python in `.venv`

Make sure you have the following installed:

- **`pyenv`**: A tool for managing multiple Python versions.

### Installing `pyenv`
Follow the instructions on the [pyenv installation page](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) to install `pyenv`.  
To integrate `pyenv` with your shell, follow the instructions [here](https://github.com/nvm-sh/nvm#deeper-shell-integration).

## Installing Local Python Version

1. Install the Python version specified in the `.python-version` file:
   ```bash
   pyenv install
   ```
2. Set the local Python version:
   ```bash
   pyenv local
   ```

## Initialize Virtual Environment (`venv`)

1. In the project's root directory, create a virtual environment:
   ```bash
   python -m venv .venv
   ```

## Activating the Virtual Environment

Activate the virtual environment by running the appropriate command based on your operating system and shell:
    
<table>
  <thead>
    <tr>
      <th>Platform</th>
      <th>Shell</th>
      <th>Command to activate virtual environment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">POSIX</td>
      <td>bash/zsh</td>
      <td><code>$ source .venv/bin/activate</code></td>
    </tr>
    <tr>
      <td>fish</td>
      <td><code>$ source .venv/bin/activate.fish</code></td>
    </tr>
    <tr>
      <td>csh/tcsh</td>
      <td><code>$ source .venv/bin/activate.csh</code></td>
    </tr>
    <tr>
      <td>pwsh</td>
      <td><code>$ .venv/bin/Activate.ps1</code></td>
    </tr>
    <tr>
      <td rowspan="2">Windows</td>
      <td>cmd.exe</td>
      <td><code>C:\&gt; .venv\Scripts\activate.bat</code></td>
    </tr>
    <tr>
      <td>PowerShell</td>
      <td><code>PS C:\&gt; .venv\Scripts\Activate.ps1</code></td>
    </tr>
  </tbody>
</table>

To deactivate the virtual environment, simply run:
```bash
deactivate
```

## Install Local Python Packages

1. Make sure the virtual environment is activated.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the CPS Test

1. Ensure the virtual environment is activated.
2. Run the script:
   ```bash
   python cps-test.py
   ```

## Additional Resources
- For more details on **`pyenv`**, visit the [pyenv documentation](https://github.com/pyenv/pyenv#readme).
- For more details on **`venv`**, visit the [venv documentation](https://docs.python.org/3/library/venv.html).


## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Kaillr/py-cps-test?tab=MIT-1-ov-file) file for details.
