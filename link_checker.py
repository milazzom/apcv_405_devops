# link_checker.py
import requests

links = [
    # week1.md
    "https://learn.microsoft.com/en-us/devops/what-is-devops",
    "https://itrevolution.com/the-devops-handbook/",
    "https://www.geeksforgeeks.org/operating-system-introduction/",
    "https://linuxjourney.com/",
    "https://www.digitalocean.com/community/tutorial_series/getting-started-with-bash-scripting",
    "https://automatetheboringstuff.com/",
    "https://www.coursera.org/learn/cloud-computing-basics",
    "https://learn.microsoft.com/en-us/training/paths/azure-fundamentals/",
    "https://www.redhat.com/en/topics/virtualization/what-is-virtualization",
    "https://www.docker.com/resources/what-container/",
    "https://cloud.google.com/devops",
    "https://dora.dev/",
    # week2.md
    "https://www.atlassian.com/devops",
    "https://itrevolution.com/the-phoenix-project/",
    "https://learn.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-powershell",
    "https://docs.ansible.com/ansible/latest/getting_started/index.html",
    "https://www.aws.training/Details/Curriculum?id=20685",
    "https://cloud.google.com/solutions/devops",
    "https://developer.hashicorp.com/terraform/tutorials/aws-get-started",
    "https://docs.aws.amazon.com/cloudformation/index.html",
    "https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration",
    "https://www.jenkins.io/doc/",
    # week3.md
    "https://www.redhat.com/en/topics/automation/what-is-software-deployment",
    "https://www.atlassian.com/continuous-delivery/build-tools",
    "https://docs.npmjs.com/about-dependencies-and-devdependencies",
    "https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html",
    "https://www.geeksforgeeks.org/compiler-design-tutorials/",
    "https://www.freecodecamp.org/news/how-do-compilers-work/",
    "https://learn.microsoft.com/en-us/azure/devops/pipelines/process/pipelines-as-code",
    "https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions",
    "https://aws.amazon.com/devops/continuous-delivery/",
    "https://www.jenkins.io/doc/book/pipeline/",
    # week4.md
    "https://www.atlassian.com/it-unplugged/change-management/devops-change-management",
    "https://learn.microsoft.com/en-us/azure/devops/learn/what-is-release-management",
    "https://guides.github.com/introduction/git-handbook/",
    "https://docs.github.com/en/get-started/quickstart/github-flow",
    "https://docs.github.com/en/actions/publishing-packages/publishing-nodejs-packages",
    "https://www.jenkins.io/doc/book/pipeline/release/",
    "https://www.guru99.com/software-testing.html",
    "https://jmeter.apache.org/usermanual/get-started.html",
    "https://www.browserstack.com/guide/regression-testing",
    "https://www.redhat.com/en/topics/devops/what-is-devsecops",
    "https://owasp.org/www-project-devsecops-best-practices/",
    "https://docs.github.com/en/code-security",
    "https://learn.microsoft.com/en-us/azure/devops/learn/security-devops",
    # week5.md
    "https://www.redhat.com/en/topics/automation/what-is-software-packaging",
    "https://docs.docker.com/get-started/overview/",
    "https://packaging.python.org/en/latest/tutorials/packaging-projects/",
    "https://www.ibm.com/cloud/blog/containerization-vs-virtualization",
    "https://developer.hashicorp.com/terraform/tutorials/aws-get-started",
    "https://docs.ansible.com/ansible/latest/index.html",
    "https://learn.microsoft.com/en-us/devops/deliver/what-is-infrastructure-as-code",
    "https://www.pulumi.com/what-is/infrastructure-as-code/",
    "https://www.atlassian.com/continuous-delivery/automated-deployment",
    "https://docs.github.com/en/actions/deployment/about-deployments",
    # week6.md
    "https://www.red-gate.com/solutions/database-devops/",
    "https://flywaydb.org/documentation/",
    "https://stackoverflow.com/questions/337701/what-are-the-pros-and-cons-of-the-various-configuration-file-formats",
    "https://12factor.net/config",
    "https://www.nginx.com/learn/service-mesh/",
    "https://istio.io/latest/docs/",
    "https://www.atlassian.com/it-unplugged/configuration-management/what-is-configuration-management",
    "https://docs.chef.io/",
    "https://learn.microsoft.com/en-us/devops/monitor/telemetry",
    "https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview",
    # week7.md
    "https://prometheus.io/docs/introduction/overview/",
    "https://grafana.com/docs/grafana/latest/",
    "https://grafana.com/tutorials/",
    "https://prometheus.io/docs/alerting/latest/alertmanager/",
    "https://www.elastic.co/what-is/elk-stack",
    "https://docs.splunk.com/Documentation/Splunk/latest",
    "https://learn.microsoft.com/en-us/azure/architecture/guide/deployment/deployment-strategies",
    "https://www.atlassian.com/continuous-delivery/continuous-deployment",
    "https://dora.dev/"
]

for url in links:
    try:
        response = requests.get(url, timeout=10)
        print(f"{url} - {response.status_code}")
    except Exception as e:
        print(f"{url} - ERROR: {e}")
