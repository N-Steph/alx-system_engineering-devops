# Puppet manifest to increase the max number of files
# the user holberton can open

exec { 'set hard ulimit':
  command => "sed -i 's/^holberton hard nofile */holberton hard nofile 4096/' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
  unless  => "grep -q 'holberton hard nofile 4096' /etc/security/limits.conf",
}

exec { 'set soft ulimit':
  command => "sed -i 's/^holberton soft nofile */holberton soft nofile 4096/' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
  unless  => "grep -q 'holberton soft nofile 4096' /etc/security/limits.conf",
}
