# Lab 4: Releasing, File Versioning, and Testing

## Objective
Learn to manage releases, use version control, and automate testing with free tools.

---

### 1. Tag a Release in Git
**Purpose:** Mark a specific point in your code history as a release for easier tracking and deployment.

- In your local repo, create a tag:
  ```sh
  git tag v1.0.0
  git push origin v1.0.0
  ```

---

### 2. Create a GitHub Release
**Purpose:** Publish a formal release on GitHub to share with others and enable downloads.

- Go to your repository on [GitHub](https://github.com/).
- Click "Releases" > "Draft a new release".
- Select the tag (e.g., `v1.0.0`), add a title and description, and publish the release.

---

### 3. Write and Run Basic Tests
**Purpose:** Ensure your code works as expected by writing and running automated tests.

- Use the provided [`test_greeting.py`](../provided_lab_files/Lab4/test_greeting.py:1) file.
- Install [pytest](https://docs.pytest.org/en/stable/):
  ```sh
  pip install pytest
  ```
- Run the test:
  ```sh
  pytest
  ```

---

### 4. Automate Tests in CI
**Purpose:** Automatically run your tests on every code change using CI/CD pipelines.

- In your repo, use the provided [`.github/workflows/python-app.yml`](../provided_lab_files/Lab4/python-app.yml:1) file.
- Commit and push.  
- Check the "Actions" tab for test results.

---

### 5. Explore Versioning
**Purpose:** Practice updating your code and managing multiple versions/releases.

- Make a small change to `greeting.py`.
- Commit and tag as `v1.0.1`:
  ```sh
  git add greeting.py
  git commit -m "Minor update"
  git tag v1.0.1
  git push origin v1.0.1
  ```

---

### 6. Submit Evidence
**Purpose:** Demonstrate completion and understanding of each step.

- Take screenshots of:
  - The GitHub Release page.
  - Test results locally and in GitHub Actions.
- Submit as instructed by your instructor.