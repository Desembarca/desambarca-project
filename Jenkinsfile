pipeline {
    agent any

    stages {
        stage('Clonar projeto') {
            steps {
                // Quando você usa Jenkinsfile, o Jenkins já clona o repo
                echo 'Código já clonado automaticamente.'
            }
        }

        stage('Instalar dependências') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Rodar testes Django') {
            steps {
                sh '''
                    source venv/bin/activate
                    python manage.py test loja
                '''
            }
        }
    }
}
