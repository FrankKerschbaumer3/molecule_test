import os
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def nginx_config_exists(host):
    host = host.file("/var/www/html/index.html").exists
    assert nginx_config_exists


def nginx_index_exists(host):
    host = host.file("/etc/nginx/nginx.conf").exists
    assert nginx_index_exists


def test_nginx_is_installed(host):
    host = host.package("nginx")
    assert test_nginx_is_installed


def test_curl_is_installed(host):
    host = host.package("curl")
    assert test_nginx_is_installed


def nginx_is_hosting(host):
    host = host.socket("tcp://1.0.0.0:80").is_listening
    assert nginx_is_hosting
