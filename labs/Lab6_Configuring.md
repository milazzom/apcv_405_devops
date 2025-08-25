# Lab 6: Configuring Applications

## Objective
Configure applications using environment variables and config files, connect to a database, and use Docker Compose for multi-service setups.

---

### 1. Configuration with Environment Variables
**Purpose:** Learn to use environment variables to configure your application without changing code.

- Use the provided [`greeting_env.py`](../provided_lab_files/Lab6/greeting_env.py:1) file.
- Run with a custom name:
  ```sh
  USER_NAME="YourName" python greeting_env.py
  ```

---

### 2. Configuration with YAML/JSON
**Purpose:** Store configuration in a file for easier management and portability.

- Use the provided [`config.yaml`](../provided_lab_files/Lab6/config.yaml:1) and [`greeting_yaml.py`](../provided_lab_files/Lab6/greeting_yaml.py:1) files.
- Install PyYAML if needed:
  ```sh
  pip install pyyaml
  ```
- Run:
  ```sh
  python greeting_yaml.py
  ```

---

### 3. Connect to a Database (SQLite Example)
**Purpose:** Store application data in a database for persistence.

- Use the provided [`greeting_sqlite.py`](../provided_lab_files/Lab6/greeting_sqlite.py:1) file.
- Run the script and verify `greetings.db` is created.

---

### 4. Use Docker Compose for Multi-Service Setup
**Purpose:** Orchestrate multiple services (like app and database) using a single configuration file.

- Use the provided [`docker-compose.yml`](../provided_lab_files/Lab6/docker-compose.yml:1) file.
- Build and run:
  ```sh
  docker-compose up --build
  ```
- To stop and clean up resources after testing, run:
  ```sh
  docker-compose down
  ```
  This command stops all services and removes containers, networks, and other resources created by Docker Compose.

---

### 5. Basic Telemetry/Logging
**Purpose:** Add logging to your application for monitoring and troubleshooting.

- Use the provided [`greeting_logging.py`](../provided_lab_files/Lab6/greeting_logging.py:1) file.

---

### 6. Submit Evidence
**Purpose:** Demonstrate completion and understanding of each step.

- Take screenshots of:
  - App output using environment variables and config files.
  - Database file and contents.
  - Docker Compose running.
- Submit as instructed by your instructor.