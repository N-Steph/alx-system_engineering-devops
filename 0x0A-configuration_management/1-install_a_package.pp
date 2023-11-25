# Install flask version 2.1.0 from pip3

exec { 'pip3 install flask==2.1.0':
command => '/usr/bin/pip3 install flask==2.1.0'
}
