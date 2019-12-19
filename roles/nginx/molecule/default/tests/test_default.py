import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_is_installed(host):
    ngx = host.package("nginx")
    assert ngx.is_installed


def test_nginx_running_and_enabled(host):
    ngx = host.service("nginx")
    assert ngx.is_running
    assert ngx.is_enabled


def test_nginx_listening_http(host):
    ngx = host.socket('tcp://0.0.0.0:80')
    assert ngx.is_listening
