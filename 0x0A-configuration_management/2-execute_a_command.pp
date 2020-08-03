# Kill the process named killmenow
exec { 'killmenow':
  path    => '/usr/bin/pkill -f killmenow',
}
