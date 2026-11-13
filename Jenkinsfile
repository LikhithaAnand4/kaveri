
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python application'
                bat '"C:\\Users\\STUDENT\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Executing automated tests'
                bat '"C:\\Users\\STUDENT\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m unittest app'
            }
        }

        stage('Run Application') {
            steps {
                echo 'Running Python application'
                bat '"C:\\Users\\STUDENT\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" app.py'
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline completed successfully'
        }

        failure {
            echo 'CI Pipeline failed'
        }
    }
}
