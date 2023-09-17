# Djagno-Adminlte Raspberry


## Configuraciones de raspberry para desplegar django-adaminlte-3 en apache2

* `sudo apt-get update`
* `sudo apt-get install apache2`
* `sudo apt-get install libapache2-mod-wsgi-py3`

### venv
* `sudo apt-get install python3-pip`
* `sudo pip install virtualenv`
* `pip install virutalenv`
* `virtualenv .venv`
* `source .venv/bin/activate`
* `pip install -r requirements.txt`

## django
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py collectstatic`



### apache2
z
## WSGIDaemonProcess en nuevo puerto

### Cambiar Puerto en 'ports.conf'

# Deshabilitar sitio(en caso de querer usar puertos ya creados)
* `sudo a2dissite file.conf`

* `Listen ##`
### Crear fichero 'file.conf' en 'sities-available'
``` 
<VirtualHost *:##>
	Alias /static/ /path/static/
	<Directory /path/static>
		Require all granted
	</Directory>

	WSGIScriptAlias / /path/config/wsgi.py
	WSGIDaemonProcess django python-path=/path python-home=/path/.venv
	WSGIProcessGroup django
	WSGIScriptAlias / /path/config/wsgi.py

	<Directory /path/config>
		<Files wsgi.py>
			Require all granted
		</Files>
	</Directory>
</VirtualHost>
```
* `sudo a2ensite file.conf`
* `sudo systemctl reload apache2`


## WSGIPythonHome en puerto default apache

* `sudo nano /etc/apache2/sites-available/000-default.conf`
```
<VirtualHost *:80>
    #...
</VirtualHost>

#STATIC
Alias /static/ /project/static/
<Directory /project/static>
    Require all granted
</Directory>

#MEDIA
Alias /media/ /project/media/
<Directory /project/media>
    AllowOverride None
    Require all granted
</Directory>

#WSGI
WSGIScriptAlias / /project/app/wsgi.py
WSGIPythonHome /project/.venv
WSGIPythonPath /project
<Directory /project/app>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>
```
* `sudo service apache2 restart`

### i2c permiso
* `sudo usermod -aG i2c www-data`
* `sudo systemctl restart apache2`

### permisos
* `sudo chmod 664 ./db.sqlite3`
* `sudo chmod 777 ./`
* `sudo chown :www-data ./db.sqlite3`
* `sudo chown :www-data ./`
* `sudo service apache2 restart`


