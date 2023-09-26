# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Update package list and install Nginx
exec { 'apt_update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
  before  => Package['nginx'],
}

# Create index.html file with Hello World!
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    root /var/www/html;
    index index.html;

    location /redirect_me {
        return 301 https://blog.ehoneahobed.com/;
    }
}
",
  require => [Package['nginx'], File['/var/www/html/index.html']],
}

# Restart Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/nginx/sites-available/default'],
}
