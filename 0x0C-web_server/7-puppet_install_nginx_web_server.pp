# configure a new ubuntu server with nginx

package {'install nginx':
  name     => 'nginx',
  command  => 'sudo apt update; sudo apt install -y nginx;',
  provider => shell
}

exec {'change_mode':
  command  => 'sudo chmod 777 /var/www/html',
  provider => shell
}

exec {'create file':
  command  => 'echo "Hello World!" > /var/www/html/index.html;sudo chmod 755 /var/www/html',
  provider => shell
}

exec {'chmod site-available':
  command  => 'sudo chmod 777 /etc/nginx/sites-available; sudo chmod 777 /etc/nginx/sites-available/default',
  provider => shell
}

echo {'create server conf':
  command  => 'echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;
    server_name _;

    location / {
                try_files \$uri \$uri/ =404;
      }

    location /redirect_me{
        return 301 https://www.alxafrica.com;
      }
  }" > sites-available/default'
  provider => shell
}

exec {'chmod site-available':
  command  => 'sudo chmod 644 /etc/nginx/sites-available/default;sudo chmod 755 /etc/nginx/sites-available;',
  provider => shell
}

exec {'restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell
}
