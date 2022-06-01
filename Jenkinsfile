pipeline {
    options {
        buildDiscarder(logRotator(numToKeepStr: '2', artifactNumToKeepStr: '2'))
    }
    agent any
        stages {
            stage('PreBuild') {
                parallel {
                    stage('Pipdeps') {
                        steps {
                            sh 'python3 -m virtualenv venv'
                            sh 'chmod a+x venv/bin/activate'
                            sh '. venv/bin/activate && pip install -r requirements.txt'
                            sh '. venv/bin/activate && pip install codecov pytest pytest-cov mock sphinx'
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
                    sh '. venv/bin/activate && make build'
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
                    sh '. venv/bin/activate && export DISPLAY=:99.0 && make test'
                }
            }
            stage('Deploy') {
                when {
                    branch 'main'
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
                    sh '. venv/bin/activate && make clean'
                }
            }
        }
    }
