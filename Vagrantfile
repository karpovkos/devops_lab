# -*- mode: ruby -*-
# vi: set ft=ruby :
nodes = [
  {
    :nodename => "pyth.box",
    :box => "sbeliakou/centos",
    :cpu => 1,
    :mem => 512,
    :ip => "192.168.56.10",
    :run => "run.sh"
  }
]
Vagrant.configure("2") do |config|
   nodes.each do |node|
      config.vm.define node[:nodename] do |pyth|
        pyth.vm.box = node[:box]
        pyth.vm.hostname = node[:nodename]
        pyth.vm.provider "virtualbox" do |v|
            v.name = node[:nodename]
            v.memory = node[:mem]
            v.cpus = node[:cpu]
         end
        pyth.vm.network "private_network", ip: node[:ip]
        pyth.vm.provision "shell", path: node[:run]
       end
   end
end