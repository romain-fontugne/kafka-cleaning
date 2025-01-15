# kafka-cleaning
Delete a topic in Kafka, Zookeeper, and on disk

For all the above commands, topics.txt, is a text file with the list of topics
to delete, one topic per line.

The scripts should be run in this order:
- delete in kafka
- delete in zookeeper
- delete on disk

'delete in kafka' is likely to fail if partitions are not all available. 

After that restarting kafka broker is a good idea.
```
sudo systemctl restart confluent-kafka
```

## Delete topics in kafka

```bash
python3 delete_kafka.py topics.txt
```

This will time out for topics that are not clean.


### Delete topics in zookeeper

```bash
python3 delete_zoo.py topics.txt
```

### Delete topics on disk

```bash
python3 delete_disk.py username topics.txt
```
