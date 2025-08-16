# Lab 1: Download DevOps Tools

## Exercise: Download and Install Git and Docker


### 1. Download and Install Docker

- Visit the [Docker Desktop download page](https://www.docker.com/products/docker-desktop/).
- Download the appropriate installer for your operating system.
- Follow the installation instructions provided on the website.
- After installation, verify Docker is running by executing:

  ```sh
  docker --version
  ```


### 2. Download and Install Visual Studio Code

- Visit the [Visual Studio Code download page](https://code.visualstudio.com/).

#### For Windows

1. Click the "Windows" download button to get the installer.
2. Run the downloaded `.exe` file and follow the setup instructions.
3. After installation, launch Visual Studio Code.
4. Verify the installation by opening a terminal in VS Code and running:
   ```sh
   code --version
   ```

#### For macOS

1. Click the "macOS" download button to get the `.zip` archive.
2. Open the downloaded `.zip` file and drag the `Visual Studio Code` app to your `Applications` folder.
3. After installation, launch Visual Studio Code.
4. Verify the installation by opening a terminal in VS Code and running:
   ```sh
   code --version
   ```

#### For Linux

1. Visit the [Visual Studio Code download page](https://code.visualstudio.com/) and download the `.deb` (for Debian/Ubuntu) or `.rpm` (for Fedora/Red Hat) package.
2. Install using your package manager. For example:
   - **Debian/Ubuntu:**
     ```sh
     sudo apt install ./<file>.deb
     ```
   - **Fedora/Red Hat:**
     ```sh
     sudo rpm -i <file>.rpm
     ```
3. Alternatively, you can install via Snap:
   ```sh
   sudo snap install --classic code
   ```
4. After installation, launch Visual Studio Code from your applications menu or by running `code` in the terminal.


### 3. Download and Install Git

- Visit the [Git download page](https://git-scm.com/downloads).

#### For Windows

1. Click the "Windows" download link to get the installer.
2. Run the downloaded `.exe` file and follow the setup instructions.
3. After installation, open a terminal or command prompt and run:
   ```sh
   git --version
   ```

#### For macOS

1. Click the "macOS" download link to get the installer.
2. Alternatively, you can install Git using Homebrew by running:
   ```sh
   brew install git
   ```
3. After installation, open a terminal and run:
   ```sh
   git --version
   ```

#### For Linux

1. Use your distribution's package manager to install Git. For example:
   - **Ubuntu/Debian:**
     ```sh
     sudo apt update
     sudo apt install git
     ```
   - **Fedora:**
     ```sh
     sudo dnf install git
     ```
   - **Arch Linux:**
     ```sh
     sudo pacman -S git
     ```
2. After installation, open a terminal and run:
   ```sh
   git --version
   ```


#### Run a Demo Docker Container

After installing Docker, you can verify it works by running a demo container from Docker Hub and interacting with it.

##### a. Run the Hello World Container

Open your terminal and run:

```sh
docker run hello-world
```

This command downloads and runs a simple container that prints a confirmation message.

##### b. Run a Web Server Container

Start an Nginx web server container and map it to port 8080 on your machine:

```sh
docker run --name webdemo -d -p 8080:80 nginx
```

Open your web browser and go to [http://localhost:8080](http://localhost:8080) to see the Nginx welcome page.

##### c. Basic Docker Commands

- **List running containers:**
  ```sh
  docker ps
  ```
- **List all containers (including stopped):**
  ```sh
  docker ps -a
  ```
- **Stop the webdemo container:**
  ```sh
  docker stop webdemo
  ```
- **Remove the webdemo container:**
  ```sh
  docker rm webdemo
  ```

These steps help you confirm Docker is installed and working correctly.


### 4. Submit a Screenshot

Take a screenshot showing the output of both `git --version` and `docker --version` commands in your terminal. Submit this screenshot as proof of successful installation.  Take a screenshot of the output of the Nginx container within your web browser.  Put all screenshots in a Word document with the filename pattern NetId-Lab1.docx (e.g. Milazzom-Lab1.docx) and submit through D2L.