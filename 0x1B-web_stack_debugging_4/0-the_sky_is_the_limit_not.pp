# Puppet manifest to change the max number of open file for nginx

exec { 'set_nginx_ulimit':
  command => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 65535\"/' /etc/default/nginx",
  path    => ['/bin', '/usr/bin'],
  unless  => "grep -q '^ULIMIT=\"-n 65535\"' /etc/default/nginx",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
}
