#!/bin/sh

sudo virsh destroy seed
sudo virsh undefine seed

for i in $(seq 0 2) ; do
  sudo virsh destroy baremetal_$i
  sudo virsh undefine baremetal_$i
  sudo virsh vol-delete --pool default baremetal-$i.qcow2
done

sudo virsh net-destroy brbm
sudo virsh net-undefine brbm

sudo ovs-vsctl del-br brbm

if [ "$TRIPLEO_ROOT" != "" ]; then
  rm $TRIPLEO_ROOT/tripleo-passwords
else
  echo "TRIPLEO_ROOT unset, unable to complete clean"
fi
