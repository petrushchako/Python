# Python Code Formatters

In Python, several tools can help automatically fix **indentation, spacing, and style**, similar to **Prettier** in JavaScript.

### 1. `Black`

- The most popular Python code formatter.  
- Opinionated (like Prettier) — very little configuration.  
- Example:

  ```bash
  pip install black
  python3 --version

  black your_file.py

    
  # Check installation status
  which black 
  #If it still says "command not found", the executable is likely installed in a directory that’s not in your shell’s $PATH.
  ll /Library/Frameworks/Python.framework/Versions/3.13/bin
  ````

- Optional:

  ```bash
  python3 --version
  which python3
  pip3 --version
  which pip3

  export PATH="/Library/Frameworks/Python.framework/Versions/3.13/bin:$PATH"
  ```

### 2. `autopep8`

- Focuses on making code **PEP 8–compliant**.
- More configurable than Black.
- Example:

  ```bash
  pip install autopep8
  autopep8 --in-place --aggressive --aggressive your_file.py
  ```

### 3. YAPF (Yet Another Python Formatter)

- Developed by Google.
- Similar to Black but allows more style customization.
- Example:

  ```bash
  pip install yapf
  yapf -i your_file.py
  ```


## Recommendation

* For a **“just do it” Prettier-like experience**, use **Black**.
* For **strict PEP 8 compliance**, use **autopep8**.
