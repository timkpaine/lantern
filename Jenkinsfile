pipeline {
    agent any
        stages {
            stage('PreBuild') {
                parallel {
                    stage('Pipdeps') {
                        steps {
                            sh 'python3 -m virtualenv venv'
                            sh 'chmod a+x venv/bin/activate'
                            sh 'venv/bin/activate'
                            sh 'pip install -r requirements.txt'
                        }
                    }
                    stage('Otherdeps'){
                        steps{
                            sh 'export DISPLAY=:99.0'
                            sh 'Xvfb :99 &'
                            sh 'sleep 3'
                        }
                    }
                }
            }
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
