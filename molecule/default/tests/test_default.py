import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_conf_file(host):
    f = host.file('/etc/nginx/nginx.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_external_socket(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening
    assert host.socket("tcp://0.0.0.0:443").is_listening
