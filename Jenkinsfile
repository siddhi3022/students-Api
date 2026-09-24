pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'github.com/siddhi3022/student-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t student-api .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker rm -f student-container || true'
                sh 'docker run -d -p 8000:8000 --name student-container student-api'
            }
        }

        stage('Test Application') {
            steps {
                sh 'curl http://localhost:8000'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline Successful!'
        }

        failure {
            echo 'CI/CD Pipeline Failed!'
        }
    }
}