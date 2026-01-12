#!/bin/bash

# Update system packages
sudo apt-get update -y

# Install prerequisites
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker's official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package index
sudo apt-get update -y

# Install Docker Engine, Docker Compose plugin, and containerd
sudo apt-get install -y \
    docker-ce \
    docker-ce-cli \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin

# Start and enable Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Install Java (OpenJDK 17 - recommended for Jenkins)
sudo apt-get install -y openjdk-17-jdk

# Add ubuntu user to docker group (change 'ubuntu' if using different user)
sudo usermod -aG docker ubuntu

# Verify installations
echo "========================================"
echo "Docker version:"
docker --version

echo "========================================"
echo "Docker Compose version:"
docker compose version

echo "========================================"
echo "Java version:"
java -version

echo "========================================"
echo "Docker service status:"
sudo systemctl status docker --no-pager

echo "========================================"
echo "Installation complete!"
echo "NOTE: Log out and log back in for docker group changes to take effect"
echo "Or run: newgrp docker"
