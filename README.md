##### Build and run

```
export DB_NAME=project 
export DB_USER=project
export DB_PASSWORD=project 
export DB_PORT=5432 
export SECRET_KEY=project 
export DJANGO_SUPERUSER_USERNAME=admin 
export DJANGO_SUPERUSER_EMAIL=admin@admin.admin 
export DJANGO_SUPERUSER_PASSWORD=admin 
export API_URI=https://probe.fbrq.cloud/v1/send 
export JWT_TOKEN=<TOKEN>

docker-compose up --build
```

#### You need to log in

`http://localhost/admin`  
`admin` `admin`

### API

`http://localhost/api/`

#### Create a mailing list (use the form below)

`http://localhost/api/messages/`

#### Create mailing (use the form below)

`http://localhost/api/deliveries/`

#### Create mailing clients (use the form below)

`http://localhost/api/clients/`

#### Add a client to the mailing list (use the form below)

`http://localhost/api/memberships/`

