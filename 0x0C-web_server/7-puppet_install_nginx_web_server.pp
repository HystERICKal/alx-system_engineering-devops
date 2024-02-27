# Now let's Install Nginx web server with puppet

package { 'nginx':
  ensure     => 'installed',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'aaaaa':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
