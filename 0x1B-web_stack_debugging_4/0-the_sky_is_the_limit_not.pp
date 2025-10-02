# Puppet manifest to change the max number of open file for nginx

file_line { 'nginx_ulimit':
  path   => '/etc/default/nginx',
  line   => 'ULIMIT="-n 65535"',
  match  => '^ULIMIT=',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure => running,
}
