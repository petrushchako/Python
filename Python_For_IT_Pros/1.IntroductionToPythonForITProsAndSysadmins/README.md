# Introduction to Python for IT Pros and Sysadmins

### Description
Discover the transformative potential of Python in streamlining IT operations and system administration, In this course, Introduction to Python for IT Pros and Sysadmins, you'll learn to leverage the power of Python to streamline your IT operations and system administration tasks. First, you'll explore the basics of Python programming, even if you have no prior coding experience. Next, you'll discover how Python can be used to automate common IT tasks, such as interacting with the operating system, network programming, and working with APIs. Finally, you'll learn how to extract and analyze data from websites, manage databases, and build automation scripts tailored to your specific needs. When you're finished with this course, you'll have the skills and knowledge of Python required to automate tasks, enhance productivity, and improve efficiency in your IT operations and system administration.

### Table of contents
- **Introduction to Python Basics**
  - Why Python for IT Pros and Sysadmins?
  - `Demo`: Setting up the Python Environment
  - `Demo`: Control Flow Statements
  - `Demo`: Functions and Modules
  - `Demo`: Handling Exceptions
  - `Demo`: File Handling
  - Summary		
- **Python Scripts for IT Ops and Sysadmin**		
  - Introduction and Overview
  - Intro to IT Ops and Sysadmin with Python
  - `Demo`: Interacting with the Operating System
  - `Demo`: Network Programming
  - `Demo`: Working with APIs
  - `Demo`: Web Scraping and Data Extraction
  - `Demo`: Working with Databases
  - `Demo`: Building Automation Scripts (Log Parser)
  - `Demo`: Building Automation Scripts (Backup and Restore)
  - `Demo`: Building Automation Scripts (AWS Resource Provisioning)
  - Summary and Final Thoughts


<br><br><br>

## **Introduction to Python Basics**		
### Why Python for IT Pros and Sysadmins
- **Simplicity & Readability**: 
  - Clean and intuitive design
  - Accessible for everyone
  - Quickly grasp the language
  - Focus on solving problems
- **Versatility & Flexibility**:
  - Automation scripts
  - Analyzing data
  - Configuring networks
  - Manage cloud resources
- **Extensive Ecosystem**:
  - Extensive library ecosystem
  - Network managment
  - Database interactions
  - Web scraping
  - Cybersecurity
  - Simplify and accelerate your tasks
  - Focus on solving challanges
- **Automation & Scripting**:
  - Automate is key for IT & Sysadmin
  - Automate repetitive tasks
  - Streamline workflows
  - Eliminate manual errors
  - Orchestrate complex processes
  - Manage configurations
  - Deploy resources
- **Cross-Platform Compatibility**:
  - Scripts and tools work across different systems
  - Saving rewriting code
  - For different environments
- **Rapid Development**:
  - Simple and efficient coding practices
  - Enable rapid development
  - Prototype, test and deploy faster
  - Stay ahead of evolving changes
  - Meet deadlines
- **Community Support**:
  - Vibrant and active community
  - Never alone with callenges
  - Seeking advice
  - Troubleshooting
  - Learning new technologies
  - Wealth of shared know-how
- **Integration Capability**:
  - Great choice for systems integration
  - Crucial for IT pros and sysadmins
  - Components and infrastructure
- **Scalability**: 
  - Ability to handle projects or varying sizes
  - Scalable for small-scale IT setups
  - Large enterprise environments
  - Python Scales to meet your needs


<br>

## Setting Up Python Environment
### Install Python
1. Go to https://www.python.org
2. Download installer specific for your system
3. Run installation
4. Verify installation with `python3 --version`
### Configure virtual environment
1. Conritm pip installation with `pip3 --version`
2. Once Python and pip are available install virtual environment with `pip install virtualenv` (check list of modules by running `pip list` or `pip show virtualenv`)
3. Create virtaul environmnet with `python3 -m venv venv`
4. Activate **venv** with `source venv/bin/activate`
5. Check status of virtual environment with `which python` (It should point to the Python binary inside **./venv/**)
6. Kill virtual environment by running `deactivate` command

To install specific verion of library use `pip install requests==2.31.0` (e.g. `pip show requests`)


<br>


## Intro to IT Ops and Sysadmin with Python
- **Role**: More than a language — enables automation, workflow streamlining, and efficiency improvements.
- **Automation**: Handles repetitive tasks like provisioning, deployments, backups, monitoring.
- **Efficiency**: Scripts simplify complex operations, reducing human intervention and saving time/resources.
- **Problem-Solving**: Useful for troubleshooting, database optimization, security management.
- **Custom Tools**: Build tailored utilities (e.g., network analysis, monitoring dashboards).

<br>  

- **Key Use Cases**:
  - Configuration management (servers, apps, networks)
  - Monitoring & alerts (system health, traffic, utilization)
  - Backup & recovery (data, configs, resilience)
  - Log analysis (errors, behavior, security)
  - Resource provisioning & scaling (optimize cost/usage)
  - Reporting & documentation (status, metrics, changes)



<br><br><br>

## `Demo`: Building Automation Scripts (Log Parser)
### How it works
> Example Log File (`access.log`)

### Step 1: Read Log File
```python
with open(log_file_path) as file:
    log_lines = file.readlines()
````

Result (`log_lines` becomes a list of 3 strings):

```python
[
 "192.168.1.100 - - [13/Aug/2023:10:00:00 +0000] \"GET /page1 HTTP/1.1\" 200 1234\n",
 "192.168.1.101 - - [13/Aug/2023:10:01:00 +0000] \"GET /page2 HTTP/1.1\" 404 5678\n",
 "192.168.1.102 - - [13/Aug/2023:10:02:00 +0000] \"GET /page1 HTTP/1.1\" 200 9876\n"
]
```

<br>

### Step 2: Extract IP Addresses
```python
ip_addresses = re.findall(ip_pattern, "".join(log_lines))
unique_ips = set(ip_addresses)
```

* Regex pattern: `\d+\.\d+\.\d+\.\d+`
* Matches IPs:
  `192.168.1.100`, `192.168.1.101`, `192.168.1.102`

Result:
```python
ip_addresses = ["192.168.1.100", "192.168.1.101", "192.168.1.102"]
unique_ips = {"192.168.1.100", "192.168.1.101", "192.168.1.102"}
```

So, **3 unique IP addresses**.

<br>

### Step 3: Count Number of Requests
```python
num_requests = len(log_lines)
```

Since there are 3 lines:
```python
num_requests = 3
```

<br>

### Step 4: Extract URLs
```python
for line in log_lines:
    match = re.search(r'"GET (.*?) HTTP', line)
    if match:
        url = match.group(1)
        url_counter[url] += 1
```

* Line 1 → URL = `/page1`
* Line 2 → URL = `/page2`
* Line 3 → URL = `/page1`

Result (`url_counter`):
```python
Counter({
    "/page1": 2,
    "/page2": 1
})
```

<br>

### Step 5: Get Most Popular URLs
```python
url_counter.most_common(3)
```

Result:
```python
[("/page1", 2), ("/page2", 1)]
```

<br>

### Step 6: Final Output
The script prints:

```sh
Log Analysis Results:
Number of Requests:        3
Number of Unique IP Addresses: 3

Popular URLs:
/page1: 2 requests
/page2: 1 requests
```


