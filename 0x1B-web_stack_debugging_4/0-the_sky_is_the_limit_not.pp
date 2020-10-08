exec { 'fix-nginx-open-files':
command => '/bin/sed -i \'s/ULIMIT="-n 15"/ULIMIT="-n 4096"/\' /etc/default/nginx',
}

exec { 'restart nginex':
command => '/usr/sbin/service nginx restart',
}
