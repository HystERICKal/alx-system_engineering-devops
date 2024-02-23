# Let's execute a command

exec { 'pkill':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
