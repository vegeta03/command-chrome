import os

def remove_karma_jasmine():
    dependencies = [
        'karma',
        'karma-chrome-launcher',
        'karma-coverage',
        'karma-jasmine',
        'karma-jasmine-html-reporter',
        '@types/jasmine',
        'jasmine-core'
    ]
    os.system('npm uninstall ' + ' '.join(dependencies))

remove_karma_jasmine()

if os.path.exists('karma.conf.js'):
    os.remove('karma.conf.js')