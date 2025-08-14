# Lab 5: Deploying and Packaging

## Objective
Package an application using Docker, push to Docker Hub, and explore Infrastructure as Code (IaC) with cloud deployment options (AWS, Google Cloud, Azure).

---

### 1. Install Docker
**Purpose:** Set up a containerization platform to package and run applications consistently across environments.

- Download and install Docker from the [Docker website](https://www.docker.com/products/docker-desktop/).
- Verify installation:
  ```sh
  docker --version
  ```

---

### 2. Create a Dockerfile
**Purpose:** Define how your application is packaged and run inside a container.

- Use the provided [`Dockerfile`](../provided_lab_files/Lab5/Dockerfile:1) in your project directory.

---

### 3. Build and Run the Docker Image
**Purpose:** Build a container image from your Dockerfile and run it locally to verify it works.

- Build the image:
  ```sh
  docker build -t devops-greeting:latest .
  ```
- Run the container:
  ```sh
  docker run --rm devops-greeting:latest
  ```

---

### 4. Push Image to Docker Hub
**Purpose:** Share your container image with others and enable cloud deployments.

- Sign up for a free [Docker Hub account](https://hub.docker.com/).
- Log in from your terminal:
  ```sh
  docker login
  ```
- Tag and push your image:
  ```sh
  docker tag devops-greeting:latest <your-dockerhub-username>/devops-greeting:latest
  docker push <your-dockerhub-username>/devops-greeting:latest
  ```

---

### 5. Deploy to the Cloud (Optional)
**Purpose:** Gain experience deploying containers to a cloud provider using free-tier services.

Choose a cloud provider and follow their free-tier instructions:

- [AWS Free Tier](https://aws.amazon.com/free/) (ECS, ECR)
- [Google Cloud Free Tier](https://cloud.google.com/free) (Cloud Run, Artifact Registry)
- [Microsoft Azure Free Account](https://azure.microsoft.com/free) (Azure Container Instances, Azure Container Registry)

**Example:**  
- Deploy your Docker image using the provider’s web console or CLI.
- Refer to the provider’s documentation for step-by-step deployment.

---

### 6. Infrastructure as Code (Optional)
**Purpose:** Learn to automate cloud resource provisioning using code.

- Explore [Terraform](https://www.terraform.io/downloads.html) for IaC.
- Try deploying a simple resource (e.g., a VM or container) using a sample Terraform script.

---

### 7. Submit Evidence
**Purpose:** Demonstrate completion and understanding of each step.

- Take screenshots of:
  - Docker image running locally.
  - Docker Hub repository.
  - Cloud dashboard (if deployed).
- Submit as instructed by your instructor.