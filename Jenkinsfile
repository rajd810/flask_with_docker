pipeline {
    agent any
    stages {
        stage("Clone Git Repository") {
            steps {
                git(
                    url: "https://github.com/rajd810/flask_with_docker.git",
                    branch: "main",
                    changelog: true,
                    poll: true
                )
            }
        }
    }
}