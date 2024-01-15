pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                script {
                    checkout scm
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                // Set up Python environment and install dependencies
                script {
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run FastAPI tests
                script {
                    sh 'pytest'
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deploy your FastAPI app (You can customize this based on your deployment strategy)
                script {
                    sh 'python app.py'
                }
            }
        }
    }

    post {
        success {
            // Additional actions to take on successful build
            echo 'Build successful!'
        }
        failure {
            // Additional actions to take on build failure
            echo 'Build failed!'
        }
    }
}
