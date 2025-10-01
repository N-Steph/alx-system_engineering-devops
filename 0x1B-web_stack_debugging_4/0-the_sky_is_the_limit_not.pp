# Puppet manifest to modify nginx.conf

# Uncomment multi_accept on;
exec { 'uncomment_multi_accept':
  command => "/bin/sed -i 's/^[[:space:]]*#[[:space:]]*multi_accept on;/    multi_accept on;/' /etc/nginx/nginx.conf",
  onlyif  => "/bin/grep -q '^[[:space:]]*#[[:space:]]*multi_accept on;' /etc/nginx/nginx.conf",
}

# Add open_file_cache directives to http block
exec { 'add_open_file_cache':
  command => "/bin/sed -i '/^http {/a\\     open_file_cache max=5000 inactive=60s;\\n' /etc/nginx/nginx.conf",
  unless  => "/bin/grep -q 'open_file_cache max=' /etc/nginx/nginx.conf",
}

exec { 'add_open_file_cache_min_uses':
  command => "/bin/sed -i '/^http {/a\\        open_file_cache_min_uses 1;\\n' /etc/nginx/nginx.conf",
  unless  => "/bin/grep -q 'open_file_cache_min_uses' /etc/nginx/nginx.conf",
}

exec { 'add_open_file_cache_errors':
  command => "/bin/sed -i '/^http {/a\\        open_file_cache_errors on;' /etc/nginx/nginx.conf",
  unless  => "/bin/grep -q 'open_file_cache_errors' /etc/nginx/nginx.conf",
}

# Restart nginx to apply changes
exec { 'restart_nginx':
  command     => '/usr/sbin/nginx -t && /usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => [Exec['uncomment_multi_accept'], Exec['add_open_file_cache'],
  Exec['add_open_file_cache_min_uses'], Exec['add_open_file_cache_errors']],
}