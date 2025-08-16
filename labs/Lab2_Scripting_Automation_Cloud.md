# Lab 2: Scripting, Task Automation, and Cloud Computing

## Objective
Gain hands-on experience with scripting, automating tasks, and exploring cloud computing using free services (AWS, Google Cloud, Azure).

---

### 1. Install Python (if not already installed)
**Purpose:** Ensure you have a scripting language installed for automation tasks.

- **Windows/macOS/Linux:**  
  Download and install Python from the [official website](https://www.python.org/downloads/).
- Verify installation:
  ```sh
  python --version
  ```

---

### 2. Write and Run a Simple Automation Script
**Purpose:** Learn how to create and execute a basic automation script.

- Open Visual Studio Code.
- Use the provided [`hello_automation.py`](../provided_lab_files/Lab2/hello_automation.py:1) file.
- Run the script in your terminal:
  ```sh
  python hello_automation.py
  ```

---

### 3. Automate a Task with GitHub Actions
**Purpose:** Experience automating tasks in the cloud using CI/CD pipelines.

- Sign up for a free [GitHub account](https://github.com/).
- Create a new repository.
- Add your `hello_automation.py` file.
- In your repo, use the provided [`.github/workflows/python-app.yml`](../provided_lab_files/Lab2/python-app.yml:1) file.
- Commit and push.  
- Check the "Actions" tab to see your workflow run.

---

### 4. Explore Cloud Provider Free Tiers
**Purpose:** Get familiar with cloud service dashboards and basic navigation.

Choose one or more cloud providers and sign up for a free account:

- [AWS Free Tier](https://aws.amazon.com/free/)
- [Google Cloud Free Tier](https://cloud.google.com/free)
- [Microsoft Azure Free Account](https://azure.microsoft.com/free)

NOTE: A credit card may be required to open a Microsoft Azure Free Account.  If you do not feel comfortable providing a card, I recommend exploring the Google Cloud Free Tier.

**Explore the console:**  
- Log in and browse the dashboard.
- Locate the section to launch a virtual machine (EC2 for AWS, Compute Engine for GCP, Virtual Machines for Azure).
- Do not launch a VM—just familiarize yourself with the interface.  Virtual machines can be expensive!

---

### 5. Submit Evidence
**Purpose:** Demonstrate completion and understanding of each step.

- Take screenshots of:
  - Your script running locally.
  - Your GitHub Actions workflow run.
  - The cloud provider dashboard after login.
- Put these screenshots in a Word document with the filename NETID-Lab2.docx and submit it to D2L