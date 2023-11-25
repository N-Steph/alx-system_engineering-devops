# Install flask version 2.1.0 from pip3

$package = 'flask==2.1.0'

exec { 'pip3 install werkzeug==2.1.1':
command => '/usr/bin/pip3 install werkzeug==2.1.1'
}

package { $package :
ensure   => 'installed',
provider => 'pip3',
require  => Exec['pip3 install werkzeug==2.1.1']
}
