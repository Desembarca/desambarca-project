pipeline {
    agent {
        docker {
            image 'python:5.7.2-slim'
    stages {

        stage('Instalar dependências') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Rodar testes Django') {
            steps {
                sh '''
                    . venv/bin/activate
                    python manage.py test
                '''
            }
        }

    }
}
