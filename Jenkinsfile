pipeline {
    agent any

    environment {
        GITHUB_TOKEN = credentials('github')
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'python3 -m venv appenv'
                    sh '. appenv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '. appenv/bin/activate && python3 -m pytest --junit-xml=test-results.xml'
                }
            }
        }

        post {
        failure {
                // Handle failure if needed
                echo 'Build failed!'
                }
        }

        stage('GitHub Checks') {
            steps {
                catchError(buildResult: 'SUCCESS') {
                    script {
                        def GITHUB_API_URL = 'https://api.github.com'
                        def GITHUB_REPO = 'sc-govsin/sample-flask'
                        def GIT_COMMIT = sh(script: 'git rev-parse HEAD', returnStdout: true).trim()

                        // Report test results to GitHub as a check run
                        sh """
                            curl -X POST \
                            -u sc-govsin:${GITHUB_TOKEN} \
                            -H 'Accept: application/vnd.github.v3+json' \
                            -d '{
                                "name": "Jenkins",
                                "head_sha": "${GIT_COMMIT}",
                                "status": "completed",
                                "conclusion": "success",
                                "output": {
                                    "title": "Jenkins Tests",
                                    "summary": "All tests passed!",
                                    "text": "Check the Jenkins logs for more details."
                                }
                            }' \
                            ${GITHUB_API_URL}/repos/${GITHUB_REPO}/check-runs
                        """
                    }
                }
            }
        }
    }
}
