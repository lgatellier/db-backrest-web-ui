# DB Backup & Restore Web UI
This project is a web application aiming to be a web abstraction of RDBMS backup & restore tools in a multi-application, multi-environment context.

Today, only public Cloud Service Providers (CSP) provide a web UI to easily trigger managed RDBMS backups and restores.

This project aims to be a similar, lightweight web UI on top of an existing orchestration tool (only Ansible AWX, at the beginning).

## Features
This project has just began, and should handle the following features soon :
- [ ] Handle a list of applications, and a list of environments for each application
- [ ] Reading OIDC JWT token content, extract user's full name and groups claim from a JWT (no JWT validation at the moment, delegating it to an oauth2-proxy)
- [ ] Determine user permissions on known application configurations
- [ ] List existing dumps for chosen application & source environment
- [ ] Trigger a dump load task for the chose application, source and destination environments
- [ ] Display dump restore task status

## Technologies
This project should be developed using a REST API (using python's [FastAPI][1] lightweight framework) for the backend, and [Angular][2] for the frontend.

The deployment target will first be a K8S cluster.

[1]: https://fastapi.tiangolo.com/
[2]: https://angular.io/
