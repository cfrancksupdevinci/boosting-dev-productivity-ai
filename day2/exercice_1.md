## Exercise 1: Creating a DevOps Template Repository with GitHub Copilot

### Objective
Create a comprehensive DevOps template repository that can be used as a starting point for future projects, utilizing GitHub Copilot to accelerate development and implement best practices.

### Exercise Steps

#### 1. Repository Setup
- Create a new GitHub repository named "devops-template"
- Clone it locally
- Use Copilot to help you create a comprehensive README.md by typing a comment like:
  ```markdown
  <!-- Create a detailed README for a DevOps template repository that includes sections on purpose, components, setup instructions, and usage examples -->
  ```

#### 2. Project Structure Creation 
- With Copilot's assistance, create the following directory structure:
  - `.github/workflows/` (for CI/CD)
  - `docker/` (for containerization)
  - `terraform/` (for infrastructure)
  - `scripts/` (for automation scripts)
  - `monitoring/` (for monitoring configs)
  - `docs/` (for documentation)

- Create placeholder files in each directory and use Copilot to help document their purpose

#### 3. CI/CD Pipeline Implementation 
- Navigate to `.github/workflows/`
- Create the following files with Copilot's help:
  - `ci.yml` - Ask Copilot: "Create a GitHub Actions workflow for continuous integration that runs tests, performs linting, and builds Docker images"
  - `cd.yml` - Ask Copilot: "Create a GitHub Actions workflow for continuous deployment that deploys to staging and production environments with proper approvals"


#### 4. Containerization Templates 
- In the `docker/` directory, use Copilot to help create:
  - A base Dockerfile for a Node.js application
  - A base Dockerfile for a Python application
  - A docker-compose.yml file for local development
  - Add comments before each section asking Copilot to incorporate best practices

#### 5. Infrastructure as Code 
- In the `terraform/` directory, create subdirectories for:
  - `modules/` - Common infrastructure components
  - `environments/` - Environment-specific configurations
  
- Use Copilot to help you create:
  - A VPC module with public and private subnets
  - An ECS or Kubernetes cluster module
  - Environment configurations for dev, staging, and production
  - Remote state configuration

#### 6. Monitoring and Observability 
- In the `monitoring/` directory, use Copilot to help create:
  - Prometheus configuration
  - Grafana dashboard definitions
  - Log aggregation setup
  - Alerting rules

#### 7. Automation Scripts 
- In the `scripts/` directory, use Copilot to help create:
  - A setup script that initializes the project
  - A database backup/restore script
  - A deployment verification script
  - A performance testing script

#### 8. Documentation 
- In the `docs/` directory, have Copilot help you create:
  - Architecture diagrams (in Mermaid format)
  - Runbooks for common operations
  - Troubleshooting guide
  - Onboarding documentation for new team members
