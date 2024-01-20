$doc_root = '/tmp/school'

file { $doc_root:
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
  }
