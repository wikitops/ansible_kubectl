import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    pkg = ["kubectl"]
    assert host.package(pkg).is_installed


def test_directories(host):
    d = host.file("/home/molecule/.kube")
    assert d.exists
    assert d.is_directory
    assert d.user == 'molecule'
    assert d.group == 'molecule'


def test_config_file(host):
    f = host.file("/home/molecule/.kube/config")
    assert f.exists
    assert f.is_file
    assert f.user == 'molecule'
    assert f.group == 'molecule'


def test_completion_file(host):
    f = host.file("/home/molecule/.kube/completion.sh")
    assert f.exists
    assert f.is_file
    assert f.user == 'molecule'
    assert f.group == 'molecule'
