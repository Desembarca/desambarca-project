pipeline {
    agent any

    stages {

        stage('Clonar projeto') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Paulo-FelixP/desambarca-project'
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
                    python manage.py test
                '''
            }
        }

    }
}
