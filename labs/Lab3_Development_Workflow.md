# Lab 3: Development Workflow

## Objective
Learn to use Git and GitHub for source control, make code changes, and build a simple pipeline.

---

### 1. Install Git
**Purpose:** Set up version control tools to manage your codebase.

- Download and install Git from the [official website](https://git-scm.com/downloads).
- Verify installation:
  ```sh
  git --version
  ```

---

### 2. Clone a Repository
**Purpose:** Create a local copy of a remote repository to work on code collaboratively.

- Sign in to [GitHub](https://github.com/) and create a new repository (or use an existing one).
- Copy the repository URL.
- In your terminal, run:
  ```sh
  git clone <your-repo-url>
  cd <repo-name>
  ```

---

### 3. Make Code Changes
**Purpose:** Practice editing code and adding new features.

- Open the repo in Visual Studio Code.
- Use the provided [`greeting.py`](../provided_lab_files/Lab3/greeting.py:1) file.
- Save the file.

---

### 4. Commit and Push Changes
**Purpose:** Record your changes and share them with collaborators.

- In your terminal:
  ```sh
  git add greeting.py
  git commit -m "Add greeting script"
  git push
  ```

---

### 5. Create and Use a Branch
**Purpose:** Work on new features or fixes independently from the main codebase.

- Create a new branch:
  ```sh
  git checkout -b feature/update-greeting
  ```
- Edit `greeting.py` to print a different message.
- Commit and push the branch:
  ```sh
  git add greeting.py
  git commit -m "Update greeting"
  git push --set-upstream origin feature/update-greeting
  ```

---

### 6. Build a Simple Pipeline as Code
**Purpose:** Automate code checks and builds using CI/CD.

- In your repo, use the provided [`.github/workflows/python-app.yml`](../provided_lab_files/Lab3/python-app.yml:1) file.
- Commit and push.  
- Check the "Actions" tab on GitHub to see your workflow run.

---

### 7. Submit Evidence
**Purpose:** Demonstrate completion and understanding of each step.

- Take screenshots of:
  - Your local repo with the new file.
  - The GitHub Actions workflow run.
- Submit as instructed by your instructor.