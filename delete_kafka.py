import sys
from kafka import KafkaAdminClient

def example_delete_topics(a, topics):
    """ delete topics """

    # Call delete_topics to asynchronously delete topics, a future is returned.
    # By default this operation on the broker returns immediately while
    # topics are deleted in the background. But here we give it some time (30s)
    # to propagate in the cluster before returning.
    #
    # Returns a dict of <topic,future>.
    fs = a.delete_topics(topics, operation_timeout=30)

    # Wait for operation to finish.
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print("Topic {} deleted".format(topic))
        except Exception as e:
            print("Failed to delete topic {}: {}".format(topic, e))

def main():
    admin_client = KafkaAdminClient(bootstrap_servers=['localhost:9092'])

    fname = sys.argv[1]
    topics = []

    with open(fname, 'r') as fp:
        topics = fp.read().splitlines()

    delete_topics(admin_client, topics) 
