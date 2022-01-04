# Execute a command
exec { 'I will kill you':
  command  => 'pkill -f killmenow',
  provider => shell,
}
