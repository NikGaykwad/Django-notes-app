pipeline {
    agent { label "jenkin-agent-1" }

    stages {

        stage("Code") {
            steps {
                echo "Cloning the code from GitHub"
                git url: "https://github.com/NikGaykwad/Django-notes-app.git", branch: "main"
                echo "Successfully cloned the code from GitHub...!"
            }
        }

        stage("Build") {
            steps {
                echo "Building Docker image"
                sh "docker build -t notes-app:latest ."
            }
        }

        stage("Push to DockerHub") {
            steps {
                echo "Pushing image to DockerHub"

                withCredentials([usernamePassword(
                    credentialsId: "dockerHubCreds",
                    usernameVariable: "dockerHubUser",
                    passwordVariable: "dockerHubPass"
                )]) {

                    sh '''
                    echo "$dockerHubPass" | docker login -u "$dockerHubUser" --password-stdin
                    docker tag notes-app:latest $dockerHubUser/notes-app:latest
                    docker push $dockerHubUser/notes-app:latest
                    '''
                }
            }
        }

        stage("Deploy with docker compose") {
            steps {
                echo "Deploying application"

                sh "docker compose down && docker compose up -d --build"
                
                echo "Application is running on port 8000"
            }
        }
    }
}
