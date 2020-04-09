# odoo-13-docker

### Make the container to access these folders:

```
$ sudo chmod -R 777 addons
$ sudo chmod -R 777 etc/odoo
```

### Start the container:

```$ docker-compose up```

### Then open localhost:8071 to access Odoo 13.0. If you want to start the server with a different port, change 8071 to another value:

### ports:
``` - "8071:8069"```

### Log file viewed on etc/odoo-server.log
