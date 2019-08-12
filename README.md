[![Build Status](https://travis-ci.org/bihealth/ansible-role-nginx.svg?branch=master)](https://travis-ci.org/bihealth/ansible-role-nginx)

# Setup of NGINX

This role performs the setup of NGINX (focus is as a reverse proxy for Django sites).

## Requirements

You have to configure the SSL certificate at least for the `nginx_cert_name` (defaults to `inventory_hostname`).

## Role Variables

See `defaults/main.yml` for a description of all variables with their defaults.

## Dependencies

- `bihealth.ssl_certs`

## Example Playbook

```yaml
- hosts: servers
  vars:
    ssl_ssl_certs:
      - name: example.com
    nginx_cert_name: example.com
  roles:
    - role: bihealth.ansible-role-nginx
```

## License

MIT

## Author Information

- Manuel Holtgrewe

Created with love at [Core Unit Bioinformatics (CUBI), Berlin Institute of Health (BIH)](https://www.cubi.bihealth.org).
