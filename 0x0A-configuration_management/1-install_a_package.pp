# This manifest installs flask from pip3

exec { '/usr/bin/pip3 install -U werkzeug==2.1.1':
  command => '/usr/bin/pip3 install -U werkzeug==2.1.1'
}

exec { '/usr/bin/pip3 install flask==2.1.0':
  command => '/usr/bin/pip3 install flask==2.1.0',
  require => Exec['/usr/bin/pip3 install -U werkzeug==2.1.1']
  }
