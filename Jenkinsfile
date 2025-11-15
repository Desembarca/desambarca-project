pipeline {
    agent any

    stage('Clonar projeto') {
    steps {
        git branch: 'main',
            credentialsId: 'github-token',
            url: 'https://github.com/Paulo-FelixP/desambarca-project.git'
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
