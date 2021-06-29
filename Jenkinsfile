#!groovy

node {

    try {
        stage 'Checkout'
            checkout scm

            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
            def lastChanges = readFile('GIT_CHANGES')

        stage 'Test'
            sh 'pip3 install -r requirements.txt'

        stage 'Deploy'
            sh 'cp ./django_test/settings_dev.py ./django_test/settings.py'
            sh 'pip3 install -r requirements.txt'
            sh 'python3 ./manage.py migrate'
            sh 'python3 ./manage.py runserver 0.0.0.0:8000'
    }

    catch (err) {
        throw err
    }

}