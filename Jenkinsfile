pipeline {
    agent any
        stages {
            stage('Build') {
                steps {
                    sh 'make build'
                }
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
