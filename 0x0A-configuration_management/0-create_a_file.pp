# Create a file named school in /tmp directory

$path_file = '/tmp/school'

file { $path_file:
ensure  => 'present',
content => 'I love Puppet',
owner   => 'www-data',
group   => 'www-data',
mode    => '0744'
}
