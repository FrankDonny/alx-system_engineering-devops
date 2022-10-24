package {'nginx':
  ensure => 'installed',
}

file {'/var/www/html':
  ensure => 'directory',
  mode   => '0777'
}

file {'/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!'
}

file {'/var/www/html':
  ensure => 'directory',
  mode   => '0755'
}

file {'/etc/nginx/sites-available':
  ensure => 'directory',
  mode   => '0777'
}

$serve = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    include snippets/err_page.conf;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;
    server_name _;
    return 301 https://www.alxafrica.com$request_uri;

    location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404 error page.
                try_files $uri $uri/ =404;
    }

    # location /redirect_me {
    #     return 301 https://www.alxafrica.com;
    # }
}"

file {'/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => $serve,
  mode    => '0644'
}

file {'/etc/nginx/sites-available':
  ensure => 'directory',
  mode   => '0755'
}

exec {'restart nginx':
  command => 'sudo service nginx restart'
}
