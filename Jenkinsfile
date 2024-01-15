pipeline {
    agent any

    environment {
        GITHUB_TOKEN = credentials('github')
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([$class: 'GitSCM', branches: [[name: 'refs/heads/main']], userRemoteConfigs: [[url: 'https://github.com/sc-govsin/sample-flask']]])
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
        always {
            script {
                // GitHub Checks script
                def GITHUB_API_URL = 'https://api.github.com'
                def GITHUB_REPO = 'sc-govsin/sample-flask'
                def GIT_COMMIT = sh(script: 'git rev-parse HEAD', returnStdout: true).trim()

                sh """
                    curl -X POST \
                    -u sc-govsin:${GITHUB_TOKEN} \
                    -H 'Accept: application/vnd.github.v3+json' \
                    -d '{
                        "name": "Jenkins",
                        "head_sha": "${GIT_COMMIT}",
                        "status": "${currentBuild.currentResult}",
                        "conclusion": "${currentBuild.currentResult == 'SUCCESS' ? 'success' : 'failure'}",
                        "output": {
                            "title": "Jenkins Tests",
                            "summary": "${currentBuild.currentResult == 'SUCCESS' ? 'All tests passed!' : 'Tests failed!'}",
                            "text": "Check the Jenkins logs for more details."
                        }
                    }' \
                    ${GITHUB_API_URL}/repos/${GITHUB_REPO}/check-runs
                """
            }
        }
    }
}
