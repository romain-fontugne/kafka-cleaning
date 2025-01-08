import paramiko
import sys

DATA_DIR = '/export/dd?/kafka/'

def delete_topic(server, connection, topic):

    if not topic:
        return

    path = f"{DATA_DIR}/{topic}-?"
    print(path)
    command = "sudo rm -rf "+path
    #command = 'sudo ls '+path
    _stdin, stdout, _stderr = connection.exec_command(command)
    lines = stdout.read().decode()
    print(lines)


def key_based_connect(server, user):
    pkey = paramiko.Ed25519Key.from_private_key_file(f"/home/{user}/.ssh/id_ed25519")
    #pkey = paramiko.RSAKey.from_private_key_file(f"/home/{user}/.ssh/id_rsa")
    client = paramiko.SSHClient()
    policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(policy)
    client.connect(server, username=user, pkey=pkey)
    return client

def main():
    user = sys.argv[1] 
    server_list = ["kafka1", "kafka2", "kafka3", "kafka4"]

    fname = sys.argv[2]
    topics = []
    with open(fname, 'r') as fp:
        topics = fp.read().splitlines()

    for server in server_list:
        connection = key_based_connect(server, user)
        print(f'Connecting to {server}...')
        if connection is None:
            print(f'Error, cannot connect to {server}')
            continue

        for topic in topics:
            delete_topic(server, connection, topic)
        connection.close()

main()
