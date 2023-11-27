# sets up client SSH configuration file

$path_to_file = '/root/.ssh/config'
$str = "Host\n\tHostName ubuntu\n\tUser ubuntui\n\tPort 22\n\tIdentityFile ~/.ssh/school"

file { $path_to_file :
ensure  => 'present',
path    => $path_to_file,
content => $str
}
