pipeline {
    agent any
        stages {
            stage('PreBuild') {
                steps {
                parallel {
                    phase1: {
                        sh 'pip install -r requirements.txt'
                    },
                    phase2: {
                        sh 'export DISPLAY=:99.0'
                        sh -e '/etc/init.d/xvfb start'
                        sh 'sleep 3'
                    }
                }
                sh 'make build'
                post {
                    success {
                        echo 'Build succeeded.'
                    }
                    failure {
                        echo 'Build failed.'
                    }
                }
            }
            stage('Test') {
                steps {
                    sh 'make test'
                }
            }
            stage('Deploy') {
                when {
                    branch 'master'
                }
                steps {
                    echo 'This is the Deploy Stage'
                }
                post {
                    success {
                        echo 'Deploy succeeded'
                    }
                    failure {
                        echo 'Deploy failed'
                    }
                }
            }
            stage('Cleanup') {
                steps {
                    sh 'make clean'
                }
            }
        }
    }
