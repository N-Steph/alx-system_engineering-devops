# Installing and configurint nginx

exec { 'custom http response header':
  command => 'sed -i "s/http {/http {\n\tadd_header X-Served-By $HOSTNAME always;\n/" /etc/nginx/nginx.conf',
  path    => '/usr/bin',
  Before  => Package['Install nginx']
}

service {'restart nginx':
  ensure  => running,
  name    => 'nginx',
  restart => 'service nginx restart'
}
