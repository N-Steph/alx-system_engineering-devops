# Conigures the client SSH configuration file to use the private key ~/.ssh/school

$config_content = '/usr/bin/sed "s/#   IdentityFile ~\/.ssh\/id_rsa/IdentityFile ~\/.ssh\/school/" /etc/ssh/ssh_config > /etc/ssh/ssh_config'

exec {$config_content:
  command => $config_content
  }
