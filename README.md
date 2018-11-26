# taskman 
REST API example with Django Rest Framework
A simple REST API that provides some functionality for managing project tasks

# APIs
```
admin/
api/v1/
report/
```

### api/v1/
- users
```
api/v1/users/ # list of users
api/v1/rest-auth/login/ # user authorization
api/v1/rest-auth/logout/
api/v1/rest-auth/registration/ # add new user
```
- projects
```
api/v1/projects/ # get projects list/ add new project
api/v1/projects/<int:pk>/ # get concrete project
```
- tasks
```
api/v1/tasks/ # get tasks list/ add new task
api/v1/tasks/<int:pk>/ # get concrete task
```

### report/
```
report/ # generate tasks report
report/send/ # send report via mail
```
