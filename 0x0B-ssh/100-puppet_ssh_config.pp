# sets up client SSH configuration file

$path_to_file = '/root/.ssh/config' 
$str = "IdentityFile ~/.ssh/school"

file { $path_to_file:
ensure  => 'present',
content => $str
}
