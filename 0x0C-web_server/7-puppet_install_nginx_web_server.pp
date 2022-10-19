# Install nginx with puppet and configure it

package { 'nginx':
  ensure => 'installed'
}

include nginx

class { 'nginx':
  manage_repo    => true,
  package_source => 'nginx-stable'
}

nginx::resource::server { '34.73.76.135':
  listen_port      => 80,
  www_root         => '/var/www/html/',
  vhost_cfg_append => { 'rewrite' => '^/redirect_me https://www.alxafrica.com/ permanent' }
}

file { 'index':
  path    => '/var/www/html/index.html',
  content => 'Hello World!'
}
