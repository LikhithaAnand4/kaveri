pipeline{
   agent any
   stages{
      stage('Checkout'){
        steps{
          checkout scm
        }
       }
      stage('Build'){
         steps{
            echo 'Checking Python application'
            bat '"C:\\Users\\STUDENT\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m py_compile app.py'
             }
       }
      stage('Test'){
          steps{
             echo 'Executing automated tests'
             bat 'python -m unittest app'
             }
          }
      stage('Run Application'){
           steps{
              bat 'python app.py'
            }
      }
}
post{
  success{
      echo 'CI Pipeline completed successfully'
  }
 failure{
      echo 'CI Pipeline failed'
    }
 }
}
