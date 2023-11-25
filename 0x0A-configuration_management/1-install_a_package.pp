# Install flask version 2.1.0 from pip3

$package = 'flask==2.1.0'

package { $package :
ensure   => 'installed',
provider => 'pip3'
}
