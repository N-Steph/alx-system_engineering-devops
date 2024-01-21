# Configures the client SSH configuration file to use the private key ~/.ssh/school

$config_content = "Host 236263-web-01\n\tHostName 54.162.2.130\n\tUser ubuntu\n\tIdentityFile ~/.ssh/school"

file {'/root/.ssh/config':
  ensure  => present,
  content => $config_content
  }
