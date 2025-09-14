# DevOps Class Project: Automated CI/CD Pipeline with Jenkins, Docker, and GitHub

## Project Overview

In this project, you will create a complete CI/CD pipeline that automates the building, testing, and deployment of a web application. You'll use Jenkins to orchestrate the pipeline, Docker to containerize your application, GitHub for version control, and DockerHub as your container registry.

## Prerequisites

Before starting this project, ensure you have the following:

### Required Accounts
- [ ] **GitHub Account**: [https://github.com/join](https://github.com/join)
- [ ] **DockerHub Account**: [https://hub.docker.com/signup](https://hub.docker.com/signup)

### Required Software
- [ ] **Git**: [https://git-scm.com/downloads](https://git-scm.com/downloads)
- [ ] **Docker Desktop**: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
- [ ] **Jenkins**: [https://www.jenkins.io/download/](https://www.jenkins.io/download/ - unless running as a container)
- [ ] **Java 11 or higher**: [https://adoptium.net/](https://adoptium.net/) (required for Jenkins unless running as a container)


### Required Knowledge
- Basic understanding of Git and GitHub
- Familiarity with command line/terminal
- Basic understanding of Docker concepts
- Understanding of CI/CD principles

## Project Deliverables

1. Fork the provided application repository ([https://github.com/milazzom/apcv_405_app.git](https://github.com/milazzom/apcv_405_app.git)) to your own GitHub account, then clone and build your forked repository locally
2. A Dockerfile for containerizing the application (if not already present)
3. A Jenkins pipeline configuration (Jenkinsfile)
4. Automated tests that run in the pipeline
5. A DockerHub repository with your published image
6. Documentation showing the complete pipeline execution

## Stage 1: Setting Up Your Application Repository

### Objective
Clone and use the provided application repository for your CI/CD pipeline project.

### Instructions

1. **Fork and clone the repository**
      - Go to [https://github.com/milazzom/apcv_405_app](https://github.com/milazzom/apcv_405_app) and click the **Fork** button to create a copy under your own GitHub account.
      - After forking, clone your forked repository locally (replace `YOUR_GITHUB_USERNAME`):
         ```bash
         git clone https://github.com/YOUR_GITHUB_USERNAME/apcv_405_app.git
         cd apcv_405_app
         ```

2. **Review the application code and structure**
   - The application listens on port 8080 and exposes a health endpoint at `/health`.
   - For this project, you will run the application container on port 9090 (host) mapped to 8080 (container).
   - Review the repository for a Dockerfile and automated tests. If missing, add them as needed in later stages.

### Resources
- [Original apcv_405_app GitHub Repository](https://github.com/milazzom/apcv_405_app)
- Your forked repository on GitHub

## Stage 2: Creating Automated Tests

### Objective
### Instructions
1. **Review and run existing tests**
    - Check the repository for test files.
    - Run the existing tests locally using the following command:
        ```bash
        dotnet test apcv_405_app.sln
        ```
    - Ensure all tests pass before proceeding.  If for some reason, a test fails, reach out to the instructor.  These tests should be executed as part of your DevOps pipeline.
### Resources
### Objective
Automated tests will be executed as part of the Jenkins pipeline using the .NET CLI.

### Instructions

All test execution will be handled by Jenkins. No manual test creation or execution is required.

## Stage 3: Containerizing Your Application

### Objective
Ensure the application can be containerized and run on port 9090.

### Instructions

1. **Check for a Dockerfile**
    - If a Dockerfile is present, review it to ensure it exposes port 9090 and runs the app correctly.

2. **Test your Docker build locally**
   ```bash
   docker build -t your-dockerhub-username/apcv_405_app:latest .
   docker run -p 9090:8080 your-dockerhub-username/apcv_405_app:latest
   # The app will be accessible at http://localhost:9090
   ```
3. **Commit any new or updated Docker files**
    ```bash
    git add .
    git commit -m "Add or update Dockerfile and .dockerignore"
    git push origin main
    ```

### Resources
- Your forked apcv_405_app GitHub Repository

## Stage 4: Setting Up Jenkins

### Objective
Install and configure Jenkins to automate your CI/CD pipeline.

### Instructions

1. **Install Jenkins**
   
   **Option A: Using Docker (Recommended)**
   ```bash
   docker run -d -p 8080:8080 -p 50000:50000 --name jenkins \
     -v jenkins_home:/var/jenkins_home \
     -v /var/run/docker.sock:/var/run/docker.sock \
     jenkins/jenkins:lts
   ```

   **Option B: Direct Installation**
   - Follow the installation guide for your OS: [https://www.jenkins.io/doc/book/installing/](https://www.jenkins.io/doc/book/installing/)

2. **Initial Jenkins Setup**
   - Navigate to `http://localhost:8080`
   - Retrieve the initial admin password:
     ```bash
     docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
     ```
   - Install suggested plugins
   - Create an admin user

3. **Install Required Plugins**
   - Go to "Manage Jenkins" → "Manage Plugins"
   - Install the following plugins:
     - Docker Pipeline
     - GitHub Integration Plugin
     - Pipeline: Stage View Plugin
     - Blue Ocean (optional but recommended)

4. **Configure Docker in Jenkins**
   - Go to "Manage Jenkins" → "Global Tool Configuration"
   - Add Docker installation or configure to use Docker from PATH

### Resources
- [Jenkins Documentation](https://www.jenkins.io/doc/)
- [Jenkins Docker Installation](https://www.jenkins.io/doc/book/installing/docker/)

## Stage 5: Creating the Jenkins Pipeline

### Objective
Create a Jenkinsfile that defines your CI/CD pipeline stages for the provided application.

### Instructions

1. **Create a Jenkinsfile in the root of the cloned repository**
      - The pipeline should:
         - Clone your forked repository
         - Build the application
         - Run automated tests using the following command:
            ```bash
            dotnet test ClassProjectApp.Tests/ClassProjectApp.Tests.csproj -c Release
            ```
         - Build and push a Docker image to DockerHub
         - Run the container on port 9090 (host) mapped to 8080 (container)
         - Perform a health check on `http://localhost:9090/health`

2. **Commit the Jenkinsfile**
    ```bash
    git add Jenkinsfile
    git commit -m "Add Jenkins pipeline configuration"
    git push origin main
    ```

### Resources
- Your forked apcv_405_app GitHub Repository

## Stage 6: Configuring Jenkins Credentials and Job

### Objective
Set up Jenkins credentials and create a pipeline job that connects to your GitHub repository.

### Instructions

1. **Configure DockerHub Credentials in Jenkins**
   - Go to "Manage Jenkins" → "Manage Credentials"
   - Click on "Global" domain
   - Click "Add Credentials"
   - Select "Username with password"
   - Username: Your DockerHub username
   - Password: Your DockerHub password (or access token)
   - ID: `dockerhub-credentials`
   - Description: "DockerHub Credentials"

2. **Create a New Pipeline Job**
   - Click "New Item" in Jenkins dashboard
   - Enter item name: `devops-pipeline-project`
   - Select "Pipeline" and click OK

3. **Configure the Pipeline Job**
   - In the job configuration:
     - Under "Pipeline" section:
       - Definition: "Pipeline script from SCM"
       - SCM: Git
   - Repository URL: `https://github.com/YOUR_GITHUB_USERNAME/apcv_405_app.git`
       - Branch: `*/main`
       - Script Path: `Jenkinsfile`
   - Save the configuration


### Resources
- [Jenkins Credentials Plugin](https://plugins.jenkins.io/credentials/)
- [GitHub Integration Plugin](https://plugins.jenkins.io/github-integration/)

## Stage 7: Running and Testing the Complete Pipeline

### Objective
Execute the complete CI/CD pipeline and verify all stages work correctly.

### Instructions

1. **Trigger the Initial Build**
   - Go to your Jenkins job dashboard
   - Click "Build Now"
   - Monitor the build progress in "Console Output"

2. **Verify Each Stage**
   - **Checkout**: Confirms code is pulled from GitHub
   - **Install Dependencies**: Packages are installed successfully
   - **Run Tests**: All tests pass
   - **Build Docker Image**: Image is created successfully
   - **Push to DockerHub**: Image is pushed to your DockerHub repository
   - **Deploy Locally**: Container is running locally
   - **Health Check**: Application responds to health endpoint

3. **Test the Deployed Application**
   - Open browser and navigate to:
     - APCV 405 Project App: http://localhost:9090`

4. **Verify DockerHub Repository**
   - Log into your DockerHub account
   - Confirm your image repository exists with the latest tag


### Resources
- [Jenkins Build Monitoring](https://www.jenkins.io/doc/book/using/builds/)
- [DockerHub Repository Management](https://docs.docker.com/docker-hub/repos/)

## Stage 8: Documentation and Cleanup

### Objective
Document your pipeline and clean up resources.

### Instructions

1. **Create Documentation**
   - Update your repository README.md with:
     - Project description
     - Build instructions
     - Deployment steps
     - Pipeline status badge (optional)

2. **Create a Pipeline Diagram**
   - Document the flow: GitHub → Jenkins → DockerHub → Local Deployment
   - Include screenshots of successful pipeline execution

3. **Cleanup Resources**
   - Stop and remove test containers: `docker stop apcv_405_app && docker rm apcv_405_app`
   - Clean up old Docker images: `docker image prune`

### Example README.md Addition
```markdown
## CI/CD Pipeline

This project includes an automated CI/CD pipeline using Jenkins that:

1. Pulls code from GitHub
2. Runs automated tests
3. Builds a Docker image
4. Pushes the image to DockerHub
5. Deploys the container locally
6. Performs health checks

### Pipeline Status
- Build: [![Build Status](http://localhost:8080/buildStatus/icon?job=devops-pipeline-project)](http://localhost:8080/job/devops-pipeline-project/)

### Manual Deployment
```bash
docker pull your-dockerhub-username/apcv_405_app:latest
docker run -p 9090:8080 your-dockerhub-username/apcv_405_app:latest
```
```

## Troubleshooting

### Common Issues and Solutions

1. **Jenkins Cannot Connect to Docker**
   - Ensure Docker daemon is running
   - Verify Jenkins has permission to access Docker socket
   - Check Docker plugin installation

2. **DockerHub Push Fails**
   - Verify credentials are correctly configured
   - Check DockerHub repository exists and is accessible
   - Ensure image name matches DockerHub repository format

3. **Tests Fail in Pipeline**
   - Run tests locally first to debug
   - Check dependency installation in Jenkins
   - Verify test environment setup

4. **Application Won't Start in Container**
   - Check Dockerfile syntax
   - Verify all dependencies are included
   - Test container locally before pipeline

### Useful Commands
```bash
# View Jenkins logs
docker logs jenkins

# Debug Docker builds
docker build --no-cache -t test-image .

# Check running containers
docker ps

# View container logs for the project app container
docker logs apcv_405_app
```

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| GitHub Repository Setup | 15 | Repository forked within student's account |
| Jenkins Configuration | 20 | Jenkins properly installed and configured with necessary plugins |
| Pipeline Implementation | 35 | Complete Jenkinsfile with all required stages |
| DockerHub Integration | 25 | Successful image push to DockerHub |
| Documentation | 5 | Clear documentation and README updates |

**Total: 100 Points**

## Submission Requirements

Please submit a Word document in D2L with the following:

1. **GitHub Repository URL** for your forked repository
2. **DockerHub Repository URL** showing published images
3. **Jenkins Pipeline Screenshots** showing successful execution

## Additional Resources

- [DevOps Practices Guide](https://aws.amazon.com/devops/what-is-devops/)
- [CI/CD Best Practices](https://docs.gitlab.com/ee/ci/pipelines/pipeline_efficiency.html)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Jenkins Tutorial](https://www.jenkins.io/doc/tutorials/)
- [GitHub Actions vs Jenkins](https://github.com/features/actions)
