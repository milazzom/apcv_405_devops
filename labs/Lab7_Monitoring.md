# Lab 7: Monitoring

## Objective
Set up monitoring for a containerized application, collect and visualize metrics, and review logs using free tools.

---

### 1. Install Prometheus and Grafana
**Purpose:** Set up monitoring and visualization tools to collect and display application metrics.

- **Docker (recommended for all OS):**
  - [Prometheus Docker Hub](https://hub.docker.com/r/prom/prometheus)
  - [Grafana Docker Hub](https://hub.docker.com/r/grafana/grafana)
- All required images will be pulled or built automatically when you run Docker Compose.

---

### 2. Create a Sample App with Metrics
**Purpose:** Generate metrics from a running application for monitoring.

- Use the provided [`metrics_app.py`](../provided_lab_files/Lab7/metrics_app.py:1) file.
- The app will be built into a container using the provided Dockerfile.
- No need to install dependencies manually; they are installed during the image build.
- The app will run automatically as a container when you start Docker Compose.
- Access the metrics endpoint at [http://localhost:8000](http://localhost:8000).

---

### 3. Run Prometheus and Grafana with Docker Compose
**Purpose:** Orchestrate monitoring tools and configure Prometheus to scrape your app's metrics.

- Use the provided [`docker-compose.yml`](../provided_lab_files/Lab7/docker-compose.yml:1) and [`prometheus.yml`](../provided_lab_files/Lab7/prometheus.yml:1) files.
- Start all services (metrics app, Prometheus, Grafana) together:
  ```sh
  docker-compose up
  ```

---

### 4. Visualize Metrics
**Purpose:** Explore and visualize collected metrics in Prometheus and Grafana dashboards.

- Access Prometheus at [http://localhost:9090](http://localhost:9090).
- Access Grafana at [http://localhost:3000](http://localhost:3000) (default login: admin/admin).
- Add Prometheus as a data source in Grafana and create a dashboard to visualize `hello_requests_total`.

---

### 5. Review Logs
**Purpose:** Check logs for troubleshooting and to verify monitoring is working.

- View logs for your app and containers:
  ```sh
  docker-compose logs
  ```
---
### 6. Stop and Clean Up Docker Compose Deployment
**Purpose:** Properly shut down all services and remove resources.

- To stop all running containers and clean up resources:
  ```sh
  docker-compose down
  ```
- This command stops all services and removes containers, networks, and default volumes created by Docker Compose.

---

---

### 7. Submit Evidence
**Purpose:** Demonstrate completion and understanding of each step.

- Take screenshots of:
  - Prometheus and Grafana dashboards (after accessing the metrics app of course!)
  - App and container logs.
- Submit your screenshots within a Word document named NetId-Lab7.docx and upload it to D2L against the Lab 7 assignment.