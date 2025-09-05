# Python for Linux System Administration

System administrators invariably write scripts to help automate the work they do, but rarely have time to learn a language from top to bottom. They just need enough to get the job done. In this course, Python for Linux System Administrators, you'll quickly get immersed into the Python language in the context of realistic system administration tasks.
- First, you'll survey the various development environments and learn the core language features. 
- Next, you'll meet the key library modules that allow Python scripts to interact with the rest of the Linux system. 
- Finally, you'll explore processing and modifying text files. 

When you're finished with this course, you'll have the skills to write simple sysadmin scripts in Python and have an understanding of the "pythonic" mindset for administering Linux systems.


<br>

### Table of Contents
- **Course Overview**
- **Python Quick Start**
  - Intro and Overview
  - Level-setting for This Course
  - Overview of Python
  - Characteristics and Features of Python
  - The Many Uses for Python
  - Why Use Python for System Administration?
  - Comparison of Bash and Python
- **Creating a Productive Python Environment**
  - Environment Setup
  - Python Interpreters		
  - Demo: Using the Default Python Interpreter and the iPython Interpreter
  - IDLE as Your Python IDE
  - PyCharm as Your Python IDE
  - VS Code as Your Python IDE
  - Demo: Tour of Python IDEs: VS Code		
  - Demo: Tour of Python IDEs: PyCharm
- **Interacting with the Linux System**
  - Installing Python on Linux
  - Core Python Modules for Linux Administration
  - Demo: Running the Server Health Script on a Linux Server
  - Core Python and Linux Interactions
- **Using Python with Files, Strings, and Text in Linux**
  - String Literals and Operators
  - String Formatting, Splitting, Joining, Finding, and Replacing
  - Functions and Tuples
  - Open and Close Files
  - Reading Binary Files
  - Introduction and the Difference between Strings and Bytes Objects
- **Combining Python with Other Tools**
  - Python Standard Library vs. Third Party Libraries
  - Top 10 Python Tools for Linux Administrators
  - Using Python's Logging Framework
  - Creating and Reading tar Archives with Python
  - Running Python Scripts on a Schedule Using Linux Cron

<br><br><br>

## Level-Setting for This Course
### What You Will Learn
- A **high-level overview of Python** (not a deep dive or programming-focused course).  
- How to use **Python for system administration**, with a strong focus on **Linux**.  
- Guidance on:
  - Setting up **Python IDEs** and environments.  
  - Installing and using Python on Linux.  
  - Applying Python to sysadmin tasks such as:
    - Server health checks  
    - User and service management  
    - File, string, and text handling  
    - Combining Python with other tools  

> While Linux is the main focus, many of the concepts can also apply to **Windows, cloud platforms, and Kubernetes**.


### Back Story for the Course
- You are a **Linux administrator** in a company that has decided to **standardize on Python** for:
  - Scripting  
  - Web development  
  - Automation across DevOps and SRE teams  
- Leadership wants:
  - Unified scripting skills across teams  
  - Easier onboarding for new engineers with Python skills  
  - Faster automation of Linux system administration  
- You already have strong Linux knowledge, but need to **ramp up on Python quickly**.


### Who This Course Is For
- **System administrators** or **Linux administrators**  
- **DevOps engineers**  
- **SRE engineers**  

Recommended background knowledge:
- Basic **scripting concepts**  
- Some programming familiarity (not necessarily deep developer experience)  
- **System administration** skills  
- Strong **Linux knowledge**

<br><br><br>


## Why Use Python for System Administration?
### Readability and Ease of Use
- Python has a small learning curve and is highly readable, making it easy to start scripting and automating tasks.
- Scripts are straightforward to write and maintain, even for complex tasks.

### Rich Ecosystem of Modules
- Large pool of system administration–related modules available, both built-in and community developed.
- Enables automation of a wide range of administrative and operational tasks.

### Consolidation of Tools
- Traditional Linux tools include Bash, `sed`, and `grep`.
- Python can consolidate many of these functions into a single language.
- Standardization across environments reduces complexity and tool sprawl.

### Proven Track Record
- Widely used by system administrators and DevOps engineers.
- Proven in production environments as a reliable automation language.

### Handling Complexity
- Bash and shell scripting can fall short for complex logic.
- Python scales well to handle more sophisticated workflows and tasks.

### Cross-Platform Support
- Works across multiple Linux distributions and other operating systems.
- Offers portability for scripts across diverse environments.

### Integration with Shell Commands
- Python’s `os` module allows execution of shell commands when needed.
- Provides flexibility to combine Python logic with existing CLI commands.

### Adoption in DevOps Tools
- Popular automation frameworks like **Ansible** and **Salt** are built with Python.
- Reinforces Python’s position as a foundational language in DevOps.

### Networking and Cloud Automation
- Python has built-in modules for networking tasks, enabling automation beyond servers.
- Supports automation with networking devices.
- Provides modules for major cloud platforms (AWS, Azure, GCP) and Kubernetes.


