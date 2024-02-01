# Installing and configurint nginx

package {'Install nginx':
  ensure => installed,
  name   => 'nginx',
}

file {'custom error page':
  ensure  => present,
  path    => '/usr/share/nginx/html/custom_404.html',
  content => 'Ceci n\'est pas une page',
  require => Package['Install nginx']
}

exec {'landing page content':
  command => 'echo "Hello World!" > /var/www/html/index.nginx-debian.html',
  path    => '/usr/bin/',
  require => Package['Install nginx']
}

exec {'redirection and custom_404.html page content':
  command => 'sed -i "s/server_name _;/server_name _;\n\trewrite\
 ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;\
\n\n\terror_page 404 \/custom_404.html;\n\tlocation = \/custom_404.html \
  {\n\t\troot \/usr\/share\/nginx\/html;\n\t\tinternal;\n\t}\n/" /etc/nginx/sites-available/default',
  path    => '/usr/bin/',
  require => Package['Install nginx']
}

exec {'nginx listen on port 80':
  command =>'/usr/sbin/ufw nginx \'HTTPS\'',
  require => Package['Install nginx']
}

exec { 'custom http response header':
  command => 'sed -i "s/http {/http {\n\tadd_header X-Served-By $HOSTNAME always;\n/" /etc/nginx/nginx.conf',
  path    => '/usr/bin',
  require => Package['Install nginx']
}

service {'restart nginx':
  ensure  => running,
  name    => 'nginx',
  restart => 'service nginx restart',
  require => [
    Package['Install nginx'],
    File['custom error page'],
    Exec['landing page content'],
    Exec['redirection and custom_404.html page content'],
    Exec['custom http response header']
    ]
}
