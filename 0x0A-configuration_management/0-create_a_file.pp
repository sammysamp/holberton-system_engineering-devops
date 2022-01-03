# Create a file, using DSL for Puppet

file { 'school':
  ensure  => 'present',
  path    => '/tmp/school',
  mode    => '0744',
  group   => 'www-data',
  owner   => 'www-data',
  content => 'I love Puppet',
}
